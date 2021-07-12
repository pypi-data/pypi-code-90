'''
Portions of this code copyright 2017, Clement Pinard
'''
from argparse import Namespace
from pathlib import Path

import torch
import torch.nn as nn
from torch.nn import init

from .submodules import *
from .flownet_base import FlowNetBase


class FlowNetSD(FlowNetBase):
    pretrained_checkpoints = {
        'things': 'https://github.com/hmorimitsu/ptlflow/releases/download/weights1/flownetsd-things-c5f3124e.ckpt'
    }

    def __init__(self,
                 args: Namespace):
        super(FlowNetSD, self).__init__(args)

        self.conv0   = conv(self.args.batch_norm,  6,   64)
        self.conv1   = conv(self.args.batch_norm,  64,   64, stride=2)
        self.conv1_1 = conv(self.args.batch_norm,  64,   128)
        self.conv2   = conv(self.args.batch_norm,  128,  128, stride=2)
        self.conv2_1 = conv(self.args.batch_norm,  128,  128)
        self.conv3   = conv(self.args.batch_norm, 128,  256, stride=2)
        self.conv3_1 = conv(self.args.batch_norm, 256,  256)
        self.conv4   = conv(self.args.batch_norm, 256,  512, stride=2)
        self.conv4_1 = conv(self.args.batch_norm, 512,  512)
        self.conv5   = conv(self.args.batch_norm, 512,  512, stride=2)
        self.conv5_1 = conv(self.args.batch_norm, 512,  512)
        self.conv6   = conv(self.args.batch_norm, 512, 1024, stride=2)
        self.conv6_1 = conv(self.args.batch_norm,1024, 1024)

        self.deconv5 = deconv(1024,512)
        self.deconv4 = deconv(1026,256)
        self.deconv3 = deconv(770,128)
        self.deconv2 = deconv(386,64)

        self.inter_conv5 = i_conv(self.args.batch_norm,  1026,   512)
        self.inter_conv4 = i_conv(self.args.batch_norm,  770,   256)
        self.inter_conv3 = i_conv(self.args.batch_norm,  386,   128)
        self.inter_conv2 = i_conv(self.args.batch_norm,  194,   64)

        self.predict_flow6 = predict_flow(1024)
        self.predict_flow5 = predict_flow(512)
        self.predict_flow4 = predict_flow(256)
        self.predict_flow3 = predict_flow(128)
        self.predict_flow2 = predict_flow(64)

        self.upsampled_flow6_to_5 = nn.ConvTranspose2d(2, 2, 4, 2, 1)
        self.upsampled_flow5_to_4 = nn.ConvTranspose2d(2, 2, 4, 2, 1)
        self.upsampled_flow4_to_3 = nn.ConvTranspose2d(2, 2, 4, 2, 1)
        self.upsampled_flow3_to_2 = nn.ConvTranspose2d(2, 2, 4, 2, 1)

        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                if m.bias is not None:
                    init.uniform_(m.bias)
                init.xavier_uniform_(m.weight)

            if isinstance(m, nn.ConvTranspose2d):
                if m.bias is not None:
                    init.uniform_(m.bias)
                init.xavier_uniform_(m.weight)
                # init_deconv_bilinear(m.weight)
        self.upsample1 = nn.Upsample(scale_factor=4, mode='bilinear', align_corners=False)

    def forward(self, inputs):
        x = inputs['images']

        x = x.view(x.shape[0], x.shape[1]*x.shape[2], x.shape[3], x.shape[4])
        out_conv0 = self.conv0(x)
        out_conv1 = self.conv1_1(self.conv1(out_conv0))
        out_conv2 = self.conv2_1(self.conv2(out_conv1))

        out_conv3 = self.conv3_1(self.conv3(out_conv2))
        out_conv4 = self.conv4_1(self.conv4(out_conv3))
        out_conv5 = self.conv5_1(self.conv5(out_conv4))
        out_conv6 = self.conv6_1(self.conv6(out_conv5))

        flow6       = self.predict_flow6(out_conv6)
        flow6_up    = self.upsampled_flow6_to_5(flow6)
        out_deconv5 = self.deconv5(out_conv6)
        
        concat5 = torch.cat((out_conv5,out_deconv5,flow6_up),1)
        out_interconv5 = self.inter_conv5(concat5)
        flow5       = self.predict_flow5(out_interconv5)

        flow5_up    = self.upsampled_flow5_to_4(flow5)
        out_deconv4 = self.deconv4(concat5)
        
        concat4 = torch.cat((out_conv4,out_deconv4,flow5_up),1)
        out_interconv4 = self.inter_conv4(concat4)
        flow4       = self.predict_flow4(out_interconv4)
        flow4_up    = self.upsampled_flow4_to_3(flow4)
        out_deconv3 = self.deconv3(concat4)
        
        concat3 = torch.cat((out_conv3,out_deconv3,flow4_up),1)
        out_interconv3 = self.inter_conv3(concat3)
        flow3       = self.predict_flow3(out_interconv3)
        flow3_up    = self.upsampled_flow3_to_2(flow3)
        out_deconv2 = self.deconv2(concat3)

        concat2 = torch.cat((out_conv2,out_deconv2,flow3_up),1)
        out_interconv2 = self.inter_conv2(concat2)
        flow2 = self.predict_flow2(out_interconv2)

        outputs = {}

        if self.training:
            outputs['flow_preds'] = [flow2.float(),flow3.float(),flow4.float(),flow5.float(),flow6.float()]
            outputs['flows'] = self.upsample1(flow2.float())[:, None] / self.args.div_flow
        else:
            outputs['flows'] = self.upsample1(flow2.float())[:, None] / self.args.div_flow

        return outputs

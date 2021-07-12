# -*- coding: utf-8 -*-
# **********************************************************************
#
# Copyright (c) 2003-2017 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.6.4
#
# <auto-generated>
#
# Generated from file `Arc.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_IObject_ice
import omero_RTypes_ice
import omero_model_RTypes_ice
import omero_System_ice
import omero_Collections_ice
import omero_model_LightSource_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module Ice
_M_Ice = Ice.openModule('Ice')

# Included module omero.sys
_M_omero.sys = Ice.openModule('omero.sys')

# Included module omero.api
_M_omero.api = Ice.openModule('omero.api')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'ArcType' not in _M_omero.model.__dict__:
    _M_omero.model._t_ArcType = IcePy.declareClass('::omero::model::ArcType')
    _M_omero.model._t_ArcTypePrx = IcePy.declareProxy('::omero::model::ArcType')

if 'Power' not in _M_omero.model.__dict__:
    _M_omero.model._t_Power = IcePy.declareClass('::omero::model::Power')
    _M_omero.model._t_PowerPrx = IcePy.declareProxy('::omero::model::Power')

if 'Instrument' not in _M_omero.model.__dict__:
    _M_omero.model._t_Instrument = IcePy.declareClass('::omero::model::Instrument')
    _M_omero.model._t_InstrumentPrx = IcePy.declareProxy('::omero::model::Instrument')

if 'LightSourceAnnotationLink' not in _M_omero.model.__dict__:
    _M_omero.model._t_LightSourceAnnotationLink = IcePy.declareClass('::omero::model::LightSourceAnnotationLink')
    _M_omero.model._t_LightSourceAnnotationLinkPrx = IcePy.declareProxy('::omero::model::LightSourceAnnotationLink')

if 'Annotation' not in _M_omero.model.__dict__:
    _M_omero.model._t_Annotation = IcePy.declareClass('::omero::model::Annotation')
    _M_omero.model._t_AnnotationPrx = IcePy.declareProxy('::omero::model::Annotation')

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'Arc' not in _M_omero.model.__dict__:
    _M_omero.model.Arc = Ice.createTempClass()
    class Arc(_M_omero.model.LightSource):
        def __init__(self, _id=None, _details=None, _loaded=False, _version=None, _manufacturer=None, _model=None, _power=None, _lotNumber=None, _serialNumber=None, _instrument=None, _annotationLinksSeq=None, _annotationLinksLoaded=False, _annotationLinksCountPerOwner=None, _type=None):
            if Ice.getType(self) == _M_omero.model.Arc:
                raise RuntimeError('omero.model.Arc is an abstract class')
            _M_omero.model.LightSource.__init__(self, _id, _details, _loaded, _version, _manufacturer, _model, _power, _lotNumber, _serialNumber, _instrument, _annotationLinksSeq, _annotationLinksLoaded, _annotationLinksCountPerOwner)
            self._type = _type

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Arc', '::omero::model::IObject', '::omero::model::LightSource')

        def ice_id(self, current=None):
            return '::omero::model::Arc'

        def ice_staticId():
            return '::omero::model::Arc'
        ice_staticId = staticmethod(ice_staticId)

        def getType(self, current=None):
            pass

        def setType(self, theType, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Arc)

        __repr__ = __str__

    _M_omero.model.ArcPrx = Ice.createTempClass()
    class ArcPrx(_M_omero.model.LightSourcePrx):

        def getType(self, _ctx=None):
            return _M_omero.model.Arc._op_getType.invoke(self, ((), _ctx))

        def begin_getType(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Arc._op_getType.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getType(self, _r):
            return _M_omero.model.Arc._op_getType.end(self, _r)

        def setType(self, theType, _ctx=None):
            return _M_omero.model.Arc._op_setType.invoke(self, ((theType, ), _ctx))

        def begin_setType(self, theType, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Arc._op_setType.begin(self, ((theType, ), _response, _ex, _sent, _ctx))

        def end_setType(self, _r):
            return _M_omero.model.Arc._op_setType.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ArcPrx.ice_checkedCast(proxy, '::omero::model::Arc', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ArcPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Arc'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_ArcPrx = IcePy.defineProxy('::omero::model::Arc', ArcPrx)

    _M_omero.model._t_Arc = IcePy.declareClass('::omero::model::Arc')

    _M_omero.model._t_Arc = IcePy.defineClass('::omero::model::Arc', Arc, -1, (), True, False, _M_omero.model._t_LightSource, (), (('_type', (), _M_omero.model._t_ArcType, False, 0),))
    Arc._ice_type = _M_omero.model._t_Arc

    Arc._op_getType = IcePy.Operation('getType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_ArcType, False, 0), ())
    Arc._op_setType = IcePy.Operation('setType', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model._t_ArcType, False, 0),), (), None, ())

    _M_omero.model.Arc = Arc
    del Arc

    _M_omero.model.ArcPrx = ArcPrx
    del ArcPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero

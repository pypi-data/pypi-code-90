#!/usr/bin/env python

#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

import glob
import sys
sys.path.append('gen-py.twisted')
sys.path.insert(0, glob.glob('../../lib/py/build/lib*')[0])

from tutorial import Calculator
from tutorial.ttypes import InvalidOperation, Operation

from shared.ttypes import SharedStruct

from zope.interface import implements
from twisted.internet import reactor

from thrift.transport import TTwisted
from thrift.protocol import TBinaryProtocol


class CalculatorHandler:
    implements(Calculator.Iface)

    def __init__(self):
        self.log = {}

    def ping(self):
        print('ping()')

    def add(self, n1, n2):
        print('add(%d,%d)' % (n1, n2))
        return n1 + n2

    def calculate(self, logid, work):
        print('calculate(%d, %r)' % (logid, work))

        if work.op == Operation.ADD:
            val = work.num1 + work.num2
        elif work.op == Operation.SUBTRACT:
            val = work.num1 - work.num2
        elif work.op == Operation.MULTIPLY:
            val = work.num1 * work.num2
        elif work.op == Operation.DIVIDE:
            if work.num2 == 0:
                raise InvalidOperation(work.op, 'Cannot divide by 0')
            val = work.num1 / work.num2
        else:
            raise InvalidOperation(work.op, 'Invalid operation')

        log = SharedStruct()
        log.key = logid
        log.value = '%d' % (val)
        self.log[logid] = log

        return val

    def getStruct(self, key):
        print('getStruct(%d)' % (key))
        return self.log[key]

    def zip(self):
        print('zip()')


if __name__ == '__main__':
    handler = CalculatorHandler()
    processor = Calculator.Processor(handler)
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = reactor.listenTCP(
        9090,
        TTwisted.ThriftServerFactory(processor, pfactory),
        interface="127.0.0.1")
    reactor.run()

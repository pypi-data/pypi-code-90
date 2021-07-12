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
# Generated from file `ProjectionAxis.ice'
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

# Start of module omero.model.enums
_M_omero.model.enums = Ice.openModule('omero.model.enums')
__name__ = 'omero.model.enums'

_M_omero.model.enums.ProjectionAxisT = "T"

_M_omero.model.enums.ProjectionAxisModuloT = "ModuloT"

_M_omero.model.enums.ProjectionAxisZ = "Z"

_M_omero.model.enums.ProjectionAxisModuloZ = "ModuloZ"

# End of module omero.model.enums

__name__ = 'omero.model'

if 'Details' not in _M_omero.model.__dict__:
    _M_omero.model._t_Details = IcePy.declareClass('::omero::model::Details')
    _M_omero.model._t_DetailsPrx = IcePy.declareProxy('::omero::model::Details')

if 'ProjectionAxis' not in _M_omero.model.__dict__:
    _M_omero.model.ProjectionAxis = Ice.createTempClass()
    class ProjectionAxis(_M_omero.model.IObject):
        def __init__(self, _id=None, _details=None, _loaded=False, _value=None):
            if Ice.getType(self) == _M_omero.model.ProjectionAxis:
                raise RuntimeError('omero.model.ProjectionAxis is an abstract class')
            _M_omero.model.IObject.__init__(self, _id, _details, _loaded)
            self._value = _value

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::IObject', '::omero::model::ProjectionAxis')

        def ice_id(self, current=None):
            return '::omero::model::ProjectionAxis'

        def ice_staticId():
            return '::omero::model::ProjectionAxis'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            pass

        def setValue(self, theValue, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_ProjectionAxis)

        __repr__ = __str__

    _M_omero.model.ProjectionAxisPrx = Ice.createTempClass()
    class ProjectionAxisPrx(_M_omero.model.IObjectPrx):

        def getValue(self, _ctx=None):
            return _M_omero.model.ProjectionAxis._op_getValue.invoke(self, ((), _ctx))

        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ProjectionAxis._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_getValue(self, _r):
            return _M_omero.model.ProjectionAxis._op_getValue.end(self, _r)

        def setValue(self, theValue, _ctx=None):
            return _M_omero.model.ProjectionAxis._op_setValue.invoke(self, ((theValue, ), _ctx))

        def begin_setValue(self, theValue, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.ProjectionAxis._op_setValue.begin(self, ((theValue, ), _response, _ex, _sent, _ctx))

        def end_setValue(self, _r):
            return _M_omero.model.ProjectionAxis._op_setValue.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.ProjectionAxisPrx.ice_checkedCast(proxy, '::omero::model::ProjectionAxis', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.ProjectionAxisPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::ProjectionAxis'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_ProjectionAxisPrx = IcePy.defineProxy('::omero::model::ProjectionAxis', ProjectionAxisPrx)

    _M_omero.model._t_ProjectionAxis = IcePy.declareClass('::omero::model::ProjectionAxis')

    _M_omero.model._t_ProjectionAxis = IcePy.defineClass('::omero::model::ProjectionAxis', ProjectionAxis, -1, (), True, False, _M_omero.model._t_IObject, (), (('_value', (), _M_omero._t_RString, False, 0),))
    ProjectionAxis._ice_type = _M_omero.model._t_ProjectionAxis

    ProjectionAxis._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero._t_RString, False, 0), ())
    ProjectionAxis._op_setValue = IcePy.Operation('setValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero._t_RString, False, 0),), (), None, ())

    _M_omero.model.ProjectionAxis = ProjectionAxis
    del ProjectionAxis

    _M_omero.model.ProjectionAxisPrx = ProjectionAxisPrx
    del ProjectionAxisPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero

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
# Generated from file `Length.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy
import omero_model_Units_ice

# Included module omero
_M_omero = Ice.openModule('omero')

# Included module omero.model
_M_omero.model = Ice.openModule('omero.model')

# Included module omero.model.enums
_M_omero.model.enums = Ice.openModule('omero.model.enums')

# Start of module omero
__name__ = 'omero'

# Start of module omero.model
__name__ = 'omero.model'

if 'Length' not in _M_omero.model.__dict__:
    _M_omero.model.Length = Ice.createTempClass()
    class Length(Ice.Object):
        """
        Unit of Length which is used through the model. This is not
        an omero.model.IObject implementation and as such does
        not have an ID value. Instead, the entire object is embedded
        into the containing class, so that the value and unit rows
        can be found on the table itself (e.g. pixels.physicalSizeX
        and pixels.physicalSizeXUnit).
        Members:
        value -- PositiveFloat value
        unit -- 
        """
        def __init__(self, _value=0.0, _unit=_M_omero.model.enums.UnitsLength.YOTTAMETER):
            if Ice.getType(self) == _M_omero.model.Length:
                raise RuntimeError('omero.model.Length is an abstract class')
            self._value = _value
            self._unit = _unit

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::omero::model::Length')

        def ice_id(self, current=None):
            return '::omero::model::Length'

        def ice_staticId():
            return '::omero::model::Length'
        ice_staticId = staticmethod(ice_staticId)

        def getValue(self, current=None):
            """
            Actual value for this unit-based field. The interpretation of
            the value is only possible along with the
            omero.model.enums.UnitsLength enum.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def setValue(self, value, current=None):
            pass

        def getUnit(self, current=None):
            """
            omero.model.enums.UnitsLength instance which is an
            omero.model.IObject
            meaning that its ID is sufficient for identifying equality.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def setUnit(self, unit, current=None):
            pass

        def getSymbol(self, current=None):
            """
            Returns the possibly unicode representation of the ""unit""
            value for display.
            Arguments:
            current -- The Current object for the invocation.
            """
            pass

        def copy(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_omero.model._t_Length)

        __repr__ = __str__

    _M_omero.model.LengthPrx = Ice.createTempClass()
    class LengthPrx(Ice.ObjectPrx):

        """
        Actual value for this unit-based field. The interpretation of
        the value is only possible along with the
        omero.model.enums.UnitsLength enum.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getValue(self, _ctx=None):
            return _M_omero.model.Length._op_getValue.invoke(self, ((), _ctx))

        """
        Actual value for this unit-based field. The interpretation of
        the value is only possible along with the
        omero.model.enums.UnitsLength enum.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getValue(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_getValue.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Actual value for this unit-based field. The interpretation of
        the value is only possible along with the
        omero.model.enums.UnitsLength enum.
        Arguments:
        """
        def end_getValue(self, _r):
            return _M_omero.model.Length._op_getValue.end(self, _r)

        def setValue(self, value, _ctx=None):
            return _M_omero.model.Length._op_setValue.invoke(self, ((value, ), _ctx))

        def begin_setValue(self, value, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_setValue.begin(self, ((value, ), _response, _ex, _sent, _ctx))

        def end_setValue(self, _r):
            return _M_omero.model.Length._op_setValue.end(self, _r)

        """
        omero.model.enums.UnitsLength instance which is an
        omero.model.IObject
        meaning that its ID is sufficient for identifying equality.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getUnit(self, _ctx=None):
            return _M_omero.model.Length._op_getUnit.invoke(self, ((), _ctx))

        """
        omero.model.enums.UnitsLength instance which is an
        omero.model.IObject
        meaning that its ID is sufficient for identifying equality.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getUnit(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_getUnit.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        omero.model.enums.UnitsLength instance which is an
        omero.model.IObject
        meaning that its ID is sufficient for identifying equality.
        Arguments:
        """
        def end_getUnit(self, _r):
            return _M_omero.model.Length._op_getUnit.end(self, _r)

        def setUnit(self, unit, _ctx=None):
            return _M_omero.model.Length._op_setUnit.invoke(self, ((unit, ), _ctx))

        def begin_setUnit(self, unit, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_setUnit.begin(self, ((unit, ), _response, _ex, _sent, _ctx))

        def end_setUnit(self, _r):
            return _M_omero.model.Length._op_setUnit.end(self, _r)

        """
        Returns the possibly unicode representation of the ""unit""
        value for display.
        Arguments:
        _ctx -- The request context for the invocation.
        """
        def getSymbol(self, _ctx=None):
            return _M_omero.model.Length._op_getSymbol.invoke(self, ((), _ctx))

        """
        Returns the possibly unicode representation of the ""unit""
        value for display.
        Arguments:
        _response -- The asynchronous response callback.
        _ex -- The asynchronous exception callback.
        _sent -- The asynchronous sent callback.
        _ctx -- The request context for the invocation.
        Returns: An asynchronous result object for the invocation.
        """
        def begin_getSymbol(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_getSymbol.begin(self, ((), _response, _ex, _sent, _ctx))

        """
        Returns the possibly unicode representation of the ""unit""
        value for display.
        Arguments:
        """
        def end_getSymbol(self, _r):
            return _M_omero.model.Length._op_getSymbol.end(self, _r)

        def copy(self, _ctx=None):
            return _M_omero.model.Length._op_copy.invoke(self, ((), _ctx))

        def begin_copy(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_omero.model.Length._op_copy.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_copy(self, _r):
            return _M_omero.model.Length._op_copy.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_omero.model.LengthPrx.ice_checkedCast(proxy, '::omero::model::Length', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_omero.model.LengthPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

        def ice_staticId():
            return '::omero::model::Length'
        ice_staticId = staticmethod(ice_staticId)

    _M_omero.model._t_LengthPrx = IcePy.defineProxy('::omero::model::Length', LengthPrx)

    _M_omero.model._t_Length = IcePy.defineClass('::omero::model::Length', Length, -1, (), True, False, None, (), (
        ('_value', (), IcePy._t_double, False, 0),
        ('_unit', (), _M_omero.model.enums._t_UnitsLength, False, 0)
    ))
    Length._ice_type = _M_omero.model._t_Length

    Length._op_getValue = IcePy.Operation('getValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_double, False, 0), ())
    Length._op_setValue = IcePy.Operation('setValue', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_double, False, 0),), (), None, ())
    Length._op_getUnit = IcePy.Operation('getUnit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model.enums._t_UnitsLength, False, 0), ())
    Length._op_setUnit = IcePy.Operation('setUnit', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_omero.model.enums._t_UnitsLength, False, 0),), (), None, ())
    Length._op_getSymbol = IcePy.Operation('getSymbol', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_string, False, 0), ())
    Length._op_copy = IcePy.Operation('copy', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_omero.model._t_Length, False, 0), ())

    _M_omero.model.Length = Length
    del Length

    _M_omero.model.LengthPrx = LengthPrx
    del LengthPrx

# End of module omero.model

__name__ = 'omero'

# End of module omero

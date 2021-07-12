# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3257
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class AggregationQuery(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'address_key': 'str',
        'description': 'str',
        'display_name': 'str',
        'type': 'str',
        'scales_with_holding_quantity': 'bool',
        'supported_operations': 'str'
    }

    attribute_map = {
        'address_key': 'addressKey',
        'description': 'description',
        'display_name': 'displayName',
        'type': 'type',
        'scales_with_holding_quantity': 'scalesWithHoldingQuantity',
        'supported_operations': 'supportedOperations'
    }

    required_map = {
        'address_key': 'required',
        'description': 'required',
        'display_name': 'required',
        'type': 'required',
        'scales_with_holding_quantity': 'required',
        'supported_operations': 'required'
    }

    def __init__(self, address_key=None, description=None, display_name=None, type=None, scales_with_holding_quantity=None, supported_operations=None):  # noqa: E501
        """
        AggregationQuery - a model defined in OpenAPI

        :param address_key:  The address that is the query to be made into the system. e.g. a Valuation/Pv or Instrument/MaturityDate (required)
        :type address_key: str
        :param description:  What does the information that is being queried by the address mean. What is the address for. (required)
        :type description: str
        :param display_name:  The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address. (required)
        :type display_name: str
        :param type:  The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Array, Map, Json (required)
        :type type: str
        :param scales_with_holding_quantity:  Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and pv. The present value  of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the  contract size. (required)
        :type scales_with_holding_quantity: bool
        :param supported_operations:  When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but  not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency  of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not  when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context). (required)
        :type supported_operations: str

        """  # noqa: E501

        self._address_key = None
        self._description = None
        self._display_name = None
        self._type = None
        self._scales_with_holding_quantity = None
        self._supported_operations = None
        self.discriminator = None

        self.address_key = address_key
        self.description = description
        self.display_name = display_name
        self.type = type
        self.scales_with_holding_quantity = scales_with_holding_quantity
        self.supported_operations = supported_operations

    @property
    def address_key(self):
        """Gets the address_key of this AggregationQuery.  # noqa: E501

        The address that is the query to be made into the system. e.g. a Valuation/Pv or Instrument/MaturityDate  # noqa: E501

        :return: The address_key of this AggregationQuery.  # noqa: E501
        :rtype: str
        """
        return self._address_key

    @address_key.setter
    def address_key(self, address_key):
        """Sets the address_key of this AggregationQuery.

        The address that is the query to be made into the system. e.g. a Valuation/Pv or Instrument/MaturityDate  # noqa: E501

        :param address_key: The address_key of this AggregationQuery.  # noqa: E501
        :type: str
        """
        if address_key is None:
            raise ValueError("Invalid value for `address_key`, must not be `None`")  # noqa: E501

        self._address_key = address_key

    @property
    def description(self):
        """Gets the description of this AggregationQuery.  # noqa: E501

        What does the information that is being queried by the address mean. What is the address for.  # noqa: E501

        :return: The description of this AggregationQuery.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AggregationQuery.

        What does the information that is being queried by the address mean. What is the address for.  # noqa: E501

        :param description: The description of this AggregationQuery.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def display_name(self):
        """Gets the display_name of this AggregationQuery.  # noqa: E501

        The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address.  # noqa: E501

        :return: The display_name of this AggregationQuery.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AggregationQuery.

        The suggested name that the user would wish to put on to the returned information for visualisation in preference to the address.  # noqa: E501

        :param display_name: The display_name of this AggregationQuery.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def type(self):
        """Gets the type of this AggregationQuery.  # noqa: E501

        The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Array, Map, Json  # noqa: E501

        :return: The type of this AggregationQuery.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AggregationQuery.

        The available values are: String, Int, Decimal, DateTime, Boolean, ResultValue, Array, Map, Json  # noqa: E501

        :param type: The type of this AggregationQuery.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["String", "Int", "Decimal", "DateTime", "Boolean", "ResultValue", "Array", "Map", "Json"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def scales_with_holding_quantity(self):
        """Gets the scales_with_holding_quantity of this AggregationQuery.  # noqa: E501

        Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and pv. The present value  of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the  contract size.  # noqa: E501

        :return: The scales_with_holding_quantity of this AggregationQuery.  # noqa: E501
        :rtype: bool
        """
        return self._scales_with_holding_quantity

    @scales_with_holding_quantity.setter
    def scales_with_holding_quantity(self, scales_with_holding_quantity):
        """Sets the scales_with_holding_quantity of this AggregationQuery.

        Is the data scaled when it is for, e.g. a holding in an instrument. A key example would be the difference between price and pv. The present value  of an instrument would scale with the quantity held. The price would be that for a hypothetical unit of that instrument, typically associated with the  contract size.  # noqa: E501

        :param scales_with_holding_quantity: The scales_with_holding_quantity of this AggregationQuery.  # noqa: E501
        :type: bool
        """
        if scales_with_holding_quantity is None:
            raise ValueError("Invalid value for `scales_with_holding_quantity`, must not be `None`")  # noqa: E501

        self._scales_with_holding_quantity = scales_with_holding_quantity

    @property
    def supported_operations(self):
        """Gets the supported_operations of this AggregationQuery.  # noqa: E501

        When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but  not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency  of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not  when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context).  # noqa: E501

        :return: The supported_operations of this AggregationQuery.  # noqa: E501
        :rtype: str
        """
        return self._supported_operations

    @supported_operations.setter
    def supported_operations(self, supported_operations):
        """Sets the supported_operations of this AggregationQuery.

        When performing an aggregation operation, what column type operations can be performed on the data. For example, it makes sense to sum decimals but  not strings. Either can be counted. With more complex types, e.g. ResultValues, operations may be linked to a semantic meaning such as the currency  of the result. In such cases the operations may be supported but context specific. For example, it makes sense to sum PVs in a single currency but not  when the currency is different. In such cases, an error would result (it being assumed that no fx rates for currency conversion were implicit in the context).  # noqa: E501

        :param supported_operations: The supported_operations of this AggregationQuery.  # noqa: E501
        :type: str
        """
        if supported_operations is None:
            raise ValueError("Invalid value for `supported_operations`, must not be `None`")  # noqa: E501

        self._supported_operations = supported_operations

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AggregationQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

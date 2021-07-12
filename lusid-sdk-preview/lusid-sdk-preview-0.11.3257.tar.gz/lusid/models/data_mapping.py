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

class DataMapping(object):
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
        'data_definitions': 'list[DataDefinition]'
    }

    attribute_map = {
        'data_definitions': 'dataDefinitions'
    }

    required_map = {
        'data_definitions': 'optional'
    }

    def __init__(self, data_definitions=None):  # noqa: E501
        """
        DataMapping - a model defined in OpenAPI

        :param data_definitions:  A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores.
        :type data_definitions: list[lusid.DataDefinition]

        """  # noqa: E501

        self._data_definitions = None
        self.discriminator = None

        self.data_definitions = data_definitions

    @property
    def data_definitions(self):
        """Gets the data_definitions of this DataMapping.  # noqa: E501

        A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores.  # noqa: E501

        :return: The data_definitions of this DataMapping.  # noqa: E501
        :rtype: list[DataDefinition]
        """
        return self._data_definitions

    @data_definitions.setter
    def data_definitions(self, data_definitions):
        """Sets the data_definitions of this DataMapping.

        A map from LUSID item keys to data definitions that define the names, types and degree of uniqueness of data provided to LUSID in structured data stores.  # noqa: E501

        :param data_definitions: The data_definitions of this DataMapping.  # noqa: E501
        :type: list[DataDefinition]
        """

        self._data_definitions = data_definitions

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
        if not isinstance(other, DataMapping):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

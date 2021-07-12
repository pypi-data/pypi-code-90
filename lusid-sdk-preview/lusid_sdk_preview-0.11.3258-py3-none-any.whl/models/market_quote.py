# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3258
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

class MarketQuote(object):
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
        'quote_type': 'str',
        'value': 'float'
    }

    attribute_map = {
        'quote_type': 'quoteType',
        'value': 'value'
    }

    required_map = {
        'quote_type': 'required',
        'value': 'required'
    }

    def __init__(self, quote_type=None, value=None):  # noqa: E501
        """
        MarketQuote - a model defined in OpenAPI

        :param quote_type:  The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront (required)
        :type quote_type: str
        :param value:  Numeric value of the quote (required)
        :type value: float

        """  # noqa: E501

        self._quote_type = None
        self._value = None
        self.discriminator = None

        self.quote_type = quote_type
        self.value = value

    @property
    def quote_type(self):
        """Gets the quote_type of this MarketQuote.  # noqa: E501

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront  # noqa: E501

        :return: The quote_type of this MarketQuote.  # noqa: E501
        :rtype: str
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type):
        """Sets the quote_type of this MarketQuote.

        The available values are: Price, Spread, Rate, LogNormalVol, NormalVol, ParSpread, IsdaSpread, Upfront  # noqa: E501

        :param quote_type: The quote_type of this MarketQuote.  # noqa: E501
        :type: str
        """
        if quote_type is None:
            raise ValueError("Invalid value for `quote_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Price", "Spread", "Rate", "LogNormalVol", "NormalVol", "ParSpread", "IsdaSpread", "Upfront"]  # noqa: E501
        if quote_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quote_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_type, allowed_values)
            )

        self._quote_type = quote_type

    @property
    def value(self):
        """Gets the value of this MarketQuote.  # noqa: E501

        Numeric value of the quote  # noqa: E501

        :return: The value of this MarketQuote.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MarketQuote.

        Numeric value of the quote  # noqa: E501

        :param value: The value of this MarketQuote.  # noqa: E501
        :type: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

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
        if not isinstance(other, MarketQuote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

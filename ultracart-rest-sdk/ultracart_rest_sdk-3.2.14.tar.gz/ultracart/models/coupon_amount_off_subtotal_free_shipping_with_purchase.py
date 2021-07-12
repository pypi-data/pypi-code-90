# coding: utf-8

"""
    UltraCart Rest API V2

    UltraCart REST API Version 2  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: support@ultracart.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CouponAmountOffSubtotalFreeShippingWithPurchase(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'currency_code': 'str',
        'discount_amount': 'float',
        'purchase_amount': 'float',
        'shipping_methods': 'list[str]'
    }

    attribute_map = {
        'currency_code': 'currency_code',
        'discount_amount': 'discount_amount',
        'purchase_amount': 'purchase_amount',
        'shipping_methods': 'shipping_methods'
    }

    def __init__(self, currency_code=None, discount_amount=None, purchase_amount=None, shipping_methods=None):  # noqa: E501
        """CouponAmountOffSubtotalFreeShippingWithPurchase - a model defined in Swagger"""  # noqa: E501

        self._currency_code = None
        self._discount_amount = None
        self._purchase_amount = None
        self._shipping_methods = None
        self.discriminator = None

        if currency_code is not None:
            self.currency_code = currency_code
        if discount_amount is not None:
            self.discount_amount = discount_amount
        if purchase_amount is not None:
            self.purchase_amount = purchase_amount
        if shipping_methods is not None:
            self.shipping_methods = shipping_methods

    @property
    def currency_code(self):
        """Gets the currency_code of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :return: The currency_code of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this CouponAmountOffSubtotalFreeShippingWithPurchase.

        The ISO-4217 three letter currency code the customer is viewing prices in  # noqa: E501

        :param currency_code: The currency_code of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :type: str
        """
        if currency_code is not None and len(currency_code) > 3:
            raise ValueError("Invalid value for `currency_code`, length must be less than or equal to `3`")  # noqa: E501

        self._currency_code = currency_code

    @property
    def discount_amount(self):
        """Gets the discount_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501

        The amount of subtotal discount  # noqa: E501

        :return: The discount_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :rtype: float
        """
        return self._discount_amount

    @discount_amount.setter
    def discount_amount(self, discount_amount):
        """Sets the discount_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.

        The amount of subtotal discount  # noqa: E501

        :param discount_amount: The discount_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :type: float
        """

        self._discount_amount = discount_amount

    @property
    def purchase_amount(self):
        """Gets the purchase_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501

        The purchase amount to qualify for subtotal discount and free shipping  # noqa: E501

        :return: The purchase_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :rtype: float
        """
        return self._purchase_amount

    @purchase_amount.setter
    def purchase_amount(self, purchase_amount):
        """Sets the purchase_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.

        The purchase amount to qualify for subtotal discount and free shipping  # noqa: E501

        :param purchase_amount: The purchase_amount of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :type: float
        """

        self._purchase_amount = purchase_amount

    @property
    def shipping_methods(self):
        """Gets the shipping_methods of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501

        One or more shipping methods that may be free  # noqa: E501

        :return: The shipping_methods of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :rtype: list[str]
        """
        return self._shipping_methods

    @shipping_methods.setter
    def shipping_methods(self, shipping_methods):
        """Sets the shipping_methods of this CouponAmountOffSubtotalFreeShippingWithPurchase.

        One or more shipping methods that may be free  # noqa: E501

        :param shipping_methods: The shipping_methods of this CouponAmountOffSubtotalFreeShippingWithPurchase.  # noqa: E501
        :type: list[str]
        """

        self._shipping_methods = shipping_methods

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CouponAmountOffSubtotalFreeShippingWithPurchase, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CouponAmountOffSubtotalFreeShippingWithPurchase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

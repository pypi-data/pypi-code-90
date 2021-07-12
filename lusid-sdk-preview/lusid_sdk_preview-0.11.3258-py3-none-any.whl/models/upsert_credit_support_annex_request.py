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

class UpsertCreditSupportAnnexRequest(object):
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
        'credit_support_annex': 'CreditSupportAnnex'
    }

    attribute_map = {
        'credit_support_annex': 'creditSupportAnnex'
    }

    required_map = {
        'credit_support_annex': 'optional'
    }

    def __init__(self, credit_support_annex=None):  # noqa: E501
        """
        UpsertCreditSupportAnnexRequest - a model defined in OpenAPI

        :param credit_support_annex: 
        :type credit_support_annex: lusid.CreditSupportAnnex

        """  # noqa: E501

        self._credit_support_annex = None
        self.discriminator = None

        if credit_support_annex is not None:
            self.credit_support_annex = credit_support_annex

    @property
    def credit_support_annex(self):
        """Gets the credit_support_annex of this UpsertCreditSupportAnnexRequest.  # noqa: E501


        :return: The credit_support_annex of this UpsertCreditSupportAnnexRequest.  # noqa: E501
        :rtype: CreditSupportAnnex
        """
        return self._credit_support_annex

    @credit_support_annex.setter
    def credit_support_annex(self, credit_support_annex):
        """Sets the credit_support_annex of this UpsertCreditSupportAnnexRequest.


        :param credit_support_annex: The credit_support_annex of this UpsertCreditSupportAnnexRequest.  # noqa: E501
        :type: CreditSupportAnnex
        """

        self._credit_support_annex = credit_support_annex

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
        if not isinstance(other, UpsertCreditSupportAnnexRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

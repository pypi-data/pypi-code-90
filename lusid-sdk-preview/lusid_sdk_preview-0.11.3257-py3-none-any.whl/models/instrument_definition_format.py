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

class InstrumentDefinitionFormat(object):
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
        'source_system': 'str',
        'vendor': 'str',
        'version': 'str'
    }

    attribute_map = {
        'source_system': 'sourceSystem',
        'vendor': 'vendor',
        'version': 'version'
    }

    required_map = {
        'source_system': 'required',
        'vendor': 'required',
        'version': 'required'
    }

    def __init__(self, source_system=None, vendor=None, version=None):  # noqa: E501
        """
        InstrumentDefinitionFormat - a model defined in OpenAPI

        :param source_system:  which source system does the format originate from (required)
        :type source_system: str
        :param vendor:  An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID's), some won't.              The provenance of an instrument indicates who \"owns\" the associated format. (required)
        :type vendor: str
        :param version:  Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations' trade formats. (required)
        :type version: str

        """  # noqa: E501

        self._source_system = None
        self._vendor = None
        self._version = None
        self.discriminator = None

        self.source_system = source_system
        self.vendor = vendor
        self.version = version

    @property
    def source_system(self):
        """Gets the source_system of this InstrumentDefinitionFormat.  # noqa: E501

        which source system does the format originate from  # noqa: E501

        :return: The source_system of this InstrumentDefinitionFormat.  # noqa: E501
        :rtype: str
        """
        return self._source_system

    @source_system.setter
    def source_system(self, source_system):
        """Sets the source_system of this InstrumentDefinitionFormat.

        which source system does the format originate from  # noqa: E501

        :param source_system: The source_system of this InstrumentDefinitionFormat.  # noqa: E501
        :type: str
        """
        if source_system is None:
            raise ValueError("Invalid value for `source_system`, must not be `None`")  # noqa: E501

        self._source_system = source_system

    @property
    def vendor(self):
        """Gets the vendor of this InstrumentDefinitionFormat.  # noqa: E501

        An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID's), some won't.              The provenance of an instrument indicates who \"owns\" the associated format.  # noqa: E501

        :return: The vendor of this InstrumentDefinitionFormat.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this InstrumentDefinitionFormat.

        An instrument will potentially have been created by any number of different organisations. Some will be understood completely (e.g. LUSID's), some won't.              The provenance of an instrument indicates who \"owns\" the associated format.  # noqa: E501

        :param vendor: The vendor of this InstrumentDefinitionFormat.  # noqa: E501
        :type: str
        """
        if vendor is None:
            raise ValueError("Invalid value for `vendor`, must not be `None`")  # noqa: E501

        self._vendor = vendor

    @property
    def version(self):
        """Gets the version of this InstrumentDefinitionFormat.  # noqa: E501

        Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations' trade formats.  # noqa: E501

        :return: The version of this InstrumentDefinitionFormat.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstrumentDefinitionFormat.

        Version of the document. Would be preferable to avoid the need, but LUSID will not control other organisations' trade formats.  # noqa: E501

        :param version: The version of this InstrumentDefinitionFormat.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, InstrumentDefinitionFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

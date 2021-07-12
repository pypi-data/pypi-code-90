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

class ExpandedGroup(object):
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
        'href': 'str',
        'id': 'ResourceId',
        'display_name': 'str',
        'description': 'str',
        'values': 'list[CompletePortfolio]',
        'sub_groups': 'list[ExpandedGroup]',
        'version': 'Version',
        'links': 'list[Link]'
    }

    attribute_map = {
        'href': 'href',
        'id': 'id',
        'display_name': 'displayName',
        'description': 'description',
        'values': 'values',
        'sub_groups': 'subGroups',
        'version': 'version',
        'links': 'links'
    }

    required_map = {
        'href': 'optional',
        'id': 'required',
        'display_name': 'required',
        'description': 'optional',
        'values': 'optional',
        'sub_groups': 'optional',
        'version': 'optional',
        'links': 'optional'
    }

    def __init__(self, href=None, id=None, display_name=None, description=None, values=None, sub_groups=None, version=None, links=None):  # noqa: E501
        """
        ExpandedGroup - a model defined in OpenAPI

        :param href:  The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.
        :type href: str
        :param id:  (required)
        :type id: lusid.ResourceId
        :param display_name:  The name of the portfolio group. (required)
        :type display_name: str
        :param description:  The long form description of the portfolio group.
        :type description: str
        :param values:  The collection of resource identifiers for the portfolios contained in the portfolio group.
        :type values: list[lusid.CompletePortfolio]
        :param sub_groups:  The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.
        :type sub_groups: list[lusid.ExpandedGroup]
        :param version: 
        :type version: lusid.Version
        :param links: 
        :type links: list[lusid.Link]

        """  # noqa: E501

        self._href = None
        self._id = None
        self._display_name = None
        self._description = None
        self._values = None
        self._sub_groups = None
        self._version = None
        self._links = None
        self.discriminator = None

        self.href = href
        self.id = id
        self.display_name = display_name
        self.description = description
        self.values = values
        self.sub_groups = sub_groups
        if version is not None:
            self.version = version
        self.links = links

    @property
    def href(self):
        """Gets the href of this ExpandedGroup.  # noqa: E501

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :return: The href of this ExpandedGroup.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ExpandedGroup.

        The specific Uniform Resource Identifier (URI) for this resource at the requested effective and asAt datetime.  # noqa: E501

        :param href: The href of this ExpandedGroup.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def id(self):
        """Gets the id of this ExpandedGroup.  # noqa: E501


        :return: The id of this ExpandedGroup.  # noqa: E501
        :rtype: ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExpandedGroup.


        :param id: The id of this ExpandedGroup.  # noqa: E501
        :type: ResourceId
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this ExpandedGroup.  # noqa: E501

        The name of the portfolio group.  # noqa: E501

        :return: The display_name of this ExpandedGroup.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ExpandedGroup.

        The name of the portfolio group.  # noqa: E501

        :param display_name: The display_name of this ExpandedGroup.  # noqa: E501
        :type: str
        """
        if display_name is None:
            raise ValueError("Invalid value for `display_name`, must not be `None`")  # noqa: E501

        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ExpandedGroup.  # noqa: E501

        The long form description of the portfolio group.  # noqa: E501

        :return: The description of this ExpandedGroup.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExpandedGroup.

        The long form description of the portfolio group.  # noqa: E501

        :param description: The description of this ExpandedGroup.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def values(self):
        """Gets the values of this ExpandedGroup.  # noqa: E501

        The collection of resource identifiers for the portfolios contained in the portfolio group.  # noqa: E501

        :return: The values of this ExpandedGroup.  # noqa: E501
        :rtype: list[CompletePortfolio]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this ExpandedGroup.

        The collection of resource identifiers for the portfolios contained in the portfolio group.  # noqa: E501

        :param values: The values of this ExpandedGroup.  # noqa: E501
        :type: list[CompletePortfolio]
        """

        self._values = values

    @property
    def sub_groups(self):
        """Gets the sub_groups of this ExpandedGroup.  # noqa: E501

        The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.  # noqa: E501

        :return: The sub_groups of this ExpandedGroup.  # noqa: E501
        :rtype: list[ExpandedGroup]
        """
        return self._sub_groups

    @sub_groups.setter
    def sub_groups(self, sub_groups):
        """Sets the sub_groups of this ExpandedGroup.

        The collection of resource identifiers for the portfolio groups contained in the portfolio group as sub groups.  # noqa: E501

        :param sub_groups: The sub_groups of this ExpandedGroup.  # noqa: E501
        :type: list[ExpandedGroup]
        """

        self._sub_groups = sub_groups

    @property
    def version(self):
        """Gets the version of this ExpandedGroup.  # noqa: E501


        :return: The version of this ExpandedGroup.  # noqa: E501
        :rtype: Version
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExpandedGroup.


        :param version: The version of this ExpandedGroup.  # noqa: E501
        :type: Version
        """

        self._version = version

    @property
    def links(self):
        """Gets the links of this ExpandedGroup.  # noqa: E501


        :return: The links of this ExpandedGroup.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ExpandedGroup.


        :param links: The links of this ExpandedGroup.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

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
        if not isinstance(other, ExpandedGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

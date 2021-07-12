# coding: utf-8

"""
    Data Repository API

    This document defines the REST API for Data Repository. **Status: design in progress** There are four top-level endpoints (besides some used by swagger):  * /swagger-ui.html - generated by swagger: swagger API page that provides this documentation and a live UI for      submitting REST requests  * /status - provides the operational status of the service  * /api    - is the authenticated and authorized Data Repository API  * /ga4gh/drs/v1 - is a transcription of the Data Repository Service API  The overall API (/api) currently supports two interfaces:  * Repository - a general and default interface for initial setup, managing ingest and repository metadata  * Resource - an interface for managing billing accounts and resources  The API endpoints are organized by interface. Each interface is separately versioned. ## Notes on Naming All of the reference items are suffixed with \"Model\". Those names are used as the class names in the generated Java code. It is helpful to distinguish these model classes from other related classes, like the DAO classes and the operation classes. ## Editing and debugging I have found it best to edit this file directly to make changes and then use the swagger-editor to validate. The errors out of swagger-codegen are not that helpful. In the swagger-editor, it gives you nice errors and links to the place in the YAML where the errors are. But... the swagger-editor has been a bit of a pain for me to run. I tried the online website and was not able to load my YAML. Instead, I run it locally in a docker container, like this: ``` docker pull swaggerapi/swagger-editor docker run -p 9090:8080 swaggerapi/swagger-editor ``` Then navigate to localhost:9090 in your browser. I have not been able to get the file upload to work. It is a bit of a PITA, but I copy-paste the source code, replacing what is in the editor. Then make any fixes. Then copy-paste the resulting, valid file back into our source code. Not elegant, but easier than playing detective with the swagger-codegen errors. This might be something about my browser or environment, so give it a try yourself and see how it goes. ## Merging the DRS standard swagger into this swagger ## The merging is done in three sections:  1. Merging the security definitions into our security definitions  2. This section of paths. We make all paths explicit (prefixed with /ga4gh/drs/v1)     All standard DRS definitions and parameters are prefixed with 'DRS' to separate them     from our native definitions and parameters. We remove the x-swagger-router-controller lines.  3. A separate part of the definitions section for the DRS definitions  NOTE: the code here does not relect the DRS spec anymore. See DR-409.   # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from data_repo_client.configuration import Configuration


class AccessInfoBigQueryModelTable(object):
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
    """
    openapi_types = {
        'name': 'str',
        'id': 'str',
        'qualified_name': 'str',
        'link': 'str',
        'sample_query': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'qualified_name': 'qualifiedName',
        'link': 'link',
        'sample_query': 'sampleQuery'
    }

    def __init__(self, name=None, id=None, qualified_name=None, link=None, sample_query=None, local_vars_configuration=None):  # noqa: E501
        """AccessInfoBigQueryModelTable - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._id = None
        self._qualified_name = None
        self._link = None
        self._sample_query = None
        self.discriminator = None

        self.name = name
        self.id = id
        self.qualified_name = qualified_name
        if link is not None:
            self.link = link
        self.sample_query = sample_query

    @property
    def name(self):
        """Gets the name of this AccessInfoBigQueryModelTable.  # noqa: E501

        The name of the BigQuery table   # noqa: E501

        :return: The name of this AccessInfoBigQueryModelTable.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccessInfoBigQueryModelTable.

        The name of the BigQuery table   # noqa: E501

        :param name: The name of this AccessInfoBigQueryModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this AccessInfoBigQueryModelTable.  # noqa: E501

        The unique id of the BigQuery table   # noqa: E501

        :return: The id of this AccessInfoBigQueryModelTable.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessInfoBigQueryModelTable.

        The unique id of the BigQuery table   # noqa: E501

        :param id: The id of this AccessInfoBigQueryModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def qualified_name(self):
        """Gets the qualified_name of this AccessInfoBigQueryModelTable.  # noqa: E501

        The fully qualified name of the BigQuery table   # noqa: E501

        :return: The qualified_name of this AccessInfoBigQueryModelTable.  # noqa: E501
        :rtype: str
        """
        return self._qualified_name

    @qualified_name.setter
    def qualified_name(self, qualified_name):
        """Sets the qualified_name of this AccessInfoBigQueryModelTable.

        The fully qualified name of the BigQuery table   # noqa: E501

        :param qualified_name: The qualified_name of this AccessInfoBigQueryModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and qualified_name is None:  # noqa: E501
            raise ValueError("Invalid value for `qualified_name`, must not be `None`")  # noqa: E501

        self._qualified_name = qualified_name

    @property
    def link(self):
        """Gets the link of this AccessInfoBigQueryModelTable.  # noqa: E501

        The link to access the BigQuery table UI in Google Cloud console   # noqa: E501

        :return: The link of this AccessInfoBigQueryModelTable.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this AccessInfoBigQueryModelTable.

        The link to access the BigQuery table UI in Google Cloud console   # noqa: E501

        :param link: The link of this AccessInfoBigQueryModelTable.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def sample_query(self):
        """Gets the sample_query of this AccessInfoBigQueryModelTable.  # noqa: E501

        An example query that can be used to select data from this table   # noqa: E501

        :return: The sample_query of this AccessInfoBigQueryModelTable.  # noqa: E501
        :rtype: str
        """
        return self._sample_query

    @sample_query.setter
    def sample_query(self, sample_query):
        """Sets the sample_query of this AccessInfoBigQueryModelTable.

        An example query that can be used to select data from this table   # noqa: E501

        :param sample_query: The sample_query of this AccessInfoBigQueryModelTable.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and sample_query is None:  # noqa: E501
            raise ValueError("Invalid value for `sample_query`, must not be `None`")  # noqa: E501

        self._sample_query = sample_query

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
        if not isinstance(other, AccessInfoBigQueryModelTable):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccessInfoBigQueryModelTable):
            return True

        return self.to_dict() != other.to_dict()

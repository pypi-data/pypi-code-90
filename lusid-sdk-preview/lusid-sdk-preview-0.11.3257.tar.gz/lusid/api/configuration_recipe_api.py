# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3257
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from lusid.api_client import ApiClient
from lusid.exceptions import (
    ApiTypeError,
    ApiValueError
)


class ConfigurationRecipeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_configuration_recipe(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Delete a Configuration Recipe, assuming that it is present.  # noqa: E501

        Delete the specified Configuration Recipe from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_configuration_recipe(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the Configuration Recipe to delete. (required)
        :param str code: The Configuration Recipe to delete. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AnnulSingleStructuredDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_configuration_recipe_with_http_info(scope, code, **kwargs)  # noqa: E501

    def delete_configuration_recipe_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Delete a Configuration Recipe, assuming that it is present.  # noqa: E501

        Delete the specified Configuration Recipe from a single scope.                The response will return either detail of the deleted item, or an explanation (failure) as to why this did not succeed.                It is important to always check for any unsuccessful response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_configuration_recipe_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the Configuration Recipe to delete. (required)
        :param str code: The Configuration Recipe to delete. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AnnulSingleStructuredDataResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_configuration_recipe" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `delete_configuration_recipe`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `delete_configuration_recipe`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_configuration_recipe`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_configuration_recipe`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `delete_configuration_recipe`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_configuration_recipe`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_configuration_recipe`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `delete_configuration_recipe`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3257'

        return self.api_client.call_api(
            '/api/recipes/{scope}/{code}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnnulSingleStructuredDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_configuration_recipe(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Get Configuration Recipe  # noqa: E501

        Get a Configuration Recipe from a single scope.                The response will return either the recipe that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration_recipe(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the Configuration Recipe to retrieve. (required)
        :param str code: The name of the recipe to retrieve the data for. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetRecipeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_configuration_recipe_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_configuration_recipe_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Get Configuration Recipe  # noqa: E501

        Get a Configuration Recipe from a single scope.                The response will return either the recipe that has been stored, or a failure explaining why the request was unsuccessful.                It is important to always check for any unsuccessful requests (failures).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_configuration_recipe_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the Configuration Recipe to retrieve. (required)
        :param str code: The name of the recipe to retrieve the data for. (required)
        :param datetime as_at: The asAt datetime at which to retrieve the Configuration Recipe. Defaults to return the latest version if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetRecipeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'as_at']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_configuration_recipe" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'scope' is set
        if ('scope' not in local_var_params or
                local_var_params['scope'] is None):
            raise ApiValueError("Missing the required parameter `scope` when calling `get_configuration_recipe`")  # noqa: E501
        # verify the required parameter 'code' is set
        if ('code' not in local_var_params or
                local_var_params['code'] is None):
            raise ApiValueError("Missing the required parameter `code` when calling `get_configuration_recipe`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_configuration_recipe`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_configuration_recipe`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_configuration_recipe`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_configuration_recipe`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_configuration_recipe`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_configuration_recipe`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3257'

        return self.api_client.call_api(
            '/api/recipes/{scope}/{code}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetRecipeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_configuration_recipes(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] List the set of Configuration Recipes  # noqa: E501

        List the set of configuration recipes at the specified date/time and scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_configuration_recipes(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime as_at: The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified.
        :param str filter: Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfGetRecipeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_configuration_recipes_with_http_info(**kwargs)  # noqa: E501

    def list_configuration_recipes_with_http_info(self, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] List the set of Configuration Recipes  # noqa: E501

        List the set of configuration recipes at the specified date/time and scope  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_configuration_recipes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param datetime as_at: The asAt datetime at which to list the Configuration Recipes. Defaults to latest if not specified.
        :param str filter: Expression to filter the result set. Read more about filtering results from LUSID here:              https://support.lusid.com/filtering-results-from-lusid.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfGetRecipeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['as_at', 'filter']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_configuration_recipes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('filter' in local_var_params and
                len(local_var_params['filter']) > 2147483647):
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_configuration_recipes`, length must be less than or equal to `2147483647`")  # noqa: E501
        if ('filter' in local_var_params and
                len(local_var_params['filter']) < 0):
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_configuration_recipes`, length must be greater than or equal to `0`")  # noqa: E501
        if 'filter' in local_var_params and not re.search(r'^[\s\S]*$', local_var_params['filter']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `filter` when calling `list_configuration_recipes`, must conform to the pattern `/^[\s\S]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'filter' in local_var_params:
            query_params.append(('filter', local_var_params['filter']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501


        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3257'

        return self.api_client.call_api(
            '/api/recipes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfGetRecipeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_configuration_recipe(self, upsert_recipe_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Upsert a Configuration Recipe. This creates or updates the data in Lusid.  # noqa: E501

        Update or insert one Configuration Recipe in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Configuration Recipe or failure message if unsuccessful                It is important to always check to verify success (or failure).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_configuration_recipe(upsert_recipe_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UpsertRecipeRequest upsert_recipe_request: The Configuration Recipe to update or insert (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpsertSingleStructuredDataResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_configuration_recipe_with_http_info(upsert_recipe_request, **kwargs)  # noqa: E501

    def upsert_configuration_recipe_with_http_info(self, upsert_recipe_request, **kwargs):  # noqa: E501
        """[EXPERIMENTAL] Upsert a Configuration Recipe. This creates or updates the data in Lusid.  # noqa: E501

        Update or insert one Configuration Recipe in a single scope. An item will be updated if it already exists  and inserted if it does not.                The response will return the successfully updated or inserted Configuration Recipe or failure message if unsuccessful                It is important to always check to verify success (or failure).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_configuration_recipe_with_http_info(upsert_recipe_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param UpsertRecipeRequest upsert_recipe_request: The Configuration Recipe to update or insert (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpsertSingleStructuredDataResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['upsert_recipe_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_configuration_recipe" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'upsert_recipe_request' is set
        if ('upsert_recipe_request' not in local_var_params or
                local_var_params['upsert_recipe_request'] is None):
            raise ApiValueError("Missing the required parameter `upsert_recipe_request` when calling `upsert_configuration_recipe`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'upsert_recipe_request' in local_var_params:
            body_params = local_var_params['upsert_recipe_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json-patch+json', 'application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth2']  # noqa: E501

        # set the LUSID header
        header_params['X-LUSID-SDK-Language'] = 'Python'
        header_params['X-LUSID-SDK-Version'] = '0.11.3257'

        return self.api_client.call_api(
            '/api/recipes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpsertSingleStructuredDataResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

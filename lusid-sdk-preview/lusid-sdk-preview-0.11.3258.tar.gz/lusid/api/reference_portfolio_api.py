# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.11.3258
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


class ReferencePortfolioApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_reference_portfolio(self, scope, create_reference_portfolio_request, **kwargs):  # noqa: E501
        """Create reference portfolio  # noqa: E501

        Create a reference portfolio in a particular scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_reference_portfolio(scope, create_reference_portfolio_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope in which to create the reference portfolio. (required)
        :param CreateReferencePortfolioRequest create_reference_portfolio_request: The definition of the reference portfolio. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Portfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_reference_portfolio_with_http_info(scope, create_reference_portfolio_request, **kwargs)  # noqa: E501

    def create_reference_portfolio_with_http_info(self, scope, create_reference_portfolio_request, **kwargs):  # noqa: E501
        """Create reference portfolio  # noqa: E501

        Create a reference portfolio in a particular scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_reference_portfolio_with_http_info(scope, create_reference_portfolio_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope in which to create the reference portfolio. (required)
        :param CreateReferencePortfolioRequest create_reference_portfolio_request: The definition of the reference portfolio. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Portfolio, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'create_reference_portfolio_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_reference_portfolio" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_reference_portfolio_request' is set
        if ('create_reference_portfolio_request' not in local_var_params or
                local_var_params['create_reference_portfolio_request'] is None):
            raise ApiValueError("Missing the required parameter `create_reference_portfolio_request` when calling `create_reference_portfolio`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_reference_portfolio_request' in local_var_params:
            body_params = local_var_params['create_reference_portfolio_request']
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
        header_params['X-LUSID-SDK-Version'] = '0.11.3258'

        return self.api_client.call_api(
            '/api/referenceportfolios/{scope}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Portfolio',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_reference_portfolio_constituents(self, scope, code, **kwargs):  # noqa: E501
        """Get reference portfolio constituents  # noqa: E501

        Get constituents from a reference portfolio at a particular effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_portfolio_constituents(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param str effective_at: The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified.
        :param list[str] property_keys: A list of property keys from the 'Instrument' or 'ReferenceHolding' domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or              'ReferenceHolding/strategy/quantsignal'. Defaults to return all available instrument and reference holding properties if not specified.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetReferencePortfolioConstituentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_reference_portfolio_constituents_with_http_info(scope, code, **kwargs)  # noqa: E501

    def get_reference_portfolio_constituents_with_http_info(self, scope, code, **kwargs):  # noqa: E501
        """Get reference portfolio constituents  # noqa: E501

        Get constituents from a reference portfolio at a particular effective time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_reference_portfolio_constituents_with_http_info(scope, code, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param str effective_at: The effective date of the constituents to retrieve. Defaults to the current LUSID system datetime if not specified.
        :param datetime as_at: The asAt datetime at which to retrieve constituents. Defaults to return the latest version              of each constituent if not specified.
        :param list[str] property_keys: A list of property keys from the 'Instrument' or 'ReferenceHolding' domain to decorate onto              constituents. These take the format {domain}/{scope}/{code} e.g. 'Instrument/system/Name' or              'ReferenceHolding/strategy/quantsignal'. Defaults to return all available instrument and reference holding properties if not specified.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetReferencePortfolioConstituentsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'effective_at', 'as_at', 'property_keys']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_reference_portfolio_constituents" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_reference_portfolio_constituents`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_reference_portfolio_constituents`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `get_reference_portfolio_constituents`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_reference_portfolio_constituents`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `get_reference_portfolio_constituents`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `get_reference_portfolio_constituents`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'effective_at' in local_var_params:
            query_params.append(('effectiveAt', local_var_params['effective_at']))  # noqa: E501
        if 'as_at' in local_var_params:
            query_params.append(('asAt', local_var_params['as_at']))  # noqa: E501
        if 'property_keys' in local_var_params:
            query_params.append(('propertyKeys', local_var_params['property_keys']))  # noqa: E501
            collection_formats['propertyKeys'] = 'multi'  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '0.11.3258'

        return self.api_client.call_api(
            '/api/referenceportfolios/{scope}/{code}/constituents', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetReferencePortfolioConstituentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_constituents_adjustments(self, scope, code, from_effective_at, to_effective_at, **kwargs):  # noqa: E501
        """List constituents adjustments  # noqa: E501

        List adjustments made to constituents in a reference portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_constituents_adjustments(scope, code, from_effective_at, to_effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param str from_effective_at: Events between this time (inclusive) and the toEffectiveAt are returned. (required)
        :param str to_effective_at: Events between this time (inclusive) and the fromEffectiveAt are returned. (required)
        :param datetime as_at_time: The asAt time for which the result is valid.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ResourceListOfConstituentsAdjustmentHeader
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_constituents_adjustments_with_http_info(scope, code, from_effective_at, to_effective_at, **kwargs)  # noqa: E501

    def list_constituents_adjustments_with_http_info(self, scope, code, from_effective_at, to_effective_at, **kwargs):  # noqa: E501
        """List constituents adjustments  # noqa: E501

        List adjustments made to constituents in a reference portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_constituents_adjustments_with_http_info(scope, code, from_effective_at, to_effective_at, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param str from_effective_at: Events between this time (inclusive) and the toEffectiveAt are returned. (required)
        :param str to_effective_at: Events between this time (inclusive) and the fromEffectiveAt are returned. (required)
        :param datetime as_at_time: The asAt time for which the result is valid.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ResourceListOfConstituentsAdjustmentHeader, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'from_effective_at', 'to_effective_at', 'as_at_time']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_constituents_adjustments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'from_effective_at' is set
        if ('from_effective_at' not in local_var_params or
                local_var_params['from_effective_at'] is None):
            raise ApiValueError("Missing the required parameter `from_effective_at` when calling `list_constituents_adjustments`")  # noqa: E501
        # verify the required parameter 'to_effective_at' is set
        if ('to_effective_at' not in local_var_params or
                local_var_params['to_effective_at'] is None):
            raise ApiValueError("Missing the required parameter `to_effective_at` when calling `list_constituents_adjustments`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_constituents_adjustments`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_constituents_adjustments`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `list_constituents_adjustments`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `list_constituents_adjustments`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `list_constituents_adjustments`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `list_constituents_adjustments`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'scope' in local_var_params:
            path_params['scope'] = local_var_params['scope']  # noqa: E501
        if 'code' in local_var_params:
            path_params['code'] = local_var_params['code']  # noqa: E501

        query_params = []
        if 'from_effective_at' in local_var_params:
            query_params.append(('fromEffectiveAt', local_var_params['from_effective_at']))  # noqa: E501
        if 'to_effective_at' in local_var_params:
            query_params.append(('toEffectiveAt', local_var_params['to_effective_at']))  # noqa: E501
        if 'as_at_time' in local_var_params:
            query_params.append(('asAtTime', local_var_params['as_at_time']))  # noqa: E501

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
        header_params['X-LUSID-SDK-Version'] = '0.11.3258'

        return self.api_client.call_api(
            '/api/referenceportfolios/{scope}/{code}/constituentsadjustments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResourceListOfConstituentsAdjustmentHeader',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_reference_portfolio_constituents(self, scope, code, upsert_reference_portfolio_constituents_request, **kwargs):  # noqa: E501
        """Upsert reference portfolio constituents  # noqa: E501

        Add constituents to a reference portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_reference_portfolio_constituents(scope, code, upsert_reference_portfolio_constituents_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param UpsertReferencePortfolioConstituentsRequest upsert_reference_portfolio_constituents_request: The constituents to upload to the reference portfolio. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: UpsertReferencePortfolioConstituentsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.upsert_reference_portfolio_constituents_with_http_info(scope, code, upsert_reference_portfolio_constituents_request, **kwargs)  # noqa: E501

    def upsert_reference_portfolio_constituents_with_http_info(self, scope, code, upsert_reference_portfolio_constituents_request, **kwargs):  # noqa: E501
        """Upsert reference portfolio constituents  # noqa: E501

        Add constituents to a reference portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_reference_portfolio_constituents_with_http_info(scope, code, upsert_reference_portfolio_constituents_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str scope: The scope of the reference portfolio. (required)
        :param str code: The code of the reference portfolio. Together with the scope this uniquely identifies              the reference portfolio. (required)
        :param UpsertReferencePortfolioConstituentsRequest upsert_reference_portfolio_constituents_request: The constituents to upload to the reference portfolio. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(UpsertReferencePortfolioConstituentsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['scope', 'code', 'upsert_reference_portfolio_constituents_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_reference_portfolio_constituents" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'upsert_reference_portfolio_constituents_request' is set
        if ('upsert_reference_portfolio_constituents_request' not in local_var_params or
                local_var_params['upsert_reference_portfolio_constituents_request'] is None):
            raise ApiValueError("Missing the required parameter `upsert_reference_portfolio_constituents_request` when calling `upsert_reference_portfolio_constituents`")  # noqa: E501

        if ('scope' in local_var_params and
                len(local_var_params['scope']) > 64):
            raise ApiValueError("Invalid value for parameter `scope` when calling `upsert_reference_portfolio_constituents`, length must be less than or equal to `64`")  # noqa: E501
        if ('scope' in local_var_params and
                len(local_var_params['scope']) < 1):
            raise ApiValueError("Invalid value for parameter `scope` when calling `upsert_reference_portfolio_constituents`, length must be greater than or equal to `1`")  # noqa: E501
        if 'scope' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['scope']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `scope` when calling `upsert_reference_portfolio_constituents`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) > 64):
            raise ApiValueError("Invalid value for parameter `code` when calling `upsert_reference_portfolio_constituents`, length must be less than or equal to `64`")  # noqa: E501
        if ('code' in local_var_params and
                len(local_var_params['code']) < 1):
            raise ApiValueError("Invalid value for parameter `code` when calling `upsert_reference_portfolio_constituents`, length must be greater than or equal to `1`")  # noqa: E501
        if 'code' in local_var_params and not re.search(r'^[a-zA-Z0-9\-_]+$', local_var_params['code']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `code` when calling `upsert_reference_portfolio_constituents`, must conform to the pattern `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501
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
        if 'upsert_reference_portfolio_constituents_request' in local_var_params:
            body_params = local_var_params['upsert_reference_portfolio_constituents_request']
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
        header_params['X-LUSID-SDK-Version'] = '0.11.3258'

        return self.api_client.call_api(
            '/api/referenceportfolios/{scope}/{code}/constituents', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UpsertReferencePortfolioConstituentsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

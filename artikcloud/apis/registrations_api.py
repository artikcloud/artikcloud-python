# coding: utf-8

"""
    ARTIK Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RegistrationsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def confirm_user(self, registration_info, **kwargs):
        """
        Confirm User
        This call updates the registration request issued earlier by associating it with an authenticated user and captures all additional information required to add a new device.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.confirm_user(registration_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeviceRegConfirmUserRequest registration_info: Device Registration information. (required)
        :return: DeviceRegConfirmUserResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.confirm_user_with_http_info(registration_info, **kwargs)
        else:
            (data) = self.confirm_user_with_http_info(registration_info, **kwargs)
            return data

    def confirm_user_with_http_info(self, registration_info, **kwargs):
        """
        Confirm User
        This call updates the registration request issued earlier by associating it with an authenticated user and captures all additional information required to add a new device.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.confirm_user_with_http_info(registration_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param DeviceRegConfirmUserRequest registration_info: Device Registration information. (required)
        :return: DeviceRegConfirmUserResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registration_info']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registration_info' is set
        if ('registration_info' not in params) or (params['registration_info'] is None):
            raise ValueError("Missing the required parameter `registration_info` when calling `confirm_user`")


        collection_formats = {}

        resource_path = '/devices/registrations/pin'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'registration_info' in params:
            body_params = params['registration_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceRegConfirmUserResponseEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_request_status_for_user(self, request_id, **kwargs):
        """
        Get Request Status For User
        This call checks the status of the request so users can poll and know when registration is complete.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_request_status_for_user(request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str request_id: Request ID. (required)
        :return: DeviceRegStatusResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_request_status_for_user_with_http_info(request_id, **kwargs)
        else:
            (data) = self.get_request_status_for_user_with_http_info(request_id, **kwargs)
            return data

    def get_request_status_for_user_with_http_info(self, request_id, **kwargs):
        """
        Get Request Status For User
        This call checks the status of the request so users can poll and know when registration is complete.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_request_status_for_user_with_http_info(request_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str request_id: Request ID. (required)
        :return: DeviceRegStatusResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_request_status_for_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request_id' is set
        if ('request_id' not in params) or (params['request_id'] is None):
            raise ValueError("Missing the required parameter `request_id` when calling `get_request_status_for_user`")


        collection_formats = {}

        resource_path = '/devices/registrations/{requestId}/status'.replace('{format}', 'json')
        path_params = {}
        if 'request_id' in params:
            path_params['requestId'] = params['request_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='DeviceRegStatusResponseEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def unregister_device(self, device_id, **kwargs):
        """
        Unregister Device
        This call clears any associations from the secure device registration.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unregister_device(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :return: UnregisterDeviceResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.unregister_device_with_http_info(device_id, **kwargs)
        else:
            (data) = self.unregister_device_with_http_info(device_id, **kwargs)
            return data

    def unregister_device_with_http_info(self, device_id, **kwargs):
        """
        Unregister Device
        This call clears any associations from the secure device registration.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.unregister_device_with_http_info(device_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str device_id: Device ID. (required)
        :return: UnregisterDeviceResponseEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['device_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unregister_device" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'device_id' is set
        if ('device_id' not in params) or (params['device_id'] is None):
            raise ValueError("Missing the required parameter `device_id` when calling `unregister_device`")


        collection_formats = {}

        resource_path = '/devices/{deviceId}/registrations'.replace('{format}', 'json')
        path_params = {}
        if 'device_id' in params:
            path_params['deviceId'] = params['device_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='UnregisterDeviceResponseEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

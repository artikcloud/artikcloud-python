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


class SubscriptionsApi(object):
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

    def create_subscription(self, subscription_info, **kwargs):
        """
        Create Subscription
        Create Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription(subscription_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SubscriptionInfo subscription_info: Subscription details (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_subscription_with_http_info(subscription_info, **kwargs)
        else:
            (data) = self.create_subscription_with_http_info(subscription_info, **kwargs)
            return data

    def create_subscription_with_http_info(self, subscription_info, **kwargs):
        """
        Create Subscription
        Create Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_subscription_with_http_info(subscription_info, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param SubscriptionInfo subscription_info: Subscription details (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['subscription_info']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'subscription_info' is set
        if ('subscription_info' not in params) or (params['subscription_info'] is None):
            raise ValueError("Missing the required parameter `subscription_info` when calling `create_subscription`")


        collection_formats = {}

        resource_path = '/subscriptions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription_info' in params:
            body_params = params['subscription_info']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubscriptionEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_subscription(self, sub_id, **kwargs):
        """
        Delete Subscription
        Delete Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription(sub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_subscription_with_http_info(sub_id, **kwargs)
        else:
            (data) = self.delete_subscription_with_http_info(sub_id, **kwargs)
            return data

    def delete_subscription_with_http_info(self, sub_id, **kwargs):
        """
        Delete Subscription
        Delete Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_subscription_with_http_info(sub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sub_id' is set
        if ('sub_id' not in params) or (params['sub_id'] is None):
            raise ValueError("Missing the required parameter `sub_id` when calling `delete_subscription`")


        collection_formats = {}

        resource_path = '/subscriptions/{subId}'.replace('{format}', 'json')
        path_params = {}
        if 'sub_id' in params:
            path_params['subId'] = params['sub_id']

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
                                        response_type='SubscriptionEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_all_subscriptions(self, **kwargs):
        """
        Get All Subscriptions
        Get All Subscriptions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uid: User ID
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set.
        :return: SubscriptionsEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_subscriptions_with_http_info(**kwargs)
        else:
            (data) = self.get_all_subscriptions_with_http_info(**kwargs)
            return data

    def get_all_subscriptions_with_http_info(self, **kwargs):
        """
        Get All Subscriptions
        Get All Subscriptions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_subscriptions_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str uid: User ID
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set.
        :return: SubscriptionsEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'offset', 'count']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_subscriptions" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        resource_path = '/subscriptions'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'uid' in params:
            query_params['uid'] = params['uid']
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'count' in params:
            query_params['count'] = params['count']

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
                                        response_type='SubscriptionsEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_messages(self, notif_id, **kwargs):
        """
        Get Messages
        Get Messages
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_messages(notif_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str notif_id: Notification ID. (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set.
        :param str order: Sort order of results by ts. Either 'asc' or 'desc'.
        :return: NotifMessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_messages_with_http_info(notif_id, **kwargs)
        else:
            (data) = self.get_messages_with_http_info(notif_id, **kwargs)
            return data

    def get_messages_with_http_info(self, notif_id, **kwargs):
        """
        Get Messages
        Get Messages
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_messages_with_http_info(notif_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str notif_id: Notification ID. (required)
        :param int offset: Offset for pagination.
        :param int count: Desired count of items in the result set.
        :param str order: Sort order of results by ts. Either 'asc' or 'desc'.
        :return: NotifMessagesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['notif_id', 'offset', 'count', 'order']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'notif_id' is set
        if ('notif_id' not in params) or (params['notif_id'] is None):
            raise ValueError("Missing the required parameter `notif_id` when calling `get_messages`")


        collection_formats = {}

        resource_path = '/notifications/{notifId}/messages'.replace('{format}', 'json')
        path_params = {}
        if 'notif_id' in params:
            path_params['notifId'] = params['notif_id']

        query_params = {}
        if 'offset' in params:
            query_params['offset'] = params['offset']
        if 'count' in params:
            query_params['count'] = params['count']
        if 'order' in params:
            query_params['order'] = params['order']

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
                                        response_type='NotifMessagesResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_subscription(self, sub_id, **kwargs):
        """
        Get Subscription
        Get Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription(sub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_subscription_with_http_info(sub_id, **kwargs)
        else:
            (data) = self.get_subscription_with_http_info(sub_id, **kwargs)
            return data

    def get_subscription_with_http_info(self, sub_id, **kwargs):
        """
        Get Subscription
        Get Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_subscription_with_http_info(sub_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sub_id' is set
        if ('sub_id' not in params) or (params['sub_id'] is None):
            raise ValueError("Missing the required parameter `sub_id` when calling `get_subscription`")


        collection_formats = {}

        resource_path = '/subscriptions/{subId}'.replace('{format}', 'json')
        path_params = {}
        if 'sub_id' in params:
            path_params['subId'] = params['sub_id']

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
                                        response_type='SubscriptionEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def validate_subscription(self, sub_id, validation_callback_request, **kwargs):
        """
        Validate Subscription
        Validate Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_subscription(sub_id, validation_callback_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :param ValidationCallbackInfo validation_callback_request: Subscription validation callback request (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.validate_subscription_with_http_info(sub_id, validation_callback_request, **kwargs)
        else:
            (data) = self.validate_subscription_with_http_info(sub_id, validation_callback_request, **kwargs)
            return data

    def validate_subscription_with_http_info(self, sub_id, validation_callback_request, **kwargs):
        """
        Validate Subscription
        Validate Subscription
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.validate_subscription_with_http_info(sub_id, validation_callback_request, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str sub_id: Subscription ID. (required)
        :param ValidationCallbackInfo validation_callback_request: Subscription validation callback request (required)
        :return: SubscriptionEnvelope
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sub_id', 'validation_callback_request']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method validate_subscription" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sub_id' is set
        if ('sub_id' not in params) or (params['sub_id'] is None):
            raise ValueError("Missing the required parameter `sub_id` when calling `validate_subscription`")
        # verify the required parameter 'validation_callback_request' is set
        if ('validation_callback_request' not in params) or (params['validation_callback_request'] is None):
            raise ValueError("Missing the required parameter `validation_callback_request` when calling `validate_subscription`")


        collection_formats = {}

        resource_path = '/subscriptions/{subId}/validate'.replace('{format}', 'json')
        path_params = {}
        if 'sub_id' in params:
            path_params['subId'] = params['sub_id']

        query_params = {}

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'validation_callback_request' in params:
            body_params = params['validation_callback_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['artikcloud_oauth']

        return self.api_client.call_api(resource_path, 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SubscriptionEnvelope',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

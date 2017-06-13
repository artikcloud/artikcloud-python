# artikcloud.SubscriptionsApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscription**](SubscriptionsApi.md#create_subscription) | **POST** /subscriptions | Create Subscription
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /subscriptions/{subId} | Delete Subscription
[**get_all_subscriptions**](SubscriptionsApi.md#get_all_subscriptions) | **GET** /subscriptions | Get All Subscriptions
[**get_messages**](SubscriptionsApi.md#get_messages) | **GET** /notifications/{notifId}/messages | Get Messages
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subId} | Get Subscription
[**validate_subscription**](SubscriptionsApi.md#validate_subscription) | **POST** /subscriptions/{subId}/validate | Validate Subscription


# **create_subscription**
> SubscriptionEnvelope create_subscription(subscription_info)

Create Subscription

Create Subscription

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
subscription_info = artikcloud.SubscriptionInfo() # SubscriptionInfo | Subscription details

try: 
    # Create Subscription
    api_response = api_instance.create_subscription(subscription_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_info** | [**SubscriptionInfo**](SubscriptionInfo.md)| Subscription details | 

### Return type

[**SubscriptionEnvelope**](SubscriptionEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> SubscriptionEnvelope delete_subscription(sub_id)

Delete Subscription

Delete Subscription

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
sub_id = 'sub_id_example' # str | Subscription ID.

try: 
    # Delete Subscription
    api_response = api_instance.delete_subscription(sub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| Subscription ID. | 

### Return type

[**SubscriptionEnvelope**](SubscriptionEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_subscriptions**
> SubscriptionsEnvelope get_all_subscriptions(uid=uid, offset=offset, count=count)

Get All Subscriptions

Get All Subscriptions

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
uid = 'uid_example' # str | User ID (optional)
offset = 56 # int | Offset for pagination. (optional)
count = 56 # int | Desired count of items in the result set. (optional)

try: 
    # Get All Subscriptions
    api_response = api_instance.get_all_subscriptions(uid=uid, offset=offset, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_all_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| User ID | [optional] 
 **offset** | **int**| Offset for pagination. | [optional] 
 **count** | **int**| Desired count of items in the result set. | [optional] 

### Return type

[**SubscriptionsEnvelope**](SubscriptionsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_messages**
> NotifMessagesResponse get_messages(notif_id, offset=offset, count=count, order=order)

Get Messages

Get Messages

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
notif_id = 'notif_id_example' # str | Notification ID.
offset = 56 # int | Offset for pagination. (optional)
count = 56 # int | Desired count of items in the result set. (optional)
order = 'order_example' # str | Sort order of results by ts. Either 'asc' or 'desc'. (optional)

try: 
    # Get Messages
    api_response = api_instance.get_messages(notif_id, offset=offset, count=count, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notif_id** | **str**| Notification ID. | 
 **offset** | **int**| Offset for pagination. | [optional] 
 **count** | **int**| Desired count of items in the result set. | [optional] 
 **order** | **str**| Sort order of results by ts. Either &#39;asc&#39; or &#39;desc&#39;. | [optional] 

### Return type

[**NotifMessagesResponse**](NotifMessagesResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> SubscriptionEnvelope get_subscription(sub_id)

Get Subscription

Get Subscription

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
sub_id = 'sub_id_example' # str | Subscription ID.

try: 
    # Get Subscription
    api_response = api_instance.get_subscription(sub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| Subscription ID. | 

### Return type

[**SubscriptionEnvelope**](SubscriptionEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_subscription**
> SubscriptionEnvelope validate_subscription(sub_id, validation_callback_request)

Validate Subscription

Validate Subscription

### Example 
```python
from __future__ import print_statement
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.SubscriptionsApi()
sub_id = 'sub_id_example' # str | Subscription ID.
validation_callback_request = artikcloud.ValidationCallbackInfo() # ValidationCallbackInfo | Subscription validation callback request

try: 
    # Validate Subscription
    api_response = api_instance.validate_subscription(sub_id, validation_callback_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->validate_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| Subscription ID. | 
 **validation_callback_request** | [**ValidationCallbackInfo**](ValidationCallbackInfo.md)| Subscription validation callback request | 

### Return type

[**SubscriptionEnvelope**](SubscriptionEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


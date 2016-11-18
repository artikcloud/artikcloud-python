# artikcloud.UsersApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_properties**](UsersApi.md#create_user_properties) | **POST** /users/{userId}/properties | Create User Application Properties
[**delete_user_properties**](UsersApi.md#delete_user_properties) | **DELETE** /users/{userId}/properties | Delete User Application Properties
[**get_self**](UsersApi.md#get_self) | **GET** /users/self | Get Current User Profile
[**get_user_device_types**](UsersApi.md#get_user_device_types) | **GET** /users/{userId}/devicetypes | Get User Device Types
[**get_user_devices**](UsersApi.md#get_user_devices) | **GET** /users/{userId}/devices | Get User Devices
[**get_user_properties**](UsersApi.md#get_user_properties) | **GET** /users/{userId}/properties | Get User application properties
[**get_user_rules**](UsersApi.md#get_user_rules) | **GET** /users/{userId}/rules | Get User Rules
[**update_user_properties**](UsersApi.md#update_user_properties) | **PUT** /users/{userId}/properties | Update User Application Properties


# **create_user_properties**
> PropertiesEnvelope create_user_properties(user_id, properties, aid=aid)

Create User Application Properties

Create application properties for a user

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User Id
properties = artikcloud.AppProperties() # AppProperties | Properties to be updated
aid = 'aid_example' # str | Application ID (optional)

try: 
    # Create User Application Properties
    api_response = api_instance.create_user_properties(user_id, properties, aid=aid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->create_user_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **properties** | [**AppProperties**](AppProperties.md)| Properties to be updated | 
 **aid** | **str**| Application ID | [optional] 

### Return type

[**PropertiesEnvelope**](PropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_properties**
> PropertiesEnvelope delete_user_properties(user_id, aid=aid)

Delete User Application Properties

Deletes a user's application properties

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User Id
aid = 'aid_example' # str | Application ID (optional)

try: 
    # Delete User Application Properties
    api_response = api_instance.delete_user_properties(user_id, aid=aid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->delete_user_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **aid** | **str**| Application ID | [optional] 

### Return type

[**PropertiesEnvelope**](PropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self**
> UserEnvelope get_self()

Get Current User Profile

Get's the current user's profile

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()

try: 
    # Get Current User Profile
    api_response = api_instance.get_self()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_self: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserEnvelope**](UserEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_device_types**
> DeviceTypesEnvelope get_user_device_types(user_id, offset=offset, count=count, include_shared=include_shared)

Get User Device Types

Retrieve User's Device Types

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User ID.
offset = 56 # int | Offset for pagination. (optional)
count = 56 # int | Desired count of items in the result set (optional)
include_shared = true # bool | Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users. (optional)

try: 
    # Get User Device Types
    api_response = api_instance.get_user_device_types(user_id, offset=offset, count=count, include_shared=include_shared)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_device_types: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. | 
 **offset** | **int**| Offset for pagination. | [optional] 
 **count** | **int**| Desired count of items in the result set | [optional] 
 **include_shared** | **bool**| Optional. Boolean (true/false) - If false, only return the user&#39;s device types. If true, also return device types shared by other users. | [optional] 

### Return type

[**DeviceTypesEnvelope**](DeviceTypesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_devices**
> DevicesEnvelope get_user_devices(user_id, offset=offset, count=count, include_properties=include_properties)

Get User Devices

Retrieve User's Devices

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User ID
offset = 56 # int | Offset for pagination. (optional)
count = 56 # int | Desired count of items in the result set (optional)
include_properties = true # bool | Optional. Boolean (true/false) - If false, only return the user's device types. If true, also return device types shared by other users. (optional)

try: 
    # Get User Devices
    api_response = api_instance.get_user_devices(user_id, offset=offset, count=count, include_properties=include_properties)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_devices: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID | 
 **offset** | **int**| Offset for pagination. | [optional] 
 **count** | **int**| Desired count of items in the result set | [optional] 
 **include_properties** | **bool**| Optional. Boolean (true/false) - If false, only return the user&#39;s device types. If true, also return device types shared by other users. | [optional] 

### Return type

[**DevicesEnvelope**](DevicesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_properties**
> PropertiesEnvelope get_user_properties(user_id, aid=aid)

Get User application properties

Get application properties of a user

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User Id
aid = 'aid_example' # str | Application ID (optional)

try: 
    # Get User application properties
    api_response = api_instance.get_user_properties(user_id, aid=aid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **aid** | **str**| Application ID | [optional] 

### Return type

[**PropertiesEnvelope**](PropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_rules**
> RulesEnvelope get_user_rules(user_id, exclude_disabled=exclude_disabled, count=count, offset=offset)

Get User Rules

Retrieve User's Rules

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User ID.
exclude_disabled = true # bool | Exclude disabled rules in the result. (optional)
count = 56 # int | Desired count of items in the result set. (optional)
offset = 56 # int | Offset for pagination. (optional)

try: 
    # Get User Rules
    api_response = api_instance.get_user_rules(user_id, exclude_disabled=exclude_disabled, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->get_user_rules: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User ID. | 
 **exclude_disabled** | **bool**| Exclude disabled rules in the result. | [optional] 
 **count** | **int**| Desired count of items in the result set. | [optional] 
 **offset** | **int**| Offset for pagination. | [optional] 

### Return type

[**RulesEnvelope**](RulesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_properties**
> PropertiesEnvelope update_user_properties(user_id, properties, aid=aid)

Update User Application Properties

Updates application properties of a user

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.UsersApi()
user_id = 'user_id_example' # str | User Id
properties = artikcloud.AppProperties() # AppProperties | Properties to be updated
aid = 'aid_example' # str | Application ID (optional)

try: 
    # Update User Application Properties
    api_response = api_instance.update_user_properties(user_id, properties, aid=aid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling UsersApi->update_user_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User Id | 
 **properties** | [**AppProperties**](AppProperties.md)| Properties to be updated | 
 **aid** | **str**| Application ID | [optional] 

### Return type

[**PropertiesEnvelope**](PropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


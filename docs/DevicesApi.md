# artikcloud.DevicesApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_device**](DevicesApi.md#add_device) | **POST** /devices | Add Device
[**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{deviceId} | Delete Device
[**delete_device_token**](DevicesApi.md#delete_device_token) | **DELETE** /devices/{deviceId}/tokens | Delete Device Token
[**get_device**](DevicesApi.md#get_device) | **GET** /devices/{deviceId} | Get Device
[**get_device_presence**](DevicesApi.md#get_device_presence) | **GET** /devices/{deviceId}/presence | Get device presence information
[**get_device_token**](DevicesApi.md#get_device_token) | **GET** /devices/{deviceId}/tokens | Get Device Token
[**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{deviceId} | Update Device
[**update_device_token**](DevicesApi.md#update_device_token) | **PUT** /devices/{deviceId}/tokens | Update Device Token


# **add_device**
> DeviceEnvelope add_device(device)

Add Device

Create a device

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device = artikcloud.Device() # Device | Device to be added to the user

try: 
    # Add Device
    api_response = api_instance.add_device(device)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->add_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)| Device to be added to the user | 

### Return type

[**DeviceEnvelope**](DeviceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> DeviceEnvelope delete_device(device_id)

Delete Device

Deletes a device

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId

try: 
    # Delete Device
    api_response = api_instance.delete_device(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->delete_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceEnvelope**](DeviceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_token**
> DeviceTokenEnvelope delete_device_token(device_id)

Delete Device Token

Deletes a device's token

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId

try: 
    # Delete Device Token
    api_response = api_instance.delete_device_token(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->delete_device_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceTokenEnvelope**](DeviceTokenEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device**
> DeviceEnvelope get_device(device_id)

Get Device

Retrieves a device

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId

try: 
    # Get Device
    api_response = api_instance.get_device(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->get_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceEnvelope**](DeviceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_presence**
> PresenceEnvelope get_device_presence(device_id)

Get device presence information

Return the presence status of the given device along with the time it was last seen

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | Device ID.

try: 
    # Get device presence information
    api_response = api_instance.get_device_presence(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->get_device_presence: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 

### Return type

[**PresenceEnvelope**](PresenceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_token**
> DeviceTokenEnvelope get_device_token(device_id)

Get Device Token

Retrieves a device's token

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId

try: 
    # Get Device Token
    api_response = api_instance.get_device_token(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->get_device_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceTokenEnvelope**](DeviceTokenEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device**
> DeviceEnvelope update_device(device_id, device)

Update Device

Updates a device

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId
device = artikcloud.Device() # Device | Device to be updated

try: 
    # Update Device
    api_response = api_instance.update_device(device_id, device)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->update_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 
 **device** | [**Device**](Device.md)| Device to be updated | 

### Return type

[**DeviceEnvelope**](DeviceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_token**
> DeviceTokenEnvelope update_device_token(device_id)

Update Device Token

Updates a device's token

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesApi()
device_id = 'device_id_example' # str | deviceId

try: 
    # Update Device Token
    api_response = api_instance.update_device_token(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesApi->update_device_token: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| deviceId | 

### Return type

[**DeviceTokenEnvelope**](DeviceTokenEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


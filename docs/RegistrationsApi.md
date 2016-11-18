# artikcloud.RegistrationsApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_user**](RegistrationsApi.md#confirm_user) | **PUT** /devices/registrations/pin | Confirm User
[**get_request_status_for_user**](RegistrationsApi.md#get_request_status_for_user) | **GET** /devices/registrations/{requestId}/status | Get Request Status For User
[**unregister_device**](RegistrationsApi.md#unregister_device) | **DELETE** /devices/{deviceId}/registrations | Unregister Device


# **confirm_user**
> DeviceRegConfirmUserResponseEnvelope confirm_user(registration_info)

Confirm User

This call updates the registration request issued earlier by associating it with an authenticated user and captures all additional information required to add a new device.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.RegistrationsApi()
registration_info = artikcloud.DeviceRegConfirmUserRequest() # DeviceRegConfirmUserRequest | Device Registration information.

try: 
    # Confirm User
    api_response = api_instance.confirm_user(registration_info)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationsApi->confirm_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_info** | [**DeviceRegConfirmUserRequest**](DeviceRegConfirmUserRequest.md)| Device Registration information. | 

### Return type

[**DeviceRegConfirmUserResponseEnvelope**](DeviceRegConfirmUserResponseEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_status_for_user**
> DeviceRegStatusResponseEnvelope get_request_status_for_user(request_id)

Get Request Status For User

This call checks the status of the request so users can poll and know when registration is complete.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.RegistrationsApi()
request_id = 'request_id_example' # str | Request ID.

try: 
    # Get Request Status For User
    api_response = api_instance.get_request_status_for_user(request_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationsApi->get_request_status_for_user: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID. | 

### Return type

[**DeviceRegStatusResponseEnvelope**](DeviceRegStatusResponseEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_device**
> UnregisterDeviceResponseEnvelope unregister_device(device_id)

Unregister Device

This call clears any associations from the secure device registration.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.RegistrationsApi()
device_id = 'device_id_example' # str | Device ID.

try: 
    # Unregister Device
    api_response = api_instance.unregister_device(device_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling RegistrationsApi->unregister_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 

### Return type

[**UnregisterDeviceResponseEnvelope**](UnregisterDeviceResponseEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# artikcloud.DevicesStatusApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_status**](DevicesStatusApi.md#get_device_status) | **GET** /devices/{deviceId}/status | Get Device Status
[**get_devices_status**](DevicesStatusApi.md#get_devices_status) | **GET** /devices/status | Get Devices Status
[**put_device_status**](DevicesStatusApi.md#put_device_status) | **PUT** /devices/{deviceId}/status | Update Device Status


# **get_device_status**
> DeviceStatus get_device_status(device_id, include_snapshot=include_snapshot, include_snapshot_timestamp=include_snapshot_timestamp)

Get Device Status

Get Device Status

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
api_instance = artikcloud.DevicesStatusApi()
device_id = 'device_id_example' # str | Device ID.
include_snapshot = true # bool | Include device snapshot into the response (optional)
include_snapshot_timestamp = true # bool | Include device snapshot timestamp into the response (optional)

try: 
    # Get Device Status
    api_response = api_instance.get_device_status(device_id, include_snapshot=include_snapshot, include_snapshot_timestamp=include_snapshot_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesStatusApi->get_device_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **include_snapshot** | **bool**| Include device snapshot into the response | [optional] 
 **include_snapshot_timestamp** | **bool**| Include device snapshot timestamp into the response | [optional] 

### Return type

[**DeviceStatus**](DeviceStatus.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_devices_status**
> DeviceStatusBatch get_devices_status(dids, include_snapshot=include_snapshot, include_snapshot_timestamp=include_snapshot_timestamp)

Get Devices Status

Get Devices Status

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
api_instance = artikcloud.DevicesStatusApi()
dids = 'dids_example' # str | List of device ids (comma-separated) for which the statuses are requested.
include_snapshot = true # bool | Include device snapshot into the response (optional)
include_snapshot_timestamp = true # bool | Include device snapshot timestamp into the response (optional)

try: 
    # Get Devices Status
    api_response = api_instance.get_devices_status(dids, include_snapshot=include_snapshot, include_snapshot_timestamp=include_snapshot_timestamp)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesStatusApi->get_devices_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dids** | **str**| List of device ids (comma-separated) for which the statuses are requested. | 
 **include_snapshot** | **bool**| Include device snapshot into the response | [optional] 
 **include_snapshot_timestamp** | **bool**| Include device snapshot timestamp into the response | [optional] 

### Return type

[**DeviceStatusBatch**](DeviceStatusBatch.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_device_status**
> DeviceStatus put_device_status(device_id, body=body)

Update Device Status

Update Device Status

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
api_instance = artikcloud.DevicesStatusApi()
device_id = 'device_id_example' # str | Device ID.
body = artikcloud.DeviceStatusPut() # DeviceStatusPut | Body (optional)

try: 
    # Update Device Status
    api_response = api_instance.put_device_status(device_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicesStatusApi->put_device_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **body** | [**DeviceStatusPut**](DeviceStatusPut.md)| Body | [optional] 

### Return type

[**DeviceStatus**](DeviceStatus.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


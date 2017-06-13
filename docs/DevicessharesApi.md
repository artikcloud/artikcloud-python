# artikcloud.DevicessharesApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_share_for_device**](DevicessharesApi.md#create_share_for_device) | **POST** in/api/devices/{deviceId}/shares | Share a device 
[**delete_sharing_for_device**](DevicessharesApi.md#delete_sharing_for_device) | **DELETE** in/api/devices/{deviceId}/shares/{shareId} | Delete specific share of the given device id
[**get_all_shares_for_device**](DevicessharesApi.md#get_all_shares_for_device) | **GET** in/api/devices/{deviceId}/shares | List all shares for the given device id
[**get_sharing_for_device**](DevicessharesApi.md#get_sharing_for_device) | **GET** in/api/devices/{deviceId}/shares/{shareId} | Get specific share of the given device id


# **create_share_for_device**
> DeviceSharingId create_share_for_device(device_id, device_share_info)

Share a device 

Share a device 

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
api_instance = artikcloud.DevicessharesApi()
device_id = 'device_id_example' # str | Device ID.
device_share_info = artikcloud.DeviceShareInfo() # DeviceShareInfo | Device object that needs to be added

try: 
    # Share a device 
    api_response = api_instance.create_share_for_device(device_id, device_share_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicessharesApi->create_share_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **device_share_info** | [**DeviceShareInfo**](DeviceShareInfo.md)| Device object that needs to be added | 

### Return type

[**DeviceSharingId**](DeviceSharingId.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sharing_for_device**
> DeviceSharingId delete_sharing_for_device(device_id, share_id)

Delete specific share of the given device id

Delete specific share of the given device id

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
api_instance = artikcloud.DevicessharesApi()
device_id = 'device_id_example' # str | Device ID.
share_id = 'share_id_example' # str | Share ID.

try: 
    # Delete specific share of the given device id
    api_response = api_instance.delete_sharing_for_device(device_id, share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicessharesApi->delete_sharing_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **share_id** | **str**| Share ID. | 

### Return type

[**DeviceSharingId**](DeviceSharingId.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_shares_for_device**
> DeviceSharingEnvelope get_all_shares_for_device(device_id, count=count, offset=offset)

List all shares for the given device id

List all shares for the given device id

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
api_instance = artikcloud.DevicessharesApi()
device_id = 'device_id_example' # str | Device ID.
count = 56 # int | Desired count of items in the result set. (optional)
offset = 56 # int | Offset for pagination. (optional)

try: 
    # List all shares for the given device id
    api_response = api_instance.get_all_shares_for_device(device_id, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicessharesApi->get_all_shares_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **count** | **int**| Desired count of items in the result set. | [optional] 
 **offset** | **int**| Offset for pagination. | [optional] 

### Return type

[**DeviceSharingEnvelope**](DeviceSharingEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sharing_for_device**
> DeviceSharing get_sharing_for_device(device_id, share_id)

Get specific share of the given device id

Get specific share of the given device id

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
api_instance = artikcloud.DevicessharesApi()
device_id = 'device_id_example' # str | Device ID.
share_id = 'share_id_example' # str | Share ID.

try: 
    # Get specific share of the given device id
    api_response = api_instance.get_sharing_for_device(device_id, share_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DevicessharesApi->get_sharing_for_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID. | 
 **share_id** | **str**| Share ID. | 

### Return type

[**DeviceSharing**](DeviceSharing.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


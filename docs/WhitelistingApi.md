# artikcloud.WhitelistingApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vdid**](WhitelistingApi.md#delete_vdid) | **DELETE** /devicetypes/{dtid}/whitelist/{vdid} | Delete a vdid from the devicetype whitelist.
[**delete_whitelist_certificate**](WhitelistingApi.md#delete_whitelist_certificate) | **DELETE** /devicetypes/{dtid}/whitelist/certificates/{cid} | Delete a whitelist certificate associated with a devicetype.
[**enable_whitelist**](WhitelistingApi.md#enable_whitelist) | **PUT** /devicetypes/:dtid/whitelist/enable | Enable or disble whitelist feature of a device type
[**get_rejected_row_list**](WhitelistingApi.md#get_rejected_row_list) | **GET** /devicetypes/{dtid}/whitelist/{uploadId}/rejectedRows | Get the list of rejected rows for an uploaded CSV file.
[**get_upload_status**](WhitelistingApi.md#get_upload_status) | **GET** /devicetypes/{dtid}/whitelist/{uploadId}/status | Get the status of a uploaded CSV file.
[**get_whitelist**](WhitelistingApi.md#get_whitelist) | **GET** /devicetypes/{dtid}/whitelist | Get whitelisted vdids of a device type.
[**get_whitelist_certificate**](WhitelistingApi.md#get_whitelist_certificate) | **GET** /devicetypes/{dtid}/whitelist/certificates | Get whitelist certificate of device type.
[**get_whitelist_status**](WhitelistingApi.md#get_whitelist_status) | **GET** /devicetypes/{dtid}/whitelist/status | Get the status of whitelist feature (enabled/disabled) of a device type.
[**upload_csv**](WhitelistingApi.md#upload_csv) | **POST** /devicetypes/{dtid}/whitelist | Upload a CSV file related to the Device Type.


# **delete_vdid**
> WhitelistEnvelope delete_vdid(dtid, vdid)

Delete a vdid from the devicetype whitelist.

Delete a vdid from the devicetype whitelist.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.
vdid = 'vdid_example' # str | Vendor Device ID.

try: 
    # Delete a vdid from the devicetype whitelist.
    api_response = api_instance.delete_vdid(dtid, vdid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->delete_vdid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **vdid** | **str**| Vendor Device ID. | 

### Return type

[**WhitelistEnvelope**](WhitelistEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_whitelist_certificate**
> WhitelistEnvelope delete_whitelist_certificate(dtid, cid)

Delete a whitelist certificate associated with a devicetype.

Delete a whitelist certificate associated with a devicetype.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.
cid = 'cid_example' # str | Certificate ID.

try: 
    # Delete a whitelist certificate associated with a devicetype.
    api_response = api_instance.delete_whitelist_certificate(dtid, cid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->delete_whitelist_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **cid** | **str**| Certificate ID. | 

### Return type

[**WhitelistEnvelope**](WhitelistEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_whitelist**
> WhitelistEnvelope enable_whitelist(dtid, device_type_update_info)

Enable or disble whitelist feature of a device type

Enable or disble whitelist feature of a device type

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.
device_type_update_info = artikcloud.DeviceTypeUpdateInput() # DeviceTypeUpdateInput | Device type update input.

try: 
    # Enable or disble whitelist feature of a device type
    api_response = api_instance.enable_whitelist(dtid, device_type_update_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->enable_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **device_type_update_info** | [**DeviceTypeUpdateInput**](DeviceTypeUpdateInput.md)| Device type update input. | 

### Return type

[**WhitelistEnvelope**](WhitelistEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rejected_row_list**
> RejectedCSVRowsEnvelope get_rejected_row_list(dtid, upload_id, count=count, offset=offset)

Get the list of rejected rows for an uploaded CSV file.

Get the list of rejected rows for an uploaded CSV file.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device type id related to the uploaded CSV file.
upload_id = 'upload_id_example' # str | Upload id related to the uploaded CSV file.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)

try: 
    # Get the list of rejected rows for an uploaded CSV file.
    api_response = api_instance.get_rejected_row_list(dtid, upload_id, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->get_rejected_row_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device type id related to the uploaded CSV file. | 
 **upload_id** | **str**| Upload id related to the uploaded CSV file. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 

### Return type

[**RejectedCSVRowsEnvelope**](RejectedCSVRowsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upload_status**
> UploadStatusEnvelope get_upload_status(dtid, upload_id)

Get the status of a uploaded CSV file.

Get the status of a uploaded CSV file.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device type id related to the uploaded CSV file.
upload_id = 'upload_id_example' # str | Upload id related to the uploaded CSV file.

try: 
    # Get the status of a uploaded CSV file.
    api_response = api_instance.get_upload_status(dtid, upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->get_upload_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device type id related to the uploaded CSV file. | 
 **upload_id** | **str**| Upload id related to the uploaded CSV file. | 

### Return type

[**UploadStatusEnvelope**](UploadStatusEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whitelist**
> WhitelistResultEnvelope get_whitelist(dtid, count=count, offset=offset)

Get whitelisted vdids of a device type.

Get whitelisted vdids of a device type.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)

try: 
    # Get whitelisted vdids of a device type.
    api_response = api_instance.get_whitelist(dtid, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->get_whitelist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 

### Return type

[**WhitelistResultEnvelope**](WhitelistResultEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whitelist_certificate**
> CertificateEnvelope get_whitelist_certificate(dtid)

Get whitelist certificate of device type.

Get whitelist certificate of device type.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.

try: 
    # Get whitelist certificate of device type.
    api_response = api_instance.get_whitelist_certificate(dtid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->get_whitelist_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 

### Return type

[**CertificateEnvelope**](CertificateEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_whitelist_status**
> WhitelistEnvelope get_whitelist_status(dtid)

Get the status of whitelist feature (enabled/disabled) of a device type.

Get the status of whitelist feature (enabled/disabled) of a device type.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.

try: 
    # Get the status of whitelist feature (enabled/disabled) of a device type.
    api_response = api_instance.get_whitelist_status(dtid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->get_whitelist_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 

### Return type

[**WhitelistEnvelope**](WhitelistEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_csv**
> UploadIdEnvelope upload_csv(dtid, file)

Upload a CSV file related to the Device Type.

Upload a CSV file related to the Device Type.

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
api_instance = artikcloud.WhitelistingApi()
dtid = 'dtid_example' # str | Device Type ID.
file = 'B' # str | Device Type ID.

try: 
    # Upload a CSV file related to the Device Type.
    api_response = api_instance.upload_csv(dtid, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WhitelistingApi->upload_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **file** | **str**| Device Type ID. | 

### Return type

[**UploadIdEnvelope**](UploadIdEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


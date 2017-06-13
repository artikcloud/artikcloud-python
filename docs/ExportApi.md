# artikcloud.ExportApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_request**](ExportApi.md#export_request) | **POST** /messages/export | Create Export Request
[**get_export_history**](ExportApi.md#get_export_history) | **GET** /messages/export/history | Get Export History
[**get_export_result**](ExportApi.md#get_export_result) | **GET** /messages/export/{exportId}/result | Get Export Result
[**get_export_status**](ExportApi.md#get_export_status) | **GET** /messages/export/{exportId}/status | Check Export Status


# **export_request**
> ExportRequestResponse export_request(export_request_info)

Create Export Request

Export normalized messages. The following input combinations are supported:<br/><table><tr><th>Combination</th><th>Parameters</th><th>Description</th></tr><tr><td>Get by users</td><td>uids</td><td>Search by a list of User IDs. For each user in the list, the current authenticated user must have read access over the specified user.</td></tr><tr><td>Get by devices</td><td>sdids</td><td>Search by Source Device IDs.</td></tr><tr><td>Get by device types</td><td>uids,sdtids</td><td>Search by list of Source Device Type IDs for the given list of users.</td></tr><tr><td>Get by trial</td><td>trialId</td><td>Search by Trial ID.</td></tr><tr><td>Get by combination of parameters</td><td>uids,sdids,sdtids</td><td>Search by list of Source Device IDs. Each Device ID must belong to a Source Device Type ID and a User ID.</td></tr><tr><td>Common</td><td>startDate,endDate,order,format,url,csvHeaders</td><td>Parameters that can be used with the above combinations.</td></tr></table>

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
api_instance = artikcloud.ExportApi()
export_request_info = artikcloud.ExportRequestInfo() # ExportRequestInfo | ExportRequest object that is passed in the body

try: 
    # Create Export Request
    api_response = api_instance.export_request(export_request_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->export_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_request_info** | [**ExportRequestInfo**](ExportRequestInfo.md)| ExportRequest object that is passed in the body | 

### Return type

[**ExportRequestResponse**](ExportRequestResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_history**
> ExportHistoryResponse get_export_history(trial_id=trial_id, count=count, offset=offset)

Get Export History

Get the history of export requests.

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
api_instance = artikcloud.ExportApi()
trial_id = 'trial_id_example' # str | Filter by trialId. (optional)
count = 56 # int | Pagination count. (optional)
offset = 56 # int | Pagination offset. (optional)

try: 
    # Get Export History
    api_response = api_instance.get_export_history(trial_id=trial_id, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_export_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trial_id** | **str**| Filter by trialId. | [optional] 
 **count** | **int**| Pagination count. | [optional] 
 **offset** | **int**| Pagination offset. | [optional] 

### Return type

[**ExportHistoryResponse**](ExportHistoryResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_result**
> str get_export_result(export_id)

Get Export Result

Retrieve result of the export query in tgz format. The tar file may contain one or more files with the results.

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
api_instance = artikcloud.ExportApi()
export_id = 'export_id_example' # str | Export ID of the export query.

try: 
    # Get Export Result
    api_response = api_instance.get_export_result(export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_export_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Export ID of the export query. | 

### Return type

**str**

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_export_status**
> ExportStatusResponse get_export_status(export_id)

Check Export Status

Check status of the export query.

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
api_instance = artikcloud.ExportApi()
export_id = 'export_id_example' # str | Export ID of the export query.

try: 
    # Check Export Status
    api_response = api_instance.get_export_status(export_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExportApi->get_export_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_id** | **str**| Export ID of the export query. | 

### Return type

[**ExportStatusResponse**](ExportStatusResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


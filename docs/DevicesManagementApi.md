# artikcloud.DevicesManagementApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tasks**](DevicesManagementApi.md#create_tasks) | **POST** /devicemgmt/tasks | Create a new task for one or more devices
[**delete_server_properties**](DevicesManagementApi.md#delete_server_properties) | **DELETE** /devicemgmt/devices/{did}/serverproperties | Deletes a device&#39;s properties.
[**get_all_by_did**](DevicesManagementApi.md#get_all_by_did) | **GET** /devicemgmt/devices/{did}/tasks | Returns the list of tasks for a particular device id with optional status filter.
[**get_device_types_info**](DevicesManagementApi.md#get_device_types_info) | **GET** /devicemgmt/devicetypes/{dtid} | Read a device type device management information.
[**get_manifest_properties**](DevicesManagementApi.md#get_manifest_properties) | **GET** /devicemgmt/devicetypes/{dtid}/manifest/properties | Get a device type&#39;s device management manifest properties
[**get_properties**](DevicesManagementApi.md#get_properties) | **GET** /devicemgmt/devices/{did}/properties | Read a device&#39;s properties.
[**get_statuses**](DevicesManagementApi.md#get_statuses) | **GET** /devicemgmt/tasks/{tid}/statuses | Returns the details and status of a task id and the individual statuses of each device id in the list.
[**get_statuses_history**](DevicesManagementApi.md#get_statuses_history) | **GET** /devicemgmt/tasks/{tid}/statuses/history | Returns the history of the status changes for a specific task id, or for a specific device id in that task.
[**get_task_by_id**](DevicesManagementApi.md#get_task_by_id) | **GET** /devicemgmt/tasks/{tid} | Returns the details and global status of a specific task id.
[**get_tasks**](DevicesManagementApi.md#get_tasks) | **GET** /devicemgmt/tasks | Returns the all the tasks for a device type.
[**query_properties**](DevicesManagementApi.md#query_properties) | **GET** /devicemgmt/devices/properties | Query device properties across devices.
[**update_device_types_info**](DevicesManagementApi.md#update_device_types_info) | **PUT** /devicemgmt/devicetypes/{dtid} | Updates a device type information
[**update_server_properties**](DevicesManagementApi.md#update_server_properties) | **POST** /devicemgmt/devices/{did}/serverproperties | Updates a device&#39;s server properties.
[**update_task**](DevicesManagementApi.md#update_task) | **PUT** /devicemgmt/tasks/{tid} | Updates a task for all devices - For now just allows changing the state to cancelled.
[**update_task_for_device**](DevicesManagementApi.md#update_task_for_device) | **PUT** /devicemgmt/tasks/{tid}/devices/{did} | Updates a task for a specific device - For now just allows changing the state to cancelled.


# **create_tasks**
> TaskEnvelope create_tasks(task_payload)

Create a new task for one or more devices

Create a new task for one or more devices

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
task_payload = artikcloud.TaskRequest() # TaskRequest | Task object to be created

try: 
    # Create a new task for one or more devices
    api_response = api_instance.create_tasks(task_payload)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->create_tasks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_payload** | [**TaskRequest**](TaskRequest.md)| Task object to be created | 

### Return type

[**TaskEnvelope**](TaskEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_properties**
> MetadataEnvelope delete_server_properties(did)

Deletes a device's properties.

Deletes a device's properties.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
did = 'did_example' # str | Device ID.

try: 
    # Deletes a device's properties.
    api_response = api_instance.delete_server_properties(did)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->delete_server_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID. | 

### Return type

[**MetadataEnvelope**](MetadataEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_by_did**
> TaskByDidListEnvelope get_all_by_did(did, count=count, offset=offset, status=status, order=order, sort=sort)

Returns the list of tasks for a particular device id with optional status filter.

Returns the list of tasks for a particular device id with optional status filter.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
did = 'did_example' # str | Device ID.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)
status = 'status_example' # str | Status filter. Comma-separated statuses. (optional)
order = 'order_example' # str | Sort results by a field. Valid fields: createdOn. (optional)
sort = 'sort_example' # str | Sort order. Valid values: asc or desc. (optional)

try: 
    # Returns the list of tasks for a particular device id with optional status filter.
    api_response = api_instance.get_all_by_did(did, count=count, offset=offset, status=status, order=order, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_all_by_did: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 
 **status** | **str**| Status filter. Comma-separated statuses. | [optional] 
 **order** | **str**| Sort results by a field. Valid fields: createdOn. | [optional] 
 **sort** | **str**| Sort order. Valid values: asc or desc. | [optional] 

### Return type

[**TaskByDidListEnvelope**](TaskByDidListEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types_info**
> DeviceTypesInfoEnvelope get_device_types_info(dtid)

Read a device type device management information.

Read a device type device management information.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
dtid = 'dtid_example' # str | Device type ID.

try: 
    # Read a device type device management information.
    api_response = api_instance.get_device_types_info(dtid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_device_types_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device type ID. | 

### Return type

[**DeviceTypesInfoEnvelope**](DeviceTypesInfoEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_properties**
> MetadataPropertiesEnvelope get_manifest_properties(dtid)

Get a device type's device management manifest properties

Get a device type's device management manifest properties

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
dtid = 'dtid_example' # str | Device Type ID.

try: 
    # Get a device type's device management manifest properties
    api_response = api_instance.get_manifest_properties(dtid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_manifest_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 

### Return type

[**MetadataPropertiesEnvelope**](MetadataPropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_properties**
> MetadataEnvelope get_properties(did, include_timestamp=include_timestamp)

Read a device's properties.

Read a device's properties.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
did = 'did_example' # str | Device ID.
include_timestamp = true # bool | Include timestamp. (optional)

try: 
    # Read a device's properties.
    api_response = api_instance.get_properties(did, include_timestamp=include_timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID. | 
 **include_timestamp** | **bool**| Include timestamp. | [optional] 

### Return type

[**MetadataEnvelope**](MetadataEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses**
> TaskStatusesEnvelope get_statuses(tid, count=count, offset=offset, status=status, dids=dids)

Returns the details and status of a task id and the individual statuses of each device id in the list.

Returns the details and status of a task id and the individual statuses of each device id in the list.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
tid = 'tid_example' # str | Task ID.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)
status = 'status_example' # str | Status filter. Comma-separated statuses. (optional)
dids = 'dids_example' # str | Devices filter. Comma-separated device IDs. (optional)

try: 
    # Returns the details and status of a task id and the individual statuses of each device id in the list.
    api_response = api_instance.get_statuses(tid, count=count, offset=offset, status=status, dids=dids)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_statuses: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Task ID. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 
 **status** | **str**| Status filter. Comma-separated statuses. | [optional] 
 **dids** | **str**| Devices filter. Comma-separated device IDs. | [optional] 

### Return type

[**TaskStatusesEnvelope**](TaskStatusesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statuses_history**
> TaskStatusesHistoryEnvelope get_statuses_history(tid, did=did)

Returns the history of the status changes for a specific task id, or for a specific device id in that task.

Returns the history of the status changes for a specific task id, or for a specific device id in that task.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
tid = 'tid_example' # str | Task ID.
did = 'did_example' # str | Device ID. Optional. (optional)

try: 
    # Returns the history of the status changes for a specific task id, or for a specific device id in that task.
    api_response = api_instance.get_statuses_history(tid, did=did)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_statuses_history: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Task ID. | 
 **did** | **str**| Device ID. Optional. | [optional] 

### Return type

[**TaskStatusesHistoryEnvelope**](TaskStatusesHistoryEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_by_id**
> TaskEnvelope get_task_by_id(tid)

Returns the details and global status of a specific task id.

Returns the details and global status of a specific task id.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
tid = 'tid_example' # str | Task ID.

try: 
    # Returns the details and global status of a specific task id.
    api_response = api_instance.get_task_by_id(tid)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_task_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Task ID. | 

### Return type

[**TaskEnvelope**](TaskEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tasks**
> TaskListEnvelope get_tasks(dtid, count=count, offset=offset, status=status, order=order, sort=sort)

Returns the all the tasks for a device type.

Returns the all the tasks for a device type.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
dtid = 'dtid_example' # str | Device Type ID.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)
status = 'status_example' # str | Status filter. Comma-separated statuses. (optional)
order = 'order_example' # str | Sort results by a field. Valid fields: createdOn. (optional)
sort = 'sort_example' # str | Sort order. Valid values: asc or desc. (optional)

try: 
    # Returns the all the tasks for a device type.
    api_response = api_instance.get_tasks(dtid, count=count, offset=offset, status=status, order=order, sort=sort)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->get_tasks: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 
 **status** | **str**| Status filter. Comma-separated statuses. | [optional] 
 **order** | **str**| Sort results by a field. Valid fields: createdOn. | [optional] 
 **sort** | **str**| Sort order. Valid values: asc or desc. | [optional] 

### Return type

[**TaskListEnvelope**](TaskListEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_properties**
> MetadataQueryEnvelope query_properties(dtid, count=count, offset=offset, filter=filter, include_timestamp=include_timestamp)

Query device properties across devices.

Query device properties across devices.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
dtid = 'dtid_example' # str | Device Type ID.
count = 56 # int | Max results count. (optional)
offset = 56 # int | Result starting offset. (optional)
filter = 'filter_example' # str | Query filter. Comma-separated key=value pairs (optional)
include_timestamp = true # bool | Include timestamp. (optional)

try: 
    # Query device properties across devices.
    api_response = api_instance.query_properties(dtid, count=count, offset=offset, filter=filter, include_timestamp=include_timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->query_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device Type ID. | 
 **count** | **int**| Max results count. | [optional] 
 **offset** | **int**| Result starting offset. | [optional] 
 **filter** | **str**| Query filter. Comma-separated key&#x3D;value pairs | [optional] 
 **include_timestamp** | **bool**| Include timestamp. | [optional] 

### Return type

[**MetadataQueryEnvelope**](MetadataQueryEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_types_info**
> DeviceTypesInfoEnvelope update_device_types_info(dtid, device_type_info)

Updates a device type information

Updates a device type information

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
dtid = 'dtid_example' # str | Device type ID.
device_type_info = artikcloud.DeviceTypesInfo() # DeviceTypesInfo | Device type info object to be set

try: 
    # Updates a device type information
    api_response = api_instance.update_device_types_info(dtid, device_type_info)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->update_device_types_info: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| Device type ID. | 
 **device_type_info** | [**DeviceTypesInfo**](DeviceTypesInfo.md)| Device type info object to be set | 

### Return type

[**DeviceTypesInfoEnvelope**](DeviceTypesInfoEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_properties**
> MetadataEnvelope update_server_properties(did, device_properties)

Updates a device's server properties.

Updates a device's server properties.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
did = 'did_example' # str | Device ID.
device_properties = NULL # object | Device properties object to be set

try: 
    # Updates a device's server properties.
    api_response = api_instance.update_server_properties(did, device_properties)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->update_server_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID. | 
 **device_properties** | **object**| Device properties object to be set | 

### Return type

[**MetadataEnvelope**](MetadataEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task**
> TaskUpdateResponse update_task(tid, task_update_request)

Updates a task for all devices - For now just allows changing the state to cancelled.

Updates a task for all devices - For now just allows changing the state to cancelled.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
tid = 'tid_example' # str | Task ID.
task_update_request = artikcloud.TaskUpdateRequest() # TaskUpdateRequest | Task update request

try: 
    # Updates a task for all devices - For now just allows changing the state to cancelled.
    api_response = api_instance.update_task(tid, task_update_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->update_task: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Task ID. | 
 **task_update_request** | [**TaskUpdateRequest**](TaskUpdateRequest.md)| Task update request | 

### Return type

[**TaskUpdateResponse**](TaskUpdateResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_task_for_device**
> DeviceTaskUpdateResponse update_task_for_device(tid, did, device_task_update_request)

Updates a task for a specific device - For now just allows changing the state to cancelled.

Updates a task for a specific device - For now just allows changing the state to cancelled.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DevicesManagementApi()
tid = 'tid_example' # str | Task ID.
did = 'did_example' # str | Device ID.
device_task_update_request = artikcloud.DeviceTaskUpdateRequest() # DeviceTaskUpdateRequest | Device task update request

try: 
    # Updates a task for a specific device - For now just allows changing the state to cancelled.
    api_response = api_instance.update_task_for_device(tid, did, device_task_update_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DevicesManagementApi->update_task_for_device: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tid** | **str**| Task ID. | 
 **did** | **str**| Device ID. | 
 **device_task_update_request** | [**DeviceTaskUpdateRequest**](DeviceTaskUpdateRequest.md)| Device task update request | 

### Return type

[**DeviceTaskUpdateResponse**](DeviceTaskUpdateResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


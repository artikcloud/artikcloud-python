# artikcloud.DeviceTypesApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_available_manifest_versions**](DeviceTypesApi.md#get_available_manifest_versions) | **GET** /devicetypes/{deviceTypeId}/availablemanifestversions | Get Available Manifest Versions
[**get_device_type**](DeviceTypesApi.md#get_device_type) | **GET** /devicetypes/{deviceTypeId} | Get Device Type
[**get_device_types**](DeviceTypesApi.md#get_device_types) | **GET** /devicetypes | Get Device Types
[**get_device_types_by_application**](DeviceTypesApi.md#get_device_types_by_application) | **GET** /applications/{appId}/devicetypes | Get Device Types by Application
[**get_latest_manifest_properties**](DeviceTypesApi.md#get_latest_manifest_properties) | **GET** /devicetypes/{deviceTypeId}/manifests/latest/properties | Get Latest Manifest Properties
[**get_manifest_properties**](DeviceTypesApi.md#get_manifest_properties) | **GET** /devicetypes/{deviceTypeId}/manifests/{version}/properties | Get manifest properties


# **get_available_manifest_versions**
> ManifestVersionsEnvelope get_available_manifest_versions(device_type_id)

Get Available Manifest Versions

Get a Device Type's available manifest versions

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
device_type_id = 'device_type_id_example' # str | deviceTypeId

try: 
    # Get Available Manifest Versions
    api_response = api_instance.get_available_manifest_versions(device_type_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_available_manifest_versions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_id** | **str**| deviceTypeId | 

### Return type

[**ManifestVersionsEnvelope**](ManifestVersionsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type**
> DeviceTypeEnvelope get_device_type(device_type_id)

Get Device Type

Retrieves a Device Type

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
device_type_id = 'device_type_id_example' # str | deviceTypeId

try: 
    # Get Device Type
    api_response = api_instance.get_device_type(device_type_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_device_type: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_id** | **str**| deviceTypeId | 

### Return type

[**DeviceTypeEnvelope**](DeviceTypeEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types**
> DeviceTypesEnvelope get_device_types(name, offset=offset, count=count, tags=tags)

Get Device Types

Retrieves Device Types

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
name = 'name_example' # str | Device Type name
offset = 56 # int | Offset for pagination. (optional)
count = 56 # int | Desired count of items in the result set (optional)
tags = 'tags_example' # str | Elements tagged with the list of tags. (comma separated) (optional)

try: 
    # Get Device Types
    api_response = api_instance.get_device_types(name, offset=offset, count=count, tags=tags)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_device_types: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Device Type name | 
 **offset** | **int**| Offset for pagination. | [optional] 
 **count** | **int**| Desired count of items in the result set | [optional] 
 **tags** | **str**| Elements tagged with the list of tags. (comma separated) | [optional] 

### Return type

[**DeviceTypesEnvelope**](DeviceTypesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_types_by_application**
> DeviceTypesEnvelope get_device_types_by_application(app_id, product_info=product_info, count=count, offset=offset)

Get Device Types by Application

Get Device Types by Application

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
app_id = 'app_id_example' # str | Application ID.
product_info = true # bool | Flag to include the associated ProductInfo if present (optional)
count = 56 # int | Desired count of items in the result set. (optional)
offset = 56 # int | Offset for pagination. (optional)

try: 
    # Get Device Types by Application
    api_response = api_instance.get_device_types_by_application(app_id, product_info=product_info, count=count, offset=offset)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_device_types_by_application: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| Application ID. | 
 **product_info** | **bool**| Flag to include the associated ProductInfo if present | [optional] 
 **count** | **int**| Desired count of items in the result set. | [optional] 
 **offset** | **int**| Offset for pagination. | [optional] 

### Return type

[**DeviceTypesEnvelope**](DeviceTypesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest_manifest_properties**
> ManifestPropertiesEnvelope get_latest_manifest_properties(device_type_id)

Get Latest Manifest Properties

Get a Device Type's manifest properties for the latest version.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
device_type_id = 'device_type_id_example' # str | Device Type ID.

try: 
    # Get Latest Manifest Properties
    api_response = api_instance.get_latest_manifest_properties(device_type_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_latest_manifest_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_id** | **str**| Device Type ID. | 

### Return type

[**ManifestPropertiesEnvelope**](ManifestPropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manifest_properties**
> ManifestPropertiesEnvelope get_manifest_properties(device_type_id, version)

Get manifest properties

Get a Device Type's manifest properties for a specific version.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.DeviceTypesApi()
device_type_id = 'device_type_id_example' # str | Device Type ID.
version = 'version_example' # str | Manifest Version.

try: 
    # Get manifest properties
    api_response = api_instance.get_manifest_properties(device_type_id, version)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeviceTypesApi->get_manifest_properties: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_type_id** | **str**| Device Type ID. | 
 **version** | **str**| Manifest Version. | 

### Return type

[**ManifestPropertiesEnvelope**](ManifestPropertiesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


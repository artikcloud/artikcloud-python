# artikcloud.TagsApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_categories**](TagsApi.md#get_tag_categories) | **GET** /tags/categories | Get all categories
[**get_tag_suggestions**](TagsApi.md#get_tag_suggestions) | **GET** /tags/suggestions | Get tag suggestions
[**get_tags_by_categories**](TagsApi.md#get_tags_by_categories) | **GET** /tags | Get all tags of categories


# **get_tag_categories**
> TagsEnvelope get_tag_categories()

Get all categories

Get all tags marked as categories

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.TagsApi()

try: 
    # Get all categories
    api_response = api_instance.get_tag_categories()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagsApi->get_tag_categories: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TagsEnvelope**](TagsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tag_suggestions**
> TagsEnvelope get_tag_suggestions(entity_type=entity_type, tags=tags, name=name, count=count)

Get tag suggestions

Get tag suggestions for applications, device types that have been most used with a group of tags.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.TagsApi()
entity_type = 'entity_type_example' # str | Entity type name. (optional)
tags = 'tags_example' # str | Comma separated list of tags. (optional)
name = 'name_example' # str | Name of tags used for type ahead. (optional)
count = 56 # int | Number of results to return. Max 10. (optional)

try: 
    # Get tag suggestions
    api_response = api_instance.get_tag_suggestions(entity_type=entity_type, tags=tags, name=name, count=count)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagsApi->get_tag_suggestions: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | **str**| Entity type name. | [optional] 
 **tags** | **str**| Comma separated list of tags. | [optional] 
 **name** | **str**| Name of tags used for type ahead. | [optional] 
 **count** | **int**| Number of results to return. Max 10. | [optional] 

### Return type

[**TagsEnvelope**](TagsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tags_by_categories**
> TagsEnvelope get_tags_by_categories(categories=categories)

Get all tags of categories

Get all tags related to the list of categories

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.TagsApi()
categories = 'categories_example' # str | Comma separated list of categories. (optional)

try: 
    # Get all tags of categories
    api_response = api_instance.get_tags_by_categories(categories=categories)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling TagsApi->get_tags_by_categories: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categories** | **str**| Comma separated list of categories. | [optional] 

### Return type

[**TagsEnvelope**](TagsEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


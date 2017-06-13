# artikcloud.RulesApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rule**](RulesApi.md#create_rule) | **POST** /rules | Create Rule
[**delete_rule**](RulesApi.md#delete_rule) | **DELETE** /rules/{ruleId} | Delete Rule
[**get_rule**](RulesApi.md#get_rule) | **GET** /rules/{ruleId} | Get Rule
[**update_rule**](RulesApi.md#update_rule) | **PUT** /rules/{ruleId} | Update Rule


# **create_rule**
> RuleEnvelope create_rule(rule_info, user_id)

Create Rule

Create a new Rule

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
api_instance = artikcloud.RulesApi()
rule_info = artikcloud.RuleCreationInfo() # RuleCreationInfo | Rule object that needs to be added
user_id = 'user_id_example' # str | User ID

try: 
    # Create Rule
    api_response = api_instance.create_rule(rule_info, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->create_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_info** | [**RuleCreationInfo**](RuleCreationInfo.md)| Rule object that needs to be added | 
 **user_id** | **str**| User ID | 

### Return type

[**RuleEnvelope**](RuleEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> RuleEnvelope delete_rule(rule_id)

Delete Rule

Delete a Rule

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
api_instance = artikcloud.RulesApi()
rule_id = 'rule_id_example' # str | Rule ID.

try: 
    # Delete Rule
    api_response = api_instance.delete_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule ID. | 

### Return type

[**RuleEnvelope**](RuleEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> RuleEnvelope get_rule(rule_id)

Get Rule

Get a rule using the Rule ID

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
api_instance = artikcloud.RulesApi()
rule_id = 'rule_id_example' # str | Rule ID.

try: 
    # Get Rule
    api_response = api_instance.get_rule(rule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->get_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule ID. | 

### Return type

[**RuleEnvelope**](RuleEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleEnvelope update_rule(rule_id, rule_info)

Update Rule

Update an existing Rule

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
api_instance = artikcloud.RulesApi()
rule_id = 'rule_id_example' # str | Rule ID.
rule_info = artikcloud.RuleUpdateInfo() # RuleUpdateInfo | Rule object that needs to be updated

try: 
    # Update Rule
    api_response = api_instance.update_rule(rule_id, rule_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RulesApi->update_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**| Rule ID. | 
 **rule_info** | [**RuleUpdateInfo**](RuleUpdateInfo.md)| Rule object that needs to be updated | 

### Return type

[**RuleEnvelope**](RuleEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


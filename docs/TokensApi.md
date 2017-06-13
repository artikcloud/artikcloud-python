# artikcloud.TokensApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_token**](TokensApi.md#check_token) | **POST** /accounts/checkToken | Check Token
[**refresh_token**](TokensApi.md#refresh_token) | **POST** /accounts/token | Refresh Token
[**token_info**](TokensApi.md#token_info) | **GET** /accounts/tokenInfo | Token Info


# **check_token**
> CheckTokenResponse check_token(token_info)

Check Token

(Deprecated) Check Token. See tokenInfo

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
api_instance = artikcloud.TokensApi()
token_info = artikcloud.TokenRequest() # TokenRequest | Token object to be checked

try: 
    # Check Token
    api_response = api_instance.check_token(token_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->check_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_info** | [**TokenRequest**](TokenRequest.md)| Token object to be checked | 

### Return type

[**CheckTokenResponse**](CheckTokenResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> RefreshTokenResponse refresh_token(grant_type, refresh_token)

Refresh Token

Refresh Token

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
api_instance = artikcloud.TokensApi()
grant_type = 'grant_type_example' # str | Grant Type.
refresh_token = 'refresh_token_example' # str | Refresh Token.

try: 
    # Refresh Token
    api_response = api_instance.refresh_token(grant_type, refresh_token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->refresh_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Grant Type. | 
 **refresh_token** | **str**| Refresh Token. | 

### Return type

[**RefreshTokenResponse**](RefreshTokenResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **token_info**
> TokenInfoSuccessResponse token_info()

Token Info

Returns the Token Information

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
api_instance = artikcloud.TokensApi()

try: 
    # Token Info
    api_response = api_instance.token_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApi->token_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenInfoSuccessResponse**](TokenInfoSuccessResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


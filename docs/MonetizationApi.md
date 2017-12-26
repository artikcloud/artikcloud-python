# artikcloud.MonetizationApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pricing_tiers**](MonetizationApi.md#create_pricing_tiers) | **POST** /pricing/devicetypes/{dtid}/pricingtiers | Define devicetype&#39;s pricing tiers.
[**get_pricing_tiers**](MonetizationApi.md#get_pricing_tiers) | **GET** /pricing/devices/{did}/pricingtiers | Get a device&#39;s pricing tiers
[**get_the__pricing_tiers**](MonetizationApi.md#get_the__pricing_tiers) | **GET** /pricing/devicetypes/{dtid}/pricingtiers | Get devicetype&#39;s pricing tiers.
[**get_upgrade_path**](MonetizationApi.md#get_upgrade_path) | **GET** /pricing/devices/{did}/revenueshare/upgradepath | Get upgrade path
[**set_pricing_tier**](MonetizationApi.md#set_pricing_tier) | **PUT** /pricing/devices/{did}/pricingtiers | Set a device&#39;s pricing tier


# **create_pricing_tiers**
> DeviceTypePricingTier create_pricing_tiers(dtid, pricing_tier_info)

Define devicetype's pricing tiers.

Define devicetype's pricing tiers.

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
api_instance = artikcloud.MonetizationApi()
dtid = 'dtid_example' # str | DeviceType ID
pricing_tier_info = artikcloud.DeviceTypePricingTier() # DeviceTypePricingTier | Pricing tier info

try: 
    # Define devicetype's pricing tiers.
    api_response = api_instance.create_pricing_tiers(dtid, pricing_tier_info)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonetizationApi->create_pricing_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| DeviceType ID | 
 **pricing_tier_info** | [**DeviceTypePricingTier**](DeviceTypePricingTier.md)| Pricing tier info | 

### Return type

[**DeviceTypePricingTier**](DeviceTypePricingTier.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pricing_tiers**
> DevicePricingTiersEnvelope get_pricing_tiers(did, active=active)

Get a device's pricing tiers

Get a device's pricing tiers

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
api_instance = artikcloud.MonetizationApi()
did = 'did_example' # str | Device ID
active = true # bool | Filter by active (optional)

try: 
    # Get a device's pricing tiers
    api_response = api_instance.get_pricing_tiers(did, active=active)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonetizationApi->get_pricing_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID | 
 **active** | **bool**| Filter by active | [optional] 

### Return type

[**DevicePricingTiersEnvelope**](DevicePricingTiersEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_the__pricing_tiers**
> DeviceTypePricingTiersEnvelope get_the__pricing_tiers(dtid, version)

Get devicetype's pricing tiers.

Get devicetype's pricing tiers.

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
api_instance = artikcloud.MonetizationApi()
dtid = 'dtid_example' # str | DeviceType ID
version = 56 # int | Version

try: 
    # Get devicetype's pricing tiers.
    api_response = api_instance.get_the__pricing_tiers(dtid, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonetizationApi->get_the__pricing_tiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dtid** | **str**| DeviceType ID | 
 **version** | **int**| Version | 

### Return type

[**DeviceTypePricingTiersEnvelope**](DeviceTypePricingTiersEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upgrade_path**
> UpgradePathEnvelope get_upgrade_path(did, action)

Get upgrade path

Get upgrade path

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
api_instance = artikcloud.MonetizationApi()
did = 'did_example' # str | Device ID
action = 'action_example' # str | Action to perform

try: 
    # Get upgrade path
    api_response = api_instance.get_upgrade_path(did, action)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonetizationApi->get_upgrade_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID | 
 **action** | **str**| Action to perform | 

### Return type

[**UpgradePathEnvelope**](UpgradePathEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_pricing_tier**
> DevicePricingTierEnvelope set_pricing_tier(did, pricing_tier)

Set a device's pricing tier

Set a device's pricing tier

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
api_instance = artikcloud.MonetizationApi()
did = 'did_example' # str | Device ID
pricing_tier = artikcloud.DevicePricingTierRequest() # DevicePricingTierRequest | Pricing tier

try: 
    # Set a device's pricing tier
    api_response = api_instance.set_pricing_tier(did, pricing_tier)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonetizationApi->set_pricing_tier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **did** | **str**| Device ID | 
 **pricing_tier** | [**DevicePricingTierRequest**](DevicePricingTierRequest.md)| Pricing tier | 

### Return type

[**DevicePricingTierEnvelope**](DevicePricingTierEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


ARTIK Cloud Python SDK
======================

[![PyPI version](https://badge.fury.io/py/artikcloud.svg)](https://badge.fury.io/py/artikcloud)
  
This SDK helps you connect your Python scripts to ARTIK Cloud. The SDK helps authenticating with ARTIK Cloud, and exposes a number of methods to easily execute REST API calls to ARTIK Cloud.

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import artikcloud 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import artikcloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://api.artik.cloud/v1.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceTypesApi* | [**get_available_manifest_versions**](docs/DeviceTypesApi.md#get_available_manifest_versions) | **GET** /devicetypes/{deviceTypeId}/availablemanifestversions | Get Available Manifest Versions
*DeviceTypesApi* | [**get_device_type**](docs/DeviceTypesApi.md#get_device_type) | **GET** /devicetypes/{deviceTypeId} | Get Device Type
*DeviceTypesApi* | [**get_device_types**](docs/DeviceTypesApi.md#get_device_types) | **GET** /devicetypes | Get Device Types
*DeviceTypesApi* | [**get_latest_manifest_properties**](docs/DeviceTypesApi.md#get_latest_manifest_properties) | **GET** /devicetypes/{deviceTypeId}/manifests/latest/properties | Get Latest Manifest Properties
*DeviceTypesApi* | [**get_manifest_properties**](docs/DeviceTypesApi.md#get_manifest_properties) | **GET** /devicetypes/{deviceTypeId}/manifests/{version}/properties | Get manifest properties
*DevicesApi* | [**add_device**](docs/DevicesApi.md#add_device) | **POST** /devices | Add Device
*DevicesApi* | [**delete_device**](docs/DevicesApi.md#delete_device) | **DELETE** /devices/{deviceId} | Delete Device
*DevicesApi* | [**delete_device_token**](docs/DevicesApi.md#delete_device_token) | **DELETE** /devices/{deviceId}/tokens | Delete Device Token
*DevicesApi* | [**get_device**](docs/DevicesApi.md#get_device) | **GET** /devices/{deviceId} | Get Device
*DevicesApi* | [**get_device_presence**](docs/DevicesApi.md#get_device_presence) | **GET** /devices/{deviceId}/presence | Get device presence information
*DevicesApi* | [**get_device_token**](docs/DevicesApi.md#get_device_token) | **GET** /devices/{deviceId}/tokens | Get Device Token
*DevicesApi* | [**update_device**](docs/DevicesApi.md#update_device) | **PUT** /devices/{deviceId} | Update Device
*DevicesApi* | [**update_device_token**](docs/DevicesApi.md#update_device_token) | **PUT** /devices/{deviceId}/tokens | Update Device Token
*ExportApi* | [**export_request**](docs/ExportApi.md#export_request) | **POST** /messages/export | Create Export Request
*ExportApi* | [**get_export_history**](docs/ExportApi.md#get_export_history) | **GET** /messages/export/history | Get Export History
*ExportApi* | [**get_export_result**](docs/ExportApi.md#get_export_result) | **GET** /messages/export/{exportId}/result | Get Export Result
*ExportApi* | [**get_export_status**](docs/ExportApi.md#get_export_status) | **GET** /messages/export/{exportId}/status | Check Export Status
*MessagesApi* | [**get_aggregates_histogram**](docs/MessagesApi.md#get_aggregates_histogram) | **GET** /messages/analytics/histogram | Get Normalized Message Histogram
*MessagesApi* | [**get_field_presence**](docs/MessagesApi.md#get_field_presence) | **GET** /messages/presence | Get normalized message presence
*MessagesApi* | [**get_last_normalized_messages**](docs/MessagesApi.md#get_last_normalized_messages) | **GET** /messages/last | Get Last Normalized Message
*MessagesApi* | [**get_message_aggregates**](docs/MessagesApi.md#get_message_aggregates) | **GET** /messages/analytics/aggregates | Get Normalized Message Aggregates
*MessagesApi* | [**get_message_snapshots**](docs/MessagesApi.md#get_message_snapshots) | **GET** /messages/snapshots | Get Message Snapshots
*MessagesApi* | [**get_normalized_actions**](docs/MessagesApi.md#get_normalized_actions) | **GET** /actions | Get Normalized Actions
*MessagesApi* | [**get_normalized_messages**](docs/MessagesApi.md#get_normalized_messages) | **GET** /messages | Get Normalized Messages
*MessagesApi* | [**send_actions**](docs/MessagesApi.md#send_actions) | **POST** /actions | Send Actions
*MessagesApi* | [**send_message**](docs/MessagesApi.md#send_message) | **POST** /messages | Send Message
*RegistrationsApi* | [**confirm_user**](docs/RegistrationsApi.md#confirm_user) | **PUT** /devices/registrations/pin | Confirm User
*RegistrationsApi* | [**get_request_status_for_user**](docs/RegistrationsApi.md#get_request_status_for_user) | **GET** /devices/registrations/{requestId}/status | Get Request Status For User
*RegistrationsApi* | [**unregister_device**](docs/RegistrationsApi.md#unregister_device) | **DELETE** /devices/{deviceId}/registrations | Unregister Device
*RulesApi* | [**create_rule**](docs/RulesApi.md#create_rule) | **POST** /rules | Create Rule
*RulesApi* | [**delete_rule**](docs/RulesApi.md#delete_rule) | **DELETE** /rules/{ruleId} | Delete Rule
*RulesApi* | [**get_rule**](docs/RulesApi.md#get_rule) | **GET** /rules/{ruleId} | Get Rule
*RulesApi* | [**update_rule**](docs/RulesApi.md#update_rule) | **PUT** /rules/{ruleId} | Update Rule
*TagsApi* | [**get_tag_categories**](docs/TagsApi.md#get_tag_categories) | **GET** /tags/categories | Get all categories
*TagsApi* | [**get_tag_suggestions**](docs/TagsApi.md#get_tag_suggestions) | **GET** /tags/suggestions | Get tag suggestions
*TagsApi* | [**get_tags_by_categories**](docs/TagsApi.md#get_tags_by_categories) | **GET** /tags | Get all tags of categories
*TokensApi* | [**check_token**](docs/TokensApi.md#check_token) | **POST** /accounts/checkToken | Check Token
*TokensApi* | [**refresh_token**](docs/TokensApi.md#refresh_token) | **POST** /accounts/token | Refresh Token
*TokensApi* | [**token_info**](docs/TokensApi.md#token_info) | **GET** /accounts/tokenInfo | Token Info
*UsersApi* | [**create_user_properties**](docs/UsersApi.md#create_user_properties) | **POST** /users/{userId}/properties | Create User Application Properties
*UsersApi* | [**delete_user_properties**](docs/UsersApi.md#delete_user_properties) | **DELETE** /users/{userId}/properties | Delete User Application Properties
*UsersApi* | [**get_self**](docs/UsersApi.md#get_self) | **GET** /users/self | Get Current User Profile
*UsersApi* | [**get_user_device_types**](docs/UsersApi.md#get_user_device_types) | **GET** /users/{userId}/devicetypes | Get User Device Types
*UsersApi* | [**get_user_devices**](docs/UsersApi.md#get_user_devices) | **GET** /users/{userId}/devices | Get User Devices
*UsersApi* | [**get_user_properties**](docs/UsersApi.md#get_user_properties) | **GET** /users/{userId}/properties | Get User application properties
*UsersApi* | [**get_user_rules**](docs/UsersApi.md#get_user_rules) | **GET** /users/{userId}/rules | Get User Rules
*UsersApi* | [**update_user_properties**](docs/UsersApi.md#update_user_properties) | **PUT** /users/{userId}/properties | Update User Application Properties


## Documentation For Models

 - [AckEnvelope](docs/AckEnvelope.md)
 - [Acknowledgement](docs/Acknowledgement.md)
 - [Action](docs/Action.md)
 - [ActionArray](docs/ActionArray.md)
 - [ActionDetails](docs/ActionDetails.md)
 - [ActionDetailsArray](docs/ActionDetailsArray.md)
 - [ActionIn](docs/ActionIn.md)
 - [ActionOut](docs/ActionOut.md)
 - [Actions](docs/Actions.md)
 - [AggregateData](docs/AggregateData.md)
 - [AggregatesHistogramData](docs/AggregatesHistogramData.md)
 - [AggregatesHistogramResponse](docs/AggregatesHistogramResponse.md)
 - [AggregatesResponse](docs/AggregatesResponse.md)
 - [AppProperties](docs/AppProperties.md)
 - [CheckTokenMessage](docs/CheckTokenMessage.md)
 - [CheckTokenResponse](docs/CheckTokenResponse.md)
 - [Device](docs/Device.md)
 - [DeviceArray](docs/DeviceArray.md)
 - [DeviceEnvelope](docs/DeviceEnvelope.md)
 - [DeviceRegCompleteRequest](docs/DeviceRegCompleteRequest.md)
 - [DeviceRegConfirmUserRequest](docs/DeviceRegConfirmUserRequest.md)
 - [DeviceRegConfirmUserResponse](docs/DeviceRegConfirmUserResponse.md)
 - [DeviceRegConfirmUserResponseEnvelope](docs/DeviceRegConfirmUserResponseEnvelope.md)
 - [DeviceRegStatusResponse](docs/DeviceRegStatusResponse.md)
 - [DeviceRegStatusResponseEnvelope](docs/DeviceRegStatusResponseEnvelope.md)
 - [DeviceToken](docs/DeviceToken.md)
 - [DeviceTokenEnvelope](docs/DeviceTokenEnvelope.md)
 - [DeviceType](docs/DeviceType.md)
 - [DeviceTypeArray](docs/DeviceTypeArray.md)
 - [DeviceTypeEnvelope](docs/DeviceTypeEnvelope.md)
 - [DeviceTypesEnvelope](docs/DeviceTypesEnvelope.md)
 - [DevicesEnvelope](docs/DevicesEnvelope.md)
 - [ErrorEnvelope](docs/ErrorEnvelope.md)
 - [ExportData](docs/ExportData.md)
 - [ExportDataArray](docs/ExportDataArray.md)
 - [ExportHistoryResponse](docs/ExportHistoryResponse.md)
 - [ExportNormalizedMessagesResponse](docs/ExportNormalizedMessagesResponse.md)
 - [ExportRequest](docs/ExportRequest.md)
 - [ExportRequestData](docs/ExportRequestData.md)
 - [ExportRequestInfo](docs/ExportRequestInfo.md)
 - [ExportRequestResponse](docs/ExportRequestResponse.md)
 - [ExportResponse](docs/ExportResponse.md)
 - [ExportStatusResponse](docs/ExportStatusResponse.md)
 - [FieldPath](docs/FieldPath.md)
 - [FieldPresence](docs/FieldPresence.md)
 - [FieldPresenceEnvelope](docs/FieldPresenceEnvelope.md)
 - [FieldsActions](docs/FieldsActions.md)
 - [ManifestProperties](docs/ManifestProperties.md)
 - [ManifestPropertiesEnvelope](docs/ManifestPropertiesEnvelope.md)
 - [ManifestVersions](docs/ManifestVersions.md)
 - [ManifestVersionsEnvelope](docs/ManifestVersionsEnvelope.md)
 - [Message](docs/Message.md)
 - [MessageAction](docs/MessageAction.md)
 - [MessageID](docs/MessageID.md)
 - [MessageIDEnvelope](docs/MessageIDEnvelope.md)
 - [MessageIn](docs/MessageIn.md)
 - [MessageOut](docs/MessageOut.md)
 - [NonEmptyString](docs/NonEmptyString.md)
 - [NormalizedAction](docs/NormalizedAction.md)
 - [NormalizedActionsEnvelope](docs/NormalizedActionsEnvelope.md)
 - [NormalizedMessage](docs/NormalizedMessage.md)
 - [NormalizedMessagesEnvelope](docs/NormalizedMessagesEnvelope.md)
 - [OutputRule](docs/OutputRule.md)
 - [PresenceEnvelope](docs/PresenceEnvelope.md)
 - [PresenceModel](docs/PresenceModel.md)
 - [PropertiesEnvelope](docs/PropertiesEnvelope.md)
 - [RefreshTokenResponse](docs/RefreshTokenResponse.md)
 - [RegisterMessage](docs/RegisterMessage.md)
 - [RuleArray](docs/RuleArray.md)
 - [RuleCreationInfo](docs/RuleCreationInfo.md)
 - [RuleEnvelope](docs/RuleEnvelope.md)
 - [RuleError](docs/RuleError.md)
 - [RuleUpdateInfo](docs/RuleUpdateInfo.md)
 - [RuleWarningOutput](docs/RuleWarningOutput.md)
 - [RulesEnvelope](docs/RulesEnvelope.md)
 - [SnapshotResponse](docs/SnapshotResponse.md)
 - [SnapshotResponses](docs/SnapshotResponses.md)
 - [SnapshotsResponseEnvelope](docs/SnapshotsResponseEnvelope.md)
 - [Tag](docs/Tag.md)
 - [TagArray](docs/TagArray.md)
 - [TagsEnvelope](docs/TagsEnvelope.md)
 - [Token](docs/Token.md)
 - [TokenInfo](docs/TokenInfo.md)
 - [TokenInfoSuccessResponse](docs/TokenInfoSuccessResponse.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [UnregisterDeviceResponse](docs/UnregisterDeviceResponse.md)
 - [UnregisterDeviceResponseEnvelope](docs/UnregisterDeviceResponseEnvelope.md)
 - [User](docs/User.md)
 - [UserEnvelope](docs/UserEnvelope.md)
 - [WebSocketError](docs/WebSocketError.md)


## Documentation For Authorization


## artikcloud_oauth

- **Type**: OAuth
- **Flow**: implicit
- **Authorization URL**: https://accounts.artik.cloud/authorize
- **Scopes**: 
 - **read:artikcloud**: Read from ARTIK Cloud
 - **write:artikcloud**: Write from ARTIK Cloud

Usage
------

Peek into [tests](https://github.com/artikcloud/artikcloud-python/tree/master/test) for examples about how to use the SDK.

More about ARTIK Cloud
----------------------

If you are not familiar with ARTIK Cloud, we have extensive documentation at https://developer.artik.cloud/documentation

The full ARTIK Cloud API specification can be found at https://developer.artik.cloud/documentation/api-reference/

Check out advanced sample applications at https://developer.artik.cloud/documentation/samples/

To create and manage your services and devices on ARTIK Cloud, create an account at https://developer.artik.cloud

Also see the ARTIK Cloud blog for tutorials, updates, and more: http://artik.io/blog/cloud

License and Copyright
---------------------

Licensed under the Apache License. See [LICENSE](https://github.com/artikcloud/artikcloud-java/blob/master/LICENSE).

Copyright (c) 2016 Samsung Electronics Co., Ltd.




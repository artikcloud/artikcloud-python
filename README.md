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
from __future__ import print_function
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
*DeviceTypesApi* | [**get_device_types_by_application**](docs/DeviceTypesApi.md#get_device_types_by_application) | **GET** /applications/{appId}/devicetypes | Get Device Types by Application
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
*DevicesManagementApi* | [**create_tasks**](docs/DevicesManagementApi.md#create_tasks) | **POST** /devicemgmt/tasks | Create a new task for one or more devices
*DevicesManagementApi* | [**delete_server_properties**](docs/DevicesManagementApi.md#delete_server_properties) | **DELETE** /devicemgmt/devices/{did}/serverproperties | Deletes a device&#39;s properties.
*DevicesManagementApi* | [**get_all_by_did**](docs/DevicesManagementApi.md#get_all_by_did) | **GET** /devicemgmt/devices/{did}/tasks | Returns the list of tasks for a particular device id with optional status filter.
*DevicesManagementApi* | [**get_device_types_info**](docs/DevicesManagementApi.md#get_device_types_info) | **GET** /devicemgmt/devicetypes/{dtid} | Read a device type device management information.
*DevicesManagementApi* | [**get_manifest_properties**](docs/DevicesManagementApi.md#get_manifest_properties) | **GET** /devicemgmt/devicetypes/{dtid}/manifest/properties | Get a device type&#39;s device management manifest properties
*DevicesManagementApi* | [**get_properties**](docs/DevicesManagementApi.md#get_properties) | **GET** /devicemgmt/devices/{did}/properties | Read a device&#39;s properties.
*DevicesManagementApi* | [**get_statuses**](docs/DevicesManagementApi.md#get_statuses) | **GET** /devicemgmt/tasks/{tid}/statuses | Returns the details and status of a task id and the individual statuses of each device id in the list.
*DevicesManagementApi* | [**get_statuses_history**](docs/DevicesManagementApi.md#get_statuses_history) | **GET** /devicemgmt/tasks/{tid}/statuses/history | Returns the history of the status changes for a specific task id, or for a specific device id in that task.
*DevicesManagementApi* | [**get_task_by_id**](docs/DevicesManagementApi.md#get_task_by_id) | **GET** /devicemgmt/tasks/{tid} | Returns the details and global status of a specific task id.
*DevicesManagementApi* | [**get_tasks**](docs/DevicesManagementApi.md#get_tasks) | **GET** /devicemgmt/tasks | Returns the all the tasks for a device type.
*DevicesManagementApi* | [**query_properties**](docs/DevicesManagementApi.md#query_properties) | **GET** /devicemgmt/devices/properties | Query device properties across devices.
*DevicesManagementApi* | [**update_device_types_info**](docs/DevicesManagementApi.md#update_device_types_info) | **PUT** /devicemgmt/devicetypes/{dtid} | Updates a device type information
*DevicesManagementApi* | [**update_server_properties**](docs/DevicesManagementApi.md#update_server_properties) | **POST** /devicemgmt/devices/{did}/serverproperties | Updates a device&#39;s server properties.
*DevicesManagementApi* | [**update_task**](docs/DevicesManagementApi.md#update_task) | **PUT** /devicemgmt/tasks/{tid} | Updates a task for all devices - For now just allows changing the state to cancelled.
*DevicesManagementApi* | [**update_task_for_device**](docs/DevicesManagementApi.md#update_task_for_device) | **PUT** /devicemgmt/tasks/{tid}/devices/{did} | Updates a task for a specific device - For now just allows changing the state to cancelled.
*DevicesSharesApi* | [**create_share_for_device**](docs/DevicesSharesApi.md#create_share_for_device) | **POST** /devices/{deviceId}/shares | Share a device 
*DevicesSharesApi* | [**delete_sharing_for_device**](docs/DevicesSharesApi.md#delete_sharing_for_device) | **DELETE** /devices/{deviceId}/shares/{shareId} | Delete specific share of the given device id
*DevicesSharesApi* | [**get_all_shares_for_device**](docs/DevicesSharesApi.md#get_all_shares_for_device) | **GET** /devices/{deviceId}/shares | List all shares for the given device id
*DevicesSharesApi* | [**get_sharing_for_device**](docs/DevicesSharesApi.md#get_sharing_for_device) | **GET** /devices/{deviceId}/shares/{shareId} | Get specific share of the given device id
*DevicesStatusApi* | [**get_device_status**](docs/DevicesStatusApi.md#get_device_status) | **GET** /devices/{deviceId}/status | Get Device Status
*DevicesStatusApi* | [**get_devices_status**](docs/DevicesStatusApi.md#get_devices_status) | **GET** /devices/status | Get Devices Status
*DevicesStatusApi* | [**put_device_status**](docs/DevicesStatusApi.md#put_device_status) | **PUT** /devices/{deviceId}/status | Update Device Status
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
*SubscriptionsApi* | [**create_subscription**](docs/SubscriptionsApi.md#create_subscription) | **POST** /subscriptions | Create Subscription
*SubscriptionsApi* | [**delete_subscription**](docs/SubscriptionsApi.md#delete_subscription) | **DELETE** /subscriptions/{subId} | Delete Subscription
*SubscriptionsApi* | [**get_all_subscriptions**](docs/SubscriptionsApi.md#get_all_subscriptions) | **GET** /subscriptions | Get All Subscriptions
*SubscriptionsApi* | [**get_messages**](docs/SubscriptionsApi.md#get_messages) | **GET** /notifications/{notifId}/messages | Get Messages
*SubscriptionsApi* | [**get_subscription**](docs/SubscriptionsApi.md#get_subscription) | **GET** /subscriptions/{subId} | Get Subscription
*SubscriptionsApi* | [**validate_subscription**](docs/SubscriptionsApi.md#validate_subscription) | **POST** /subscriptions/{subId}/validate | Validate Subscription
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
*UsersApi* | [**list_all_shares_for_user**](docs/UsersApi.md#list_all_shares_for_user) | **GET** /users/{userId}/shares | Get User shares
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
 - [DeviceShareInfo](docs/DeviceShareInfo.md)
 - [DeviceSharing](docs/DeviceSharing.md)
 - [DeviceSharingArray](docs/DeviceSharingArray.md)
 - [DeviceSharingEnvelope](docs/DeviceSharingEnvelope.md)
 - [DeviceSharingId](docs/DeviceSharingId.md)
 - [DeviceStatus](docs/DeviceStatus.md)
 - [DeviceStatusBatch](docs/DeviceStatusBatch.md)
 - [DeviceStatusData](docs/DeviceStatusData.md)
 - [DeviceStatusPut](docs/DeviceStatusPut.md)
 - [DeviceStatusPutData](docs/DeviceStatusPutData.md)
 - [DeviceTask](docs/DeviceTask.md)
 - [DeviceTaskUpdateRequest](docs/DeviceTaskUpdateRequest.md)
 - [DeviceTaskUpdateResponse](docs/DeviceTaskUpdateResponse.md)
 - [DeviceToken](docs/DeviceToken.md)
 - [DeviceTokenEnvelope](docs/DeviceTokenEnvelope.md)
 - [DeviceType](docs/DeviceType.md)
 - [DeviceTypeArray](docs/DeviceTypeArray.md)
 - [DeviceTypeEnvelope](docs/DeviceTypeEnvelope.md)
 - [DeviceTypeInfo](docs/DeviceTypeInfo.md)
 - [DeviceTypeInfoEnvelope](docs/DeviceTypeInfoEnvelope.md)
 - [DeviceTypesEnvelope](docs/DeviceTypesEnvelope.md)
 - [DeviceTypesInfo](docs/DeviceTypesInfo.md)
 - [DeviceTypesInfoEnvelope](docs/DeviceTypesInfoEnvelope.md)
 - [DevicesEnvelope](docs/DevicesEnvelope.md)
 - [ErrorEnvelope](docs/ErrorEnvelope.md)
 - [EventFeedData](docs/EventFeedData.md)
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
 - [MetadataEnvelope](docs/MetadataEnvelope.md)
 - [MetadataPropertiesEnvelope](docs/MetadataPropertiesEnvelope.md)
 - [MetadataQueryEnvelope](docs/MetadataQueryEnvelope.md)
 - [NonEmptyString](docs/NonEmptyString.md)
 - [NormalizedAction](docs/NormalizedAction.md)
 - [NormalizedActionsEnvelope](docs/NormalizedActionsEnvelope.md)
 - [NormalizedMessage](docs/NormalizedMessage.md)
 - [NormalizedMessagesEnvelope](docs/NormalizedMessagesEnvelope.md)
 - [NotifMessage](docs/NotifMessage.md)
 - [NotifMessageArray](docs/NotifMessageArray.md)
 - [NotifMessagesResponse](docs/NotifMessagesResponse.md)
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
 - [Subscription](docs/Subscription.md)
 - [SubscriptionArray](docs/SubscriptionArray.md)
 - [SubscriptionEnvelope](docs/SubscriptionEnvelope.md)
 - [SubscriptionInfo](docs/SubscriptionInfo.md)
 - [SubscriptionsEnvelope](docs/SubscriptionsEnvelope.md)
 - [Tag](docs/Tag.md)
 - [TagArray](docs/TagArray.md)
 - [TagsEnvelope](docs/TagsEnvelope.md)
 - [Task](docs/Task.md)
 - [TaskByDid](docs/TaskByDid.md)
 - [TaskByDidList](docs/TaskByDidList.md)
 - [TaskByDidListEnvelope](docs/TaskByDidListEnvelope.md)
 - [TaskEnvelope](docs/TaskEnvelope.md)
 - [TaskHistory](docs/TaskHistory.md)
 - [TaskHistoryList](docs/TaskHistoryList.md)
 - [TaskList](docs/TaskList.md)
 - [TaskListEnvelope](docs/TaskListEnvelope.md)
 - [TaskParameters](docs/TaskParameters.md)
 - [TaskRequest](docs/TaskRequest.md)
 - [TaskStatus](docs/TaskStatus.md)
 - [TaskStatusCounts](docs/TaskStatusCounts.md)
 - [TaskStatuses](docs/TaskStatuses.md)
 - [TaskStatusesEnvelope](docs/TaskStatusesEnvelope.md)
 - [TaskStatusesHistoryEnvelope](docs/TaskStatusesHistoryEnvelope.md)
 - [TaskUpdateRequest](docs/TaskUpdateRequest.md)
 - [TaskUpdateResponse](docs/TaskUpdateResponse.md)
 - [TasksStatusCounts](docs/TasksStatusCounts.md)
 - [Token](docs/Token.md)
 - [TokenInfo](docs/TokenInfo.md)
 - [TokenInfoSuccessResponse](docs/TokenInfoSuccessResponse.md)
 - [TokenRequest](docs/TokenRequest.md)
 - [TokenResponse](docs/TokenResponse.md)
 - [UnregisterDeviceResponse](docs/UnregisterDeviceResponse.md)
 - [UnregisterDeviceResponseEnvelope](docs/UnregisterDeviceResponseEnvelope.md)
 - [UpdateParameters](docs/UpdateParameters.md)
 - [User](docs/User.md)
 - [UserEnvelope](docs/UserEnvelope.md)
 - [ValidationCallbackInfo](docs/ValidationCallbackInfo.md)
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

Copyright (c) 2017 Samsung Electronics Co., Ltd.

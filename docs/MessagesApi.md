# artikcloud.MessagesApi

All URIs are relative to *https://api.artik.cloud/v1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aggregates_histogram**](MessagesApi.md#get_aggregates_histogram) | **GET** /messages/analytics/histogram | Get Normalized Message Histogram
[**get_field_presence**](MessagesApi.md#get_field_presence) | **GET** /messages/presence | Get normalized message presence
[**get_last_normalized_messages**](MessagesApi.md#get_last_normalized_messages) | **GET** /messages/last | Get Last Normalized Message
[**get_message_aggregates**](MessagesApi.md#get_message_aggregates) | **GET** /messages/analytics/aggregates | Get Normalized Message Aggregates
[**get_message_snapshots**](MessagesApi.md#get_message_snapshots) | **GET** /messages/snapshots | Get Message Snapshots
[**get_normalized_messages**](MessagesApi.md#get_normalized_messages) | **GET** /messages | Get Normalized Messages
[**send_message_action**](MessagesApi.md#send_message_action) | **POST** /messages | Send Message Action


# **get_aggregates_histogram**
> AggregatesHistogramResponse get_aggregates_histogram(start_date, end_date, sdid=sdid, field=field, interval=interval)

Get Normalized Message Histogram

Get Histogram on normalized messages.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
start_date = 789 # int | Timestamp of earliest message (in milliseconds since epoch).
end_date = 789 # int | Timestamp of latest message (in milliseconds since epoch).
sdid = 'sdid_example' # str | Source device ID of the messages being searched. (optional)
field = 'field_example' # str | Message field being queried for building histogram. (optional)
interval = 'interval_example' # str | Interval of time for building histogram blocks. (Valid values: minute, hour, day, month, year) (optional)

try: 
    # Get Normalized Message Histogram
    api_response = api_instance.get_aggregates_histogram(start_date, end_date, sdid=sdid, field=field, interval=interval)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_aggregates_histogram: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| Timestamp of earliest message (in milliseconds since epoch). | 
 **end_date** | **int**| Timestamp of latest message (in milliseconds since epoch). | 
 **sdid** | **str**| Source device ID of the messages being searched. | [optional] 
 **field** | **str**| Message field being queried for building histogram. | [optional] 
 **interval** | **str**| Interval of time for building histogram blocks. (Valid values: minute, hour, day, month, year) | [optional] 

### Return type

[**AggregatesHistogramResponse**](AggregatesHistogramResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_presence**
> FieldPresenceEnvelope get_field_presence(start_date, end_date, interval, sdid=sdid, field_presence=field_presence)

Get normalized message presence

Get normalized message presence.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
start_date = 789 # int | startDate
end_date = 789 # int | endDate
interval = 'interval_example' # str | String representing grouping interval. One of: 'minute' (1 hour limit), 'hour' (1 day limit), 'day' (31 days limit), 'month' (1 year limit), or 'year' (10 years limit).
sdid = 'sdid_example' # str | Source device ID of the messages being searched. (optional)
field_presence = 'field_presence_example' # str | String representing a field from the specified device ID. (optional)

try: 
    # Get normalized message presence
    api_response = api_instance.get_field_presence(start_date, end_date, interval, sdid=sdid, field_presence=field_presence)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_field_presence: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **int**| startDate | 
 **end_date** | **int**| endDate | 
 **interval** | **str**| String representing grouping interval. One of: &#39;minute&#39; (1 hour limit), &#39;hour&#39; (1 day limit), &#39;day&#39; (31 days limit), &#39;month&#39; (1 year limit), or &#39;year&#39; (10 years limit). | 
 **sdid** | **str**| Source device ID of the messages being searched. | [optional] 
 **field_presence** | **str**| String representing a field from the specified device ID. | [optional] 

### Return type

[**FieldPresenceEnvelope**](FieldPresenceEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_last_normalized_messages**
> NormalizedMessagesEnvelope get_last_normalized_messages(count=count, sdids=sdids, field_presence=field_presence)

Get Last Normalized Message

Get last messages normalized.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
count = 56 # int | Number of items to return per query. (optional)
sdids = 'sdids_example' # str | Comma separated list of source device IDs (minimum: 1). (optional)
field_presence = 'field_presence_example' # str | String representing a field from the specified device ID. (optional)

try: 
    # Get Last Normalized Message
    api_response = api_instance.get_last_normalized_messages(count=count, sdids=sdids, field_presence=field_presence)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_last_normalized_messages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| Number of items to return per query. | [optional] 
 **sdids** | **str**| Comma separated list of source device IDs (minimum: 1). | [optional] 
 **field_presence** | **str**| String representing a field from the specified device ID. | [optional] 

### Return type

[**NormalizedMessagesEnvelope**](NormalizedMessagesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_aggregates**
> AggregatesResponse get_message_aggregates(sdid, field, start_date, end_date)

Get Normalized Message Aggregates

Get Aggregates on normalized messages.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
sdid = 'sdid_example' # str | Source device ID of the messages being searched.
field = 'field_example' # str | Message field being queried for aggregates.
start_date = 789 # int | Timestamp of earliest message (in milliseconds since epoch).
end_date = 789 # int | Timestamp of latest message (in milliseconds since epoch).

try: 
    # Get Normalized Message Aggregates
    api_response = api_instance.get_message_aggregates(sdid, field, start_date, end_date)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_message_aggregates: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdid** | **str**| Source device ID of the messages being searched. | 
 **field** | **str**| Message field being queried for aggregates. | 
 **start_date** | **int**| Timestamp of earliest message (in milliseconds since epoch). | 
 **end_date** | **int**| Timestamp of latest message (in milliseconds since epoch). | 

### Return type

[**AggregatesResponse**](AggregatesResponse.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message_snapshots**
> SnapshotResponses get_message_snapshots(sdids, include_timestamp=include_timestamp)

Get Message Snapshots

Get message snapshots.

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
sdids = 'sdids_example' # str | Device IDs for which the snapshots are requested. Max 100 device ids per call.
include_timestamp = true # bool | Indicates whether to return timestamps of the last update for each field. (optional)

try: 
    # Get Message Snapshots
    api_response = api_instance.get_message_snapshots(sdids, include_timestamp=include_timestamp)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_message_snapshots: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sdids** | **str**| Device IDs for which the snapshots are requested. Max 100 device ids per call. | 
 **include_timestamp** | **bool**| Indicates whether to return timestamps of the last update for each field. | [optional] 

### Return type

[**SnapshotResponses**](SnapshotResponses.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_normalized_messages**
> NormalizedMessagesEnvelope get_normalized_messages(uid=uid, sdid=sdid, mid=mid, field_presence=field_presence, filter=filter, offset=offset, count=count, start_date=start_date, end_date=end_date, order=order)

Get Normalized Messages

Get the messages normalized

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
uid = 'uid_example' # str | User ID. If not specified, assume that of the current authenticated user. If specified, it must be that of a user for which the current authenticated user has read access to. (optional)
sdid = 'sdid_example' # str | Source device ID of the messages being searched. (optional)
mid = 'mid_example' # str | The SAMI message ID being searched. (optional)
field_presence = 'field_presence_example' # str | String representing a field from the specified device ID. (optional)
filter = 'filter_example' # str | Filter. (optional)
offset = 'offset_example' # str | A string that represents the starting item, should be the value of 'next' field received in the last response. (required for pagination) (optional)
count = 56 # int | count (optional)
start_date = 789 # int | startDate (optional)
end_date = 789 # int | endDate (optional)
order = 'order_example' # str | Desired sort order: 'asc' or 'desc' (optional)

try: 
    # Get Normalized Messages
    api_response = api_instance.get_normalized_messages(uid=uid, sdid=sdid, mid=mid, field_presence=field_presence, filter=filter, offset=offset, count=count, start_date=start_date, end_date=end_date, order=order)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->get_normalized_messages: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**| User ID. If not specified, assume that of the current authenticated user. If specified, it must be that of a user for which the current authenticated user has read access to. | [optional] 
 **sdid** | **str**| Source device ID of the messages being searched. | [optional] 
 **mid** | **str**| The SAMI message ID being searched. | [optional] 
 **field_presence** | **str**| String representing a field from the specified device ID. | [optional] 
 **filter** | **str**| Filter. | [optional] 
 **offset** | **str**| A string that represents the starting item, should be the value of &#39;next&#39; field received in the last response. (required for pagination) | [optional] 
 **count** | **int**| count | [optional] 
 **start_date** | **int**| startDate | [optional] 
 **end_date** | **int**| endDate | [optional] 
 **order** | **str**| Desired sort order: &#39;asc&#39; or &#39;desc&#39; | [optional] 

### Return type

[**NormalizedMessagesEnvelope**](NormalizedMessagesEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_message_action**
> MessageIDEnvelope send_message_action(data)

Send Message Action

(Deprecated) Send a message or an Action:<br/><table><tr><th>Combination</th><th>Parameters</th><th>Description</th></tr><tr><td>Send Message</td><td>sdid, type=message</td><td>Send a message from a Source Device</td></tr><tr><td>Send Action</td><td>ddid, type=action</td><td>Send an action to a Destination Device</td></tr><tr><td>Common</td><td>data, ts, token</td><td>Parameters that can be used with the above combinations.</td></tr></table>

### Example 
```python
import time
import artikcloud
from artikcloud.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: artikcloud_oauth
artikcloud.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = artikcloud.MessagesApi()
data = artikcloud.MessageAction() # MessageAction | Message or Action object that is passed in the body

try: 
    # Send Message Action
    api_response = api_instance.send_message_action(data)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagesApi->send_message_action: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**MessageAction**](MessageAction.md)| Message or Action object that is passed in the body | 

### Return type

[**MessageIDEnvelope**](MessageIDEnvelope.md)

### Authorization

[artikcloud_oauth](../README.md#artikcloud_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# SubscriptionInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_region** | **str** | AWS region (if subscriptionType is awsKinesis | [optional] 
**description** | **str** | Description | [optional] 
**aws_key** | **str** | AWS key (if subscriptionType is awsKinesis | [optional] 
**aws_secret** | **str** | AWS secret (if subscriptionType is awsKinesis | [optional] 
**aws_kinesis_stream_name** | **str** | AWS Kinesis stream name (if subscriptionType is awsKinesis | [optional] 
**uid** | **str** | User ID | [optional] 
**message_type** | **str** | Message type | [optional] 
**ddid** | **str** | Destination device ID | [optional] 
**subscription_type** | **str** | Subscription type (either httpCallback or awsKinesis, default to httpCallback) | [optional] 
**name** | **str** | Name | [optional] 
**sdid** | **str** | Source device ID | [optional] 
**callback_url** | **str** | Callback URL | [optional] 
**sdtid** | **str** | Source device type ID | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



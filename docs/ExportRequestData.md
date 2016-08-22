# ExportRequestData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv_headers** | **bool** | Add header to csv format | [optional] 
**end_date** | **int** | Timestamp of latest message (in milliseconds since epoch). | [optional] 
**export_id** | **str** | Returned Export ID that should be used to check status and get the export result. | [optional] 
**format** | **str** | Format of the export. | [optional] 
**order** | **str** | Ascending or descending sort order. | [optional] 
**sdids** | **str** | Source Device IDs being searched for messages (Comma-separated for multiple Device IDs). | [optional] 
**sdtids** | **str** | Source Device Type IDs being searched for messages (Comma-separated for multiple Device Type IDs). | [optional] 
**start_date** | **int** | Timestamp of earliest message (in milliseconds since epoch). | [optional] 
**trial_id** | **str** | Trial ID being searched for messages. | [optional] 
**uids** | **str** | Owner&#39;s user IDs being searched for messages (Comma-separated for multiple User IDs). | [optional] 
**url** | **str** | URL added to successful email message. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



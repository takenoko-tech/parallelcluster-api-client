# openapi_client.model.log_stream.LogStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**logStreamArn** | str,  | str,  | The Amazon Resource Name (ARN) of the log stream. | 
**creationTime** | str, datetime,  | str,  | The creation time of the stream. | value must conform to RFC-3339 date-time
**firstEventTimestamp** | str, datetime,  | str,  | The time of the first event of the stream. | value must conform to RFC-3339 date-time
**logStreamName** | str,  | str,  | Name of the log stream. | 
**lastEventTimestamp** | str, datetime,  | str,  | The time of the last event of the stream. The lastEventTime value updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer. | value must conform to RFC-3339 date-time
**lastIngestionTime** | str, datetime,  | str,  | The last ingestion time. | value must conform to RFC-3339 date-time
**uploadSequenceToken** | str,  | str,  | The sequence token. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


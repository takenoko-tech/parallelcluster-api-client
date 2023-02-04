# openapi_client.model.cluster_instance.ClusterInstance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**launchTime** | str, datetime,  | str,  |  | value must conform to RFC-3339 date-time
**instanceId** | str,  | str,  |  | 
**instanceType** | str,  | str,  |  | 
**state** | [**InstanceState**](InstanceState.md) | [**InstanceState**](InstanceState.md) |  | 
**nodeType** | [**NodeType**](NodeType.md) | [**NodeType**](NodeType.md) |  | 
**privateIpAddress** | str,  | str,  |  | 
**publicIpAddress** | str,  | str,  |  | [optional] 
**queueName** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


# openapi_client.model.stack_event.StackEvent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eventId** | str,  | str,  | The unique ID of this event. | 
**physicalResourceId** | str,  | str,  | The name or unique identifier associated with the physical instance of the resource. | 
**resourceStatus** | [**CloudFormationResourceStatus**](CloudFormationResourceStatus.md) | [**CloudFormationResourceStatus**](CloudFormationResourceStatus.md) |  | 
**stackId** | str,  | str,  | The unique ID name of the instance of the stack. | 
**stackName** | str,  | str,  | The name associated with a stack. | 
**logicalResourceId** | str,  | str,  | The logical name of the resource specified in the template. | 
**resourceType** | str,  | str,  | Type of resource. | 
**timestamp** | str, datetime,  | str,  | Time the status was updated. | value must conform to RFC-3339 date-time
**resourceStatusReason** | str,  | str,  | Success/failure message associated with the resource. | [optional] 
**resourceProperties** | str,  | str,  | BLOB of the properties used to create the resource. | [optional] 
**clientRequestToken** | str,  | str,  | The token passed to the operation that generated this event. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


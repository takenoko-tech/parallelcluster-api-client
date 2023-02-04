# openapi_client.model.update_cluster_bad_request_exception_response_content.UpdateClusterBadRequestExceptionResponseContent

This exception is thrown when a client calls the UpdateCluster API with an invalid request. This includes an error due to invalid cluster configuration and unsupported update.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | This exception is thrown when a client calls the UpdateCluster API with an invalid request. This includes an error due to invalid cluster configuration and unsupported update. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**message** | str,  | str,  |  | [optional] 
**[configurationValidationErrors](#configurationValidationErrors)** | list, tuple,  | tuple,  |  | [optional] 
**[updateValidationErrors](#updateValidationErrors)** | list, tuple,  | tuple,  |  | [optional] 
**[changeSet](#changeSet)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# configurationValidationErrors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConfigValidationMessage**](ConfigValidationMessage.md) | [**ConfigValidationMessage**](ConfigValidationMessage.md) | [**ConfigValidationMessage**](ConfigValidationMessage.md) |  | 

# updateValidationErrors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UpdateError**](UpdateError.md) | [**UpdateError**](UpdateError.md) | [**UpdateError**](UpdateError.md) |  | 

# changeSet

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Change**](Change.md) | [**Change**](Change.md) | [**Change**](Change.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


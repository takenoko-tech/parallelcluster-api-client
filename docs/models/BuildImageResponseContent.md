# openapi_client.model.build_image_response_content.BuildImageResponseContent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**image** | [**ImageInfoSummary**](ImageInfoSummary.md) | [**ImageInfoSummary**](ImageInfoSummary.md) |  | 
**[validationMessages](#validationMessages)** | list, tuple,  | tuple,  | List of messages collected during image config validation whose level is lower than the &#x27;validationFailureLevel&#x27; set by the user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# validationMessages

List of messages collected during image config validation whose level is lower than the 'validationFailureLevel' set by the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of messages collected during image config validation whose level is lower than the &#x27;validationFailureLevel&#x27; set by the user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConfigValidationMessage**](ConfigValidationMessage.md) | [**ConfigValidationMessage**](ConfigValidationMessage.md) | [**ConfigValidationMessage**](ConfigValidationMessage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


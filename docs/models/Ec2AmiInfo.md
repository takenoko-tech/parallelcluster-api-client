# openapi_client.model.ec2_ami_info.Ec2AmiInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amiId** | str,  | str,  | EC2 AMI id | 
**[tags](#tags)** | list, tuple,  | tuple,  | EC2 AMI Tags | [optional] 
**amiName** | str,  | str,  | EC2 AMI name | [optional] 
**architecture** | str,  | str,  | EC2 AMI architecture | [optional] 
**state** | [**Ec2AmiState**](Ec2AmiState.md) | [**Ec2AmiState**](Ec2AmiState.md) |  | [optional] 
**description** | str,  | str,  | EC2 AMI description | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

EC2 AMI Tags

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | EC2 AMI Tags | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](Tag.md) | [**Tag**](Tag.md) | [**Tag**](Tag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


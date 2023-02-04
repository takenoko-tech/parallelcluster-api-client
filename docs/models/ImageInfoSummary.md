# openapi_client.model.image_info_summary.ImageInfoSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**imageId** | str,  | str,  | Id of the image. | 
**imageBuildStatus** | [**ImageBuildStatus**](ImageBuildStatus.md) | [**ImageBuildStatus**](ImageBuildStatus.md) |  | 
**region** | str,  | str,  | AWS region where the image is built. | 
**version** | str,  | str,  | ParallelCluster version used to build the image. | 
**ec2AmiInfo** | [**Ec2AmiInfoSummary**](Ec2AmiInfoSummary.md) | [**Ec2AmiInfoSummary**](Ec2AmiInfoSummary.md) |  | [optional] 
**cloudformationStackArn** | str,  | str,  | ARN of the main CloudFormation stack. | [optional] 
**cloudformationStackStatus** | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


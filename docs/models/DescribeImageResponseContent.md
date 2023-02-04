# openapi_client.model.describe_image_response_content.DescribeImageResponseContent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**imageConfiguration** | [**ImageConfigurationStructure**](ImageConfigurationStructure.md) | [**ImageConfigurationStructure**](ImageConfigurationStructure.md) |  | 
**imageId** | str,  | str,  | Id of the Image to retrieve detailed information for. | 
**imageBuildStatus** | [**ImageBuildStatus**](ImageBuildStatus.md) | [**ImageBuildStatus**](ImageBuildStatus.md) |  | 
**region** | str,  | str,  | AWS region where the image is created. | 
**version** | str,  | str,  | ParallelCluster version used to build the image. | 
**imageBuildLogsArn** | str,  | str,  | ARN of the logs for the image build process. | [optional] 
**cloudformationStackStatus** | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) |  | [optional] 
**cloudformationStackStatusReason** | str,  | str,  | Reason for the CloudFormation stack status. | [optional] 
**cloudformationStackArn** | str,  | str,  | ARN of the main CloudFormation stack. | [optional] 
**creationTime** | str, datetime,  | str,  | Timestamp representing the image creation time. | [optional] value must conform to RFC-3339 date-time
**cloudformationStackCreationTime** | str, datetime,  | str,  | Timestamp representing the CloudFormation stack creation time. | [optional] value must conform to RFC-3339 date-time
**[cloudformationStackTags](#cloudformationStackTags)** | list, tuple,  | tuple,  | Tags for the CloudFormation stack. | [optional] 
**imagebuilderImageStatus** | [**ImageBuilderImageStatus**](ImageBuilderImageStatus.md) | [**ImageBuilderImageStatus**](ImageBuilderImageStatus.md) |  | [optional] 
**imagebuilderImageStatusReason** | str,  | str,  | Reason for the ImageBuilder Image status. | [optional] 
**ec2AmiInfo** | [**Ec2AmiInfo**](Ec2AmiInfo.md) | [**Ec2AmiInfo**](Ec2AmiInfo.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# cloudformationStackTags

Tags for the CloudFormation stack.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags for the CloudFormation stack. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](Tag.md) | [**Tag**](Tag.md) | [**Tag**](Tag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


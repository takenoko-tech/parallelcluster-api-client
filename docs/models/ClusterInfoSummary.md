# openapi_client.model.cluster_info_summary.ClusterInfoSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Name of the cluster. | 
**cloudformationStackStatus** | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) |  | 
**cloudformationStackArn** | str,  | str,  | ARN of the main CloudFormation stack. | 
**region** | str,  | str,  | AWS region where the cluster is created. | 
**version** | str,  | str,  | ParallelCluster version used to create the cluster. | 
**clusterStatus** | [**ClusterStatus**](ClusterStatus.md) | [**ClusterStatus**](ClusterStatus.md) |  | 
**scheduler** | [**Scheduler**](Scheduler.md) | [**Scheduler**](Scheduler.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


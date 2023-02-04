# openapi_client.model.describe_cluster_response_content.DescribeClusterResponseContent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**creationTime** | str, datetime,  | str,  | Timestamp representing the cluster creation time. | value must conform to RFC-3339 date-time
**cloudFormationStackStatus** | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) | [**CloudFormationStackStatus**](CloudFormationStackStatus.md) |  | 
**clusterName** | str,  | str,  | Name of the cluster. | 
**computeFleetStatus** | [**ComputeFleetStatus**](ComputeFleetStatus.md) | [**ComputeFleetStatus**](ComputeFleetStatus.md) |  | 
**cloudformationStackArn** | str,  | str,  | ARN of the main CloudFormation stack. | 
**lastUpdatedTime** | str, datetime,  | str,  | Timestamp representing the last cluster update time. | value must conform to RFC-3339 date-time
**region** | str,  | str,  | AWS region where the cluster is created. | 
**version** | str,  | str,  | ParallelCluster version used to create the cluster. | 
**clusterConfiguration** | [**ClusterConfigurationStructure**](ClusterConfigurationStructure.md) | [**ClusterConfigurationStructure**](ClusterConfigurationStructure.md) |  | 
**clusterStatus** | [**ClusterStatus**](ClusterStatus.md) | [**ClusterStatus**](ClusterStatus.md) |  | 
**[tags](#tags)** | list, tuple,  | tuple,  | Tags associated with the cluster. | 
**scheduler** | [**Scheduler**](Scheduler.md) | [**Scheduler**](Scheduler.md) |  | [optional] 
**headNode** | [**EC2Instance**](EC2Instance.md) | [**EC2Instance**](EC2Instance.md) |  | [optional] 
**failureReason** | str,  | str,  | Reason of the failure when the stack is in CREATE_FAILED, UPDATE_FAILED or DELETE_FAILED status. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tags

Tags associated with the cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Tags associated with the cluster. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Tag**](Tag.md) | [**Tag**](Tag.md) | [**Tag**](Tag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)


<a name="__pageTop"></a>
# openapi_client.apis.tags.cluster_instances_api.ClusterInstancesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cluster_instances**](#delete_cluster_instances) | **delete** /v3/clusters/{clusterName}/instances | 
[**describe_cluster_instances**](#describe_cluster_instances) | **get** /v3/clusters/{clusterName}/instances | 

# **delete_cluster_instances**
<a name="delete_cluster_instances"></a>
> delete_cluster_instances(cluster_name)



Initiate the forced termination of all cluster compute nodes. Does not work with AWS Batch clusters.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_instances_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.not_found_exception_response_content import NotFoundExceptionResponseContent
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws.auth.sigv4
configuration.api_key['aws.auth.sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws.auth.sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_instances_api.ClusterInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_cluster_instances(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterInstancesApi->delete_cluster_instances: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
        'force': True,
    }
    try:
        api_response = api_instance.delete_cluster_instances(
            path_params=path_params,
            query_params=query_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterInstancesApi->delete_cluster_instances: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
region | RegionSchema | | optional
force | ForceSchema | | optional


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

# ForceSchema

Force the deletion also when the cluster with the given name is not found. (Defaults to 'false'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Force the deletion also when the cluster with the given name is not found. (Defaults to &#x27;false&#x27;.) | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
clusterName | ClusterNameSchema | | 

# ClusterNameSchema

Name of the cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Name of the cluster | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#delete_cluster_instances.ApiResponseFor202) | DeleteClusterInstances 202 response
400 | [ApiResponseFor400](#delete_cluster_instances.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#delete_cluster_instances.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#delete_cluster_instances.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#delete_cluster_instances.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#delete_cluster_instances.ApiResponseFor500) | InternalServiceException 500 response

#### delete_cluster_instances.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_cluster_instances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### delete_cluster_instances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### delete_cluster_instances.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### delete_cluster_instances.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### delete_cluster_instances.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServiceExceptionResponseContent**](../../models/InternalServiceExceptionResponseContent.md) |  | 


### Authorization

[aws.auth.sigv4](../../../README.md#aws.auth.sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **describe_cluster_instances**
<a name="describe_cluster_instances"></a>
> DescribeClusterInstancesResponseContent describe_cluster_instances(cluster_name)



Describe the instances belonging to a given cluster.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_instances_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.node_type import NodeType
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.describe_cluster_instances_response_content import DescribeClusterInstancesResponseContent
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: aws.auth.sigv4
configuration.api_key['aws.auth.sigv4'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['aws.auth.sigv4'] = 'Bearer'
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cluster_instances_api.ClusterInstancesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.describe_cluster_instances(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterInstancesApi->describe_cluster_instances: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
        'nextToken': "nextToken_example",
        'nodeType': NodeType("HeadNode"),
        'queueName': "queueName_example",
    }
    try:
        api_response = api_instance.describe_cluster_instances(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterInstancesApi->describe_cluster_instances: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
region | RegionSchema | | optional
nextToken | NextTokenSchema | | optional
nodeType | NodeTypeSchema | | optional
queueName | QueueNameSchema | | optional


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

# NextTokenSchema

Token to use for paginated requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to use for paginated requests. | 

# NodeTypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**NodeType**](../../models/NodeType.md) |  | 


# QueueNameSchema

Filter the instances by queue name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Filter the instances by queue name. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
clusterName | ClusterNameSchema | | 

# ClusterNameSchema

Name of the cluster

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Name of the cluster | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#describe_cluster_instances.ApiResponseFor200) | DescribeClusterInstances 200 response
400 | [ApiResponseFor400](#describe_cluster_instances.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#describe_cluster_instances.ApiResponseFor401) | UnauthorizedClientError 401 response
429 | [ApiResponseFor429](#describe_cluster_instances.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#describe_cluster_instances.ApiResponseFor500) | InternalServiceException 500 response

#### describe_cluster_instances.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DescribeClusterInstancesResponseContent**](../../models/DescribeClusterInstancesResponseContent.md) |  | 


#### describe_cluster_instances.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### describe_cluster_instances.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### describe_cluster_instances.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### describe_cluster_instances.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**InternalServiceExceptionResponseContent**](../../models/InternalServiceExceptionResponseContent.md) |  | 


### Authorization

[aws.auth.sigv4](../../../README.md#aws.auth.sigv4)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)


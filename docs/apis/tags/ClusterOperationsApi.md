<a name="__pageTop"></a>
# openapi_client.apis.tags.cluster_operations_api.ClusterOperationsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](#create_cluster) | **post** /v3/clusters | 
[**delete_cluster**](#delete_cluster) | **delete** /v3/clusters/{clusterName} | 
[**describe_cluster**](#describe_cluster) | **get** /v3/clusters/{clusterName} | 
[**list_clusters**](#list_clusters) | **get** /v3/clusters | 
[**update_cluster**](#update_cluster) | **put** /v3/clusters/{clusterName} | 

# **create_cluster**
<a name="create_cluster"></a>
> CreateClusterResponseContent create_cluster(create_cluster_request_content)



Create a managed cluster in a given region.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_operations_api
from openapi_client.model.create_cluster_request_content import CreateClusterRequestContent
from openapi_client.model.conflict_exception_response_content import ConflictExceptionResponseContent
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.dryrun_operation_exception_response_content import DryrunOperationExceptionResponseContent
from openapi_client.model.validation_level import ValidationLevel
from openapi_client.model.create_cluster_bad_request_exception_response_content import CreateClusterBadRequestExceptionResponseContent
from openapi_client.model.create_cluster_response_content import CreateClusterResponseContent
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
    api_instance = cluster_operations_api.ClusterOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = CreateClusterRequestContent(
        cluster_name="AqWzyB",
        cluster_configuration="cluster_configuration_example",
    )
    try:
        api_response = api_instance.create_cluster(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->create_cluster: %s\n" % e)

    # example passing only optional values
    query_params = {
        'region': "region_example",
        'suppressValidators': [
        "type:u2LC4"
    ],
        'validationFailureLevel': ValidationLevel("INFO"),
        'dryrun': True,
        'rollbackOnFailure': True,
    }
    body = CreateClusterRequestContent(
        cluster_name="AqWzyB",
        cluster_configuration="cluster_configuration_example",
    )
    try:
        api_response = api_instance.create_cluster(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->create_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateClusterRequestContent**](../../models/CreateClusterRequestContent.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
region | RegionSchema | | optional
suppressValidators | SuppressValidatorsSchema | | optional
validationFailureLevel | ValidationFailureLevelSchema | | optional
dryrun | DryrunSchema | | optional
rollbackOnFailure | RollbackOnFailureSchema | | optional


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

# SuppressValidatorsSchema

Identifies one or more config validators to suppress. Format: (ALL|type:[A-Za-z0-9]+)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifies one or more config validators to suppress. Format: (ALL|type:[A-Za-z0-9]+) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ValidationFailureLevelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationLevel**](../../models/ValidationLevel.md) |  | 


# DryrunSchema

Only perform request validation without creating any resource. May be used to validate the cluster configuration. (Defaults to 'false'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Only perform request validation without creating any resource. May be used to validate the cluster configuration. (Defaults to &#x27;false&#x27;.) | 

# RollbackOnFailureSchema

When set it automatically initiates a cluster stack rollback on failures. (Defaults to 'true'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | When set it automatically initiates a cluster stack rollback on failures. (Defaults to &#x27;true&#x27;.) | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#create_cluster.ApiResponseFor202) | CreateCluster 202 response
400 | [ApiResponseFor400](#create_cluster.ApiResponseFor400) | CreateClusterBadRequestException 400 response
401 | [ApiResponseFor401](#create_cluster.ApiResponseFor401) | UnauthorizedClientError 401 response
409 | [ApiResponseFor409](#create_cluster.ApiResponseFor409) | ConflictException 409 response
412 | [ApiResponseFor412](#create_cluster.ApiResponseFor412) | DryrunOperationException 412 response
429 | [ApiResponseFor429](#create_cluster.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#create_cluster.ApiResponseFor500) | InternalServiceException 500 response

#### create_cluster.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateClusterResponseContent**](../../models/CreateClusterResponseContent.md) |  | 


#### create_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateClusterBadRequestExceptionResponseContent**](../../models/CreateClusterBadRequestExceptionResponseContent.md) |  | 


#### create_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### create_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictExceptionResponseContent**](../../models/ConflictExceptionResponseContent.md) |  | 


#### create_cluster.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DryrunOperationExceptionResponseContent**](../../models/DryrunOperationExceptionResponseContent.md) |  | 


#### create_cluster.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### create_cluster.ApiResponseFor500
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

# **delete_cluster**
<a name="delete_cluster"></a>
> DeleteClusterResponseContent delete_cluster(cluster_name)



Initiate the deletion of a cluster.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_operations_api
from openapi_client.model.delete_cluster_response_content import DeleteClusterResponseContent
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
    api_instance = cluster_operations_api.ClusterOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.delete_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->delete_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
    }
    try:
        api_response = api_instance.delete_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->delete_cluster: %s\n" % e)
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


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

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
202 | [ApiResponseFor202](#delete_cluster.ApiResponseFor202) | DeleteCluster 202 response
400 | [ApiResponseFor400](#delete_cluster.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#delete_cluster.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#delete_cluster.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#delete_cluster.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#delete_cluster.ApiResponseFor500) | InternalServiceException 500 response

#### delete_cluster.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteClusterResponseContent**](../../models/DeleteClusterResponseContent.md) |  | 


#### delete_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### delete_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### delete_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### delete_cluster.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### delete_cluster.ApiResponseFor500
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

# **describe_cluster**
<a name="describe_cluster"></a>
> DescribeClusterResponseContent describe_cluster(cluster_name)



Get detailed information about an existing cluster.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_operations_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.describe_cluster_response_content import DescribeClusterResponseContent
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
    api_instance = cluster_operations_api.ClusterOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.describe_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->describe_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
    }
    try:
        api_response = api_instance.describe_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->describe_cluster: %s\n" % e)
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


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

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
200 | [ApiResponseFor200](#describe_cluster.ApiResponseFor200) | DescribeCluster 200 response
400 | [ApiResponseFor400](#describe_cluster.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#describe_cluster.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#describe_cluster.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#describe_cluster.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#describe_cluster.ApiResponseFor500) | InternalServiceException 500 response

#### describe_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DescribeClusterResponseContent**](../../models/DescribeClusterResponseContent.md) |  | 


#### describe_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### describe_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### describe_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### describe_cluster.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### describe_cluster.ApiResponseFor500
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

# **list_clusters**
<a name="list_clusters"></a>
> ListClustersResponseContent list_clusters()



Retrieve the list of existing clusters.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_operations_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.cluster_status_filtering_option import ClusterStatusFilteringOption
from openapi_client.model.list_clusters_response_content import ListClustersResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
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
    api_instance = cluster_operations_api.ClusterOperationsApi(api_client)

    # example passing only optional values
    query_params = {
        'region': "region_example",
        'nextToken': "nextToken_example",
        'clusterStatus': [
        ClusterStatusFilteringOption("CREATE_IN_PROGRESS")
    ],
    }
    try:
        api_response = api_instance.list_clusters(
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->list_clusters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
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
clusterStatus | ClusterStatusSchema | | optional


# RegionSchema

List clusters deployed to a given AWS Region.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | List clusters deployed to a given AWS Region. | 

# NextTokenSchema

Token to use for paginated requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to use for paginated requests. | 

# ClusterStatusSchema

Filter by cluster status. (Defaults to all clusters.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter by cluster status. (Defaults to all clusters.) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterStatusFilteringOption**]({{complexTypePrefix}}ClusterStatusFilteringOption.md) | [**ClusterStatusFilteringOption**]({{complexTypePrefix}}ClusterStatusFilteringOption.md) | [**ClusterStatusFilteringOption**]({{complexTypePrefix}}ClusterStatusFilteringOption.md) |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_clusters.ApiResponseFor200) | ListClusters 200 response
400 | [ApiResponseFor400](#list_clusters.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#list_clusters.ApiResponseFor401) | UnauthorizedClientError 401 response
429 | [ApiResponseFor429](#list_clusters.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#list_clusters.ApiResponseFor500) | InternalServiceException 500 response

#### list_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListClustersResponseContent**](../../models/ListClustersResponseContent.md) |  | 


#### list_clusters.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### list_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### list_clusters.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### list_clusters.ApiResponseFor500
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

# **update_cluster**
<a name="update_cluster"></a>
> UpdateClusterResponseContent update_cluster(cluster_nameupdate_cluster_request_content)



Update a cluster managed in a given region.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_operations_api
from openapi_client.model.conflict_exception_response_content import ConflictExceptionResponseContent
from openapi_client.model.update_cluster_request_content import UpdateClusterRequestContent
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.update_cluster_bad_request_exception_response_content import UpdateClusterBadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.dryrun_operation_exception_response_content import DryrunOperationExceptionResponseContent
from openapi_client.model.validation_level import ValidationLevel
from openapi_client.model.update_cluster_response_content import UpdateClusterResponseContent
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
    api_instance = cluster_operations_api.ClusterOperationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    body = UpdateClusterRequestContent(
        cluster_configuration="cluster_configuration_example",
    )
    try:
        api_response = api_instance.update_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->update_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'suppressValidators': [
        "type:u2LC4"
    ],
        'validationFailureLevel': ValidationLevel("INFO"),
        'region': "region_example",
        'dryrun': True,
        'forceUpdate': True,
    }
    body = UpdateClusterRequestContent(
        cluster_configuration="cluster_configuration_example",
    )
    try:
        api_response = api_instance.update_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterOperationsApi->update_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateClusterRequestContent**](../../models/UpdateClusterRequestContent.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
suppressValidators | SuppressValidatorsSchema | | optional
validationFailureLevel | ValidationFailureLevelSchema | | optional
region | RegionSchema | | optional
dryrun | DryrunSchema | | optional
forceUpdate | ForceUpdateSchema | | optional


# SuppressValidatorsSchema

Identifies one or more config validators to suppress. Format: (ALL|type:[A-Za-z0-9]+)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Identifies one or more config validators to suppress. Format: (ALL|type:[A-Za-z0-9]+) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# ValidationFailureLevelSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ValidationLevel**](../../models/ValidationLevel.md) |  | 


# RegionSchema

AWS Region that the operation corresponds to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | AWS Region that the operation corresponds to. | 

# DryrunSchema

Only perform request validation without creating any resource. May be used to validate the cluster configuration and update requirements. (Defaults to 'false'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Only perform request validation without creating any resource. May be used to validate the cluster configuration and update requirements. (Defaults to &#x27;false&#x27;.) | 

# ForceUpdateSchema

Force update by ignoring the update validation errors. (Defaults to 'false'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Force update by ignoring the update validation errors. (Defaults to &#x27;false&#x27;.) | 

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
202 | [ApiResponseFor202](#update_cluster.ApiResponseFor202) | UpdateCluster 202 response
400 | [ApiResponseFor400](#update_cluster.ApiResponseFor400) | UpdateClusterBadRequestException 400 response
401 | [ApiResponseFor401](#update_cluster.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#update_cluster.ApiResponseFor404) | NotFoundException 404 response
409 | [ApiResponseFor409](#update_cluster.ApiResponseFor409) | ConflictException 409 response
412 | [ApiResponseFor412](#update_cluster.ApiResponseFor412) | DryrunOperationException 412 response
429 | [ApiResponseFor429](#update_cluster.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#update_cluster.ApiResponseFor500) | InternalServiceException 500 response

#### update_cluster.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateClusterResponseContent**](../../models/UpdateClusterResponseContent.md) |  | 


#### update_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateClusterBadRequestExceptionResponseContent**](../../models/UpdateClusterBadRequestExceptionResponseContent.md) |  | 


#### update_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### update_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### update_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ConflictExceptionResponseContent**](../../models/ConflictExceptionResponseContent.md) |  | 


#### update_cluster.ApiResponseFor412
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor412ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor412ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DryrunOperationExceptionResponseContent**](../../models/DryrunOperationExceptionResponseContent.md) |  | 


#### update_cluster.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### update_cluster.ApiResponseFor500
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


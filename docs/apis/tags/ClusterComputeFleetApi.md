<a name="__pageTop"></a>
# openapi_client.apis.tags.cluster_compute_fleet_api.ClusterComputeFleetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**describe_compute_fleet**](#describe_compute_fleet) | **get** /v3/clusters/{clusterName}/computefleet | 
[**update_compute_fleet**](#update_compute_fleet) | **patch** /v3/clusters/{clusterName}/computefleet | 

# **describe_compute_fleet**
<a name="describe_compute_fleet"></a>
> DescribeComputeFleetResponseContent describe_compute_fleet(cluster_name)



Describe the status of the compute fleet.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_compute_fleet_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.describe_compute_fleet_response_content import DescribeComputeFleetResponseContent
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
    api_instance = cluster_compute_fleet_api.ClusterComputeFleetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.describe_compute_fleet(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterComputeFleetApi->describe_compute_fleet: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
    }
    try:
        api_response = api_instance.describe_compute_fleet(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterComputeFleetApi->describe_compute_fleet: %s\n" % e)
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
200 | [ApiResponseFor200](#describe_compute_fleet.ApiResponseFor200) | DescribeComputeFleet 200 response
400 | [ApiResponseFor400](#describe_compute_fleet.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#describe_compute_fleet.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#describe_compute_fleet.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#describe_compute_fleet.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#describe_compute_fleet.ApiResponseFor500) | InternalServiceException 500 response

#### describe_compute_fleet.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DescribeComputeFleetResponseContent**](../../models/DescribeComputeFleetResponseContent.md) |  | 


#### describe_compute_fleet.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### describe_compute_fleet.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### describe_compute_fleet.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### describe_compute_fleet.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### describe_compute_fleet.ApiResponseFor500
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

# **update_compute_fleet**
<a name="update_compute_fleet"></a>
> UpdateComputeFleetResponseContent update_compute_fleet(cluster_nameupdate_compute_fleet_request_content)



Update the status of the cluster compute fleet.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import cluster_compute_fleet_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.update_compute_fleet_response_content import UpdateComputeFleetResponseContent
from openapi_client.model.update_compute_fleet_request_content import UpdateComputeFleetRequestContent
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
    api_instance = cluster_compute_fleet_api.ClusterComputeFleetApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
    }
    body = UpdateComputeFleetRequestContent(
        status=RequestedComputeFleetStatus("START_REQUESTED"),
    )
    try:
        api_response = api_instance.update_compute_fleet(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterComputeFleetApi->update_compute_fleet: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
    }
    body = UpdateComputeFleetRequestContent(
        status=RequestedComputeFleetStatus("START_REQUESTED"),
    )
    try:
        api_response = api_instance.update_compute_fleet(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ClusterComputeFleetApi->update_compute_fleet: %s\n" % e)
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
[**UpdateComputeFleetRequestContent**](../../models/UpdateComputeFleetRequestContent.md) |  | 


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
204 | [ApiResponseFor204](#update_compute_fleet.ApiResponseFor204) | UpdateComputeFleet 204 response
400 | [ApiResponseFor400](#update_compute_fleet.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#update_compute_fleet.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#update_compute_fleet.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#update_compute_fleet.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#update_compute_fleet.ApiResponseFor500) | InternalServiceException 500 response

#### update_compute_fleet.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor204ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor204ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UpdateComputeFleetResponseContent**](../../models/UpdateComputeFleetResponseContent.md) |  | 


#### update_compute_fleet.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### update_compute_fleet.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### update_compute_fleet.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### update_compute_fleet.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### update_compute_fleet.ApiResponseFor500
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


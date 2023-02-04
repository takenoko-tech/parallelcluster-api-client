<a name="__pageTop"></a>
# openapi_client.apis.tags.image_logs_api.ImageLogsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_image_log_events**](#get_image_log_events) | **get** /v3/images/custom/{imageId}/logstreams/{logStreamName} | 
[**get_image_stack_events**](#get_image_stack_events) | **get** /v3/images/custom/{imageId}/stackevents | 
[**list_image_log_streams**](#list_image_log_streams) | **get** /v3/images/custom/{imageId}/logstreams | 

# **get_image_log_events**
<a name="get_image_log_events"></a>
> GetImageLogEventsResponseContent get_image_log_events(image_idlog_stream_name)



Retrieve the events associated with an image build.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import image_logs_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.get_image_log_events_response_content import GetImageLogEventsResponseContent
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
    api_instance = image_logs_api.ImageLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'imageId': "AqWzyB",
        'logStreamName': "logStreamName_example",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_image_log_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->get_image_log_events: %s\n" % e)

    # example passing only optional values
    path_params = {
        'imageId': "AqWzyB",
        'logStreamName': "logStreamName_example",
    }
    query_params = {
        'region': "region_example",
        'nextToken': "nextToken_example",
        'startFromHead': True,
        'limit': 3.14,
        'startTime': "1970-01-01T00:00:00.00Z",
        'endTime': "1970-01-01T00:00:00.00Z",
    }
    try:
        api_response = api_instance.get_image_log_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->get_image_log_events: %s\n" % e)
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
startFromHead | StartFromHeadSchema | | optional
limit | LimitSchema | | optional
startTime | StartTimeSchema | | optional
endTime | EndTimeSchema | | optional


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

# StartFromHeadSchema

If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. (Defaults to 'false'.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. (Defaults to &#x27;false&#x27;.) | 

# LimitSchema

The maximum number of log events returned. If you don't specify a value, the maximum is as many log events as can fit in a response size of 1 MB, up to 10,000 log events.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum number of log events returned. If you don&#x27;t specify a value, the maximum is as many log events as can fit in a response size of 1 MB, up to 10,000 log events. | 

# StartTimeSchema

The start of the time range, expressed in ISO 8601 format (e.g. '2021-01-01T20:00:00Z'). Events with a timestamp equal to this time or later than this time are included.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The start of the time range, expressed in ISO 8601 format (e.g. &#x27;2021-01-01T20:00:00Z&#x27;). Events with a timestamp equal to this time or later than this time are included. | value must conform to RFC-3339 date-time

# EndTimeSchema

The end of the time range, expressed in ISO 8601 format (e.g. '2021-01-01T20:00:00Z'). Events with a timestamp equal to or later than this time are not included.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The end of the time range, expressed in ISO 8601 format (e.g. &#x27;2021-01-01T20:00:00Z&#x27;). Events with a timestamp equal to or later than this time are not included. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
imageId | ImageIdSchema | | 
logStreamName | LogStreamNameSchema | | 

# ImageIdSchema

Id of the image.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Id of the image. | 

# LogStreamNameSchema

Name of the log stream.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Name of the log stream. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_image_log_events.ApiResponseFor200) | GetImageLogEvents 200 response
400 | [ApiResponseFor400](#get_image_log_events.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#get_image_log_events.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#get_image_log_events.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#get_image_log_events.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#get_image_log_events.ApiResponseFor500) | InternalServiceException 500 response

#### get_image_log_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetImageLogEventsResponseContent**](../../models/GetImageLogEventsResponseContent.md) |  | 


#### get_image_log_events.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### get_image_log_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### get_image_log_events.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### get_image_log_events.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### get_image_log_events.ApiResponseFor500
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

# **get_image_stack_events**
<a name="get_image_stack_events"></a>
> GetImageStackEventsResponseContent get_image_stack_events(image_id)



Retrieve the events associated with the stack for a given image build.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import image_logs_api
from openapi_client.model.internal_service_exception_response_content import InternalServiceExceptionResponseContent
from openapi_client.model.bad_request_exception_response_content import BadRequestExceptionResponseContent
from openapi_client.model.limit_exceeded_exception_response_content import LimitExceededExceptionResponseContent
from openapi_client.model.unauthorized_client_error_response_content import UnauthorizedClientErrorResponseContent
from openapi_client.model.get_image_stack_events_response_content import GetImageStackEventsResponseContent
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
    api_instance = image_logs_api.ImageLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'imageId': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.get_image_stack_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->get_image_stack_events: %s\n" % e)

    # example passing only optional values
    path_params = {
        'imageId': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
        'nextToken': "nextToken_example",
    }
    try:
        api_response = api_instance.get_image_stack_events(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->get_image_stack_events: %s\n" % e)
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

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
imageId | ImageIdSchema | | 

# ImageIdSchema

Id of the image.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Id of the image. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_image_stack_events.ApiResponseFor200) | GetImageStackEvents 200 response
400 | [ApiResponseFor400](#get_image_stack_events.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#get_image_stack_events.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#get_image_stack_events.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#get_image_stack_events.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#get_image_stack_events.ApiResponseFor500) | InternalServiceException 500 response

#### get_image_stack_events.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetImageStackEventsResponseContent**](../../models/GetImageStackEventsResponseContent.md) |  | 


#### get_image_stack_events.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### get_image_stack_events.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### get_image_stack_events.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### get_image_stack_events.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### get_image_stack_events.ApiResponseFor500
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

# **list_image_log_streams**
<a name="list_image_log_streams"></a>
> ListImageLogStreamsResponseContent list_image_log_streams(image_id)



Retrieve the list of log streams associated with an image.

### Example

* Api Key Authentication (aws.auth.sigv4):
```python
import openapi_client
from openapi_client.apis.tags import image_logs_api
from openapi_client.model.list_image_log_streams_response_content import ListImageLogStreamsResponseContent
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
    api_instance = image_logs_api.ImageLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'imageId': "AqWzyB",
    }
    query_params = {
    }
    try:
        api_response = api_instance.list_image_log_streams(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->list_image_log_streams: %s\n" % e)

    # example passing only optional values
    path_params = {
        'imageId': "AqWzyB",
    }
    query_params = {
        'region': "region_example",
        'nextToken': "nextToken_example",
    }
    try:
        api_response = api_instance.list_image_log_streams(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ImageLogsApi->list_image_log_streams: %s\n" % e)
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


# RegionSchema

Region that the given image belongs to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Region that the given image belongs to. | 

# NextTokenSchema

Token to use for paginated requests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to use for paginated requests. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
imageId | ImageIdSchema | | 

# ImageIdSchema

Id of the image.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Id of the image. | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_image_log_streams.ApiResponseFor200) | ListImageLogStreams 200 response
400 | [ApiResponseFor400](#list_image_log_streams.ApiResponseFor400) | BadRequestException 400 response
401 | [ApiResponseFor401](#list_image_log_streams.ApiResponseFor401) | UnauthorizedClientError 401 response
404 | [ApiResponseFor404](#list_image_log_streams.ApiResponseFor404) | NotFoundException 404 response
429 | [ApiResponseFor429](#list_image_log_streams.ApiResponseFor429) | LimitExceededException 429 response
500 | [ApiResponseFor500](#list_image_log_streams.ApiResponseFor500) | InternalServiceException 500 response

#### list_image_log_streams.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ListImageLogStreamsResponseContent**](../../models/ListImageLogStreamsResponseContent.md) |  | 


#### list_image_log_streams.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BadRequestExceptionResponseContent**](../../models/BadRequestExceptionResponseContent.md) |  | 


#### list_image_log_streams.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UnauthorizedClientErrorResponseContent**](../../models/UnauthorizedClientErrorResponseContent.md) |  | 


#### list_image_log_streams.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NotFoundExceptionResponseContent**](../../models/NotFoundExceptionResponseContent.md) |  | 


#### list_image_log_streams.ApiResponseFor429
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor429ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor429ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**LimitExceededExceptionResponseContent**](../../models/LimitExceededExceptionResponseContent.md) |  | 


#### list_image_log_streams.ApiResponseFor500
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


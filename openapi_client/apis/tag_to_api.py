import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.cluster_compute_fleet_api import ClusterComputeFleetApi
from openapi_client.apis.tags.cluster_instances_api import ClusterInstancesApi
from openapi_client.apis.tags.cluster_logs_api import ClusterLogsApi
from openapi_client.apis.tags.cluster_operations_api import ClusterOperationsApi
from openapi_client.apis.tags.image_logs_api import ImageLogsApi
from openapi_client.apis.tags.image_operations_api import ImageOperationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.CLUSTER_COMPUTE_FLEET: ClusterComputeFleetApi,
        TagValues.CLUSTER_INSTANCES: ClusterInstancesApi,
        TagValues.CLUSTER_LOGS: ClusterLogsApi,
        TagValues.CLUSTER_OPERATIONS: ClusterOperationsApi,
        TagValues.IMAGE_LOGS: ImageLogsApi,
        TagValues.IMAGE_OPERATIONS: ImageOperationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.CLUSTER_COMPUTE_FLEET: ClusterComputeFleetApi,
        TagValues.CLUSTER_INSTANCES: ClusterInstancesApi,
        TagValues.CLUSTER_LOGS: ClusterLogsApi,
        TagValues.CLUSTER_OPERATIONS: ClusterOperationsApi,
        TagValues.IMAGE_LOGS: ImageLogsApi,
        TagValues.IMAGE_OPERATIONS: ImageOperationsApi,
    }
)

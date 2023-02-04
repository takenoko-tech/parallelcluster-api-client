import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.v3_clusters import V3Clusters
from openapi_client.apis.paths.v3_clusters_cluster_name import V3ClustersClusterName
from openapi_client.apis.paths.v3_clusters_cluster_name_computefleet import V3ClustersClusterNameComputefleet
from openapi_client.apis.paths.v3_clusters_cluster_name_instances import V3ClustersClusterNameInstances
from openapi_client.apis.paths.v3_clusters_cluster_name_logstreams import V3ClustersClusterNameLogstreams
from openapi_client.apis.paths.v3_clusters_cluster_name_logstreams_log_stream_name import V3ClustersClusterNameLogstreamsLogStreamName
from openapi_client.apis.paths.v3_clusters_cluster_name_stackevents import V3ClustersClusterNameStackevents
from openapi_client.apis.paths.v3_images_custom import V3ImagesCustom
from openapi_client.apis.paths.v3_images_custom_image_id import V3ImagesCustomImageId
from openapi_client.apis.paths.v3_images_custom_image_id_logstreams import V3ImagesCustomImageIdLogstreams
from openapi_client.apis.paths.v3_images_custom_image_id_logstreams_log_stream_name import V3ImagesCustomImageIdLogstreamsLogStreamName
from openapi_client.apis.paths.v3_images_custom_image_id_stackevents import V3ImagesCustomImageIdStackevents
from openapi_client.apis.paths.v3_images_official import V3ImagesOfficial

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V3_CLUSTERS: V3Clusters,
        PathValues.V3_CLUSTERS_CLUSTER_NAME: V3ClustersClusterName,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_COMPUTEFLEET: V3ClustersClusterNameComputefleet,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_INSTANCES: V3ClustersClusterNameInstances,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS: V3ClustersClusterNameLogstreams,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS_LOG_STREAM_NAME: V3ClustersClusterNameLogstreamsLogStreamName,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_STACKEVENTS: V3ClustersClusterNameStackevents,
        PathValues.V3_IMAGES_CUSTOM: V3ImagesCustom,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID: V3ImagesCustomImageId,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS: V3ImagesCustomImageIdLogstreams,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS_LOG_STREAM_NAME: V3ImagesCustomImageIdLogstreamsLogStreamName,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_STACKEVENTS: V3ImagesCustomImageIdStackevents,
        PathValues.V3_IMAGES_OFFICIAL: V3ImagesOfficial,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V3_CLUSTERS: V3Clusters,
        PathValues.V3_CLUSTERS_CLUSTER_NAME: V3ClustersClusterName,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_COMPUTEFLEET: V3ClustersClusterNameComputefleet,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_INSTANCES: V3ClustersClusterNameInstances,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS: V3ClustersClusterNameLogstreams,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS_LOG_STREAM_NAME: V3ClustersClusterNameLogstreamsLogStreamName,
        PathValues.V3_CLUSTERS_CLUSTER_NAME_STACKEVENTS: V3ClustersClusterNameStackevents,
        PathValues.V3_IMAGES_CUSTOM: V3ImagesCustom,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID: V3ImagesCustomImageId,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS: V3ImagesCustomImageIdLogstreams,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS_LOG_STREAM_NAME: V3ImagesCustomImageIdLogstreamsLogStreamName,
        PathValues.V3_IMAGES_CUSTOM_IMAGE_ID_STACKEVENTS: V3ImagesCustomImageIdStackevents,
        PathValues.V3_IMAGES_OFFICIAL: V3ImagesOfficial,
    }
)

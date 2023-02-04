# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V3_CLUSTERS = "/v3/clusters"
    V3_CLUSTERS_CLUSTER_NAME = "/v3/clusters/{clusterName}"
    V3_CLUSTERS_CLUSTER_NAME_COMPUTEFLEET = "/v3/clusters/{clusterName}/computefleet"
    V3_CLUSTERS_CLUSTER_NAME_INSTANCES = "/v3/clusters/{clusterName}/instances"
    V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS = "/v3/clusters/{clusterName}/logstreams"
    V3_CLUSTERS_CLUSTER_NAME_LOGSTREAMS_LOG_STREAM_NAME = "/v3/clusters/{clusterName}/logstreams/{logStreamName}"
    V3_CLUSTERS_CLUSTER_NAME_STACKEVENTS = "/v3/clusters/{clusterName}/stackevents"
    V3_IMAGES_CUSTOM = "/v3/images/custom"
    V3_IMAGES_CUSTOM_IMAGE_ID = "/v3/images/custom/{imageId}"
    V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS = "/v3/images/custom/{imageId}/logstreams"
    V3_IMAGES_CUSTOM_IMAGE_ID_LOGSTREAMS_LOG_STREAM_NAME = "/v3/images/custom/{imageId}/logstreams/{logStreamName}"
    V3_IMAGES_CUSTOM_IMAGE_ID_STACKEVENTS = "/v3/images/custom/{imageId}/stackevents"
    V3_IMAGES_OFFICIAL = "/v3/images/official"

# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CLUSTER_COMPUTE_FLEET = "Cluster ComputeFleet"
    CLUSTER_INSTANCES = "Cluster Instances"
    CLUSTER_LOGS = "Cluster Logs"
    CLUSTER_OPERATIONS = "Cluster Operations"
    IMAGE_LOGS = "Image Logs"
    IMAGE_OPERATIONS = "Image Operations"

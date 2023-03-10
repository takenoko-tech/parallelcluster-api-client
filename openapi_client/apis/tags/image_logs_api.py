# coding: utf-8

"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.4.0
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.v3_images_custom_image_id_logstreams_log_stream_name.get import GetImageLogEvents
from openapi_client.paths.v3_images_custom_image_id_stackevents.get import GetImageStackEvents
from openapi_client.paths.v3_images_custom_image_id_logstreams.get import ListImageLogStreams


class ImageLogsApi(
    GetImageLogEvents,
    GetImageStackEvents,
    ListImageLogStreams,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass

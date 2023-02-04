# coding: utf-8

"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.4.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class RequestedComputeFleetStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def START_REQUESTED(cls):
        return cls("START_REQUESTED")
    
    @schemas.classproperty
    def STOP_REQUESTED(cls):
        return cls("STOP_REQUESTED")
    
    @schemas.classproperty
    def ENABLED(cls):
        return cls("ENABLED")
    
    @schemas.classproperty
    def DISABLED(cls):
        return cls("DISABLED")

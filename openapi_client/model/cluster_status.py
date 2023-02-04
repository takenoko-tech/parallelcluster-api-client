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


class ClusterStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "CREATE_IN_PROGRESS": "CREATE_IN_PROGRESS",
            "CREATE_FAILED": "CREATE_FAILED",
            "CREATE_COMPLETE": "CREATE_COMPLETE",
            "DELETE_IN_PROGRESS": "DELETE_IN_PROGRESS",
            "DELETE_FAILED": "DELETE_FAILED",
            "DELETE_COMPLETE": "DELETE_COMPLETE",
            "UPDATE_IN_PROGRESS": "UPDATE_IN_PROGRESS",
            "UPDATE_COMPLETE": "UPDATE_COMPLETE",
            "UPDATE_FAILED": "UPDATE_FAILED",
        }
    
    @schemas.classproperty
    def CREATE_IN_PROGRESS(cls):
        return cls("CREATE_IN_PROGRESS")
    
    @schemas.classproperty
    def CREATE_FAILED(cls):
        return cls("CREATE_FAILED")
    
    @schemas.classproperty
    def CREATE_COMPLETE(cls):
        return cls("CREATE_COMPLETE")
    
    @schemas.classproperty
    def DELETE_IN_PROGRESS(cls):
        return cls("DELETE_IN_PROGRESS")
    
    @schemas.classproperty
    def DELETE_FAILED(cls):
        return cls("DELETE_FAILED")
    
    @schemas.classproperty
    def DELETE_COMPLETE(cls):
        return cls("DELETE_COMPLETE")
    
    @schemas.classproperty
    def UPDATE_IN_PROGRESS(cls):
        return cls("UPDATE_IN_PROGRESS")
    
    @schemas.classproperty
    def UPDATE_COMPLETE(cls):
        return cls("UPDATE_COMPLETE")
    
    @schemas.classproperty
    def UPDATE_FAILED(cls):
        return cls("UPDATE_FAILED")
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


class ImageBuilderImageStatus(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def PENDING(cls):
        return cls("PENDING")
    
    @schemas.classproperty
    def CREATING(cls):
        return cls("CREATING")
    
    @schemas.classproperty
    def BUILDING(cls):
        return cls("BUILDING")
    
    @schemas.classproperty
    def TESTING(cls):
        return cls("TESTING")
    
    @schemas.classproperty
    def DISTRIBUTING(cls):
        return cls("DISTRIBUTING")
    
    @schemas.classproperty
    def INTEGRATING(cls):
        return cls("INTEGRATING")
    
    @schemas.classproperty
    def AVAILABLE(cls):
        return cls("AVAILABLE")
    
    @schemas.classproperty
    def CANCELLED(cls):
        return cls("CANCELLED")
    
    @schemas.classproperty
    def FAILED(cls):
        return cls("FAILED")
    
    @schemas.classproperty
    def DEPRECATED(cls):
        return cls("DEPRECATED")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("DELETED")

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


class CreateClusterRequestContent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "clusterName",
            "clusterConfiguration",
        }
        
        class properties:
            
            
            class clusterName(
                schemas.StrSchema
            ):
                pass
            clusterConfiguration = schemas.StrSchema
            __annotations__ = {
                "clusterName": clusterName,
                "clusterConfiguration": clusterConfiguration,
            }
    
    clusterName: MetaOapg.properties.clusterName
    clusterConfiguration: MetaOapg.properties.clusterConfiguration
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterConfiguration"]) -> MetaOapg.properties.clusterConfiguration: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clusterName", "clusterConfiguration", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterConfiguration"]) -> MetaOapg.properties.clusterConfiguration: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clusterName", "clusterConfiguration", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        clusterName: typing.Union[MetaOapg.properties.clusterName, str, ],
        clusterConfiguration: typing.Union[MetaOapg.properties.clusterConfiguration, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateClusterRequestContent':
        return super().__new__(
            cls,
            *_args,
            clusterName=clusterName,
            clusterConfiguration=clusterConfiguration,
            _configuration=_configuration,
            **kwargs,
        )

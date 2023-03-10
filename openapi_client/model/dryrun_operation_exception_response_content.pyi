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


class DryrunOperationExceptionResponseContent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Communicates that the operation would have succeeded without the dryrun flag.
    """


    class MetaOapg:
        
        class properties:
            message = schemas.StrSchema
            
            
            class changeSet(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Change']:
                        return Change
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Change'], typing.List['Change']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'changeSet':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Change':
                    return super().__getitem__(i)
            
            
            class validationMessages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ConfigValidationMessage']:
                        return ConfigValidationMessage
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ConfigValidationMessage'], typing.List['ConfigValidationMessage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'validationMessages':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ConfigValidationMessage':
                    return super().__getitem__(i)
            __annotations__ = {
                "message": message,
                "changeSet": changeSet,
                "validationMessages": validationMessages,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["changeSet"]) -> MetaOapg.properties.changeSet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["validationMessages"]) -> MetaOapg.properties.validationMessages: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "changeSet", "validationMessages", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> typing.Union[MetaOapg.properties.message, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["changeSet"]) -> typing.Union[MetaOapg.properties.changeSet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["validationMessages"]) -> typing.Union[MetaOapg.properties.validationMessages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "changeSet", "validationMessages", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        message: typing.Union[MetaOapg.properties.message, str, schemas.Unset] = schemas.unset,
        changeSet: typing.Union[MetaOapg.properties.changeSet, list, tuple, schemas.Unset] = schemas.unset,
        validationMessages: typing.Union[MetaOapg.properties.validationMessages, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DryrunOperationExceptionResponseContent':
        return super().__new__(
            cls,
            *_args,
            message=message,
            changeSet=changeSet,
            validationMessages=validationMessages,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.change import Change
from openapi_client.model.config_validation_message import ConfigValidationMessage

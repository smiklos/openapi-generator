# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api.schemas import (  # noqa: F401
    AnyTypeSchema,
    ComposedSchema,
    DictSchema,
    ListSchema,
    StrSchema,
    IntSchema,
    Int32Schema,
    Int64Schema,
    Float32Schema,
    Float64Schema,
    NumberSchema,
    UUIDSchema,
    DateSchema,
    DateTimeSchema,
    DecimalSchema,
    BoolSchema,
    BinarySchema,
    NoneSchema,
    none_type,
    Configuration,
    Unset,
    unset,
    ComposedBase,
    ListBase,
    DictBase,
    NoneBase,
    StrBase,
    IntBase,
    Int32Base,
    Int64Base,
    Float32Base,
    Float64Base,
    NumberBase,
    UUIDBase,
    DateBase,
    DateTimeBase,
    BoolBase,
    BinaryBase,
    Schema,
    _SchemaValidator,
    _SchemaTypeChecker,
    _SchemaEnumMaker
)


class Pet(
    DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Pet object that needs to be added to the store
    """
    _required_property_names = set((
        'name',
        'photoUrls',
    ))
    id = Int64Schema

    @classmethod
    @property
    def category(cls) -> typing.Type['Category']:
        return Category
    name = StrSchema
    
    
    class photoUrls(
        ListSchema
    ):
        _items = StrSchema
    
    
    class tags(
        ListSchema
    ):
    
        @classmethod
        @property
        def _items(cls) -> typing.Type['Tag']:
            return Tag
    
    
    class status(
        _SchemaEnumMaker(
            enum_value_to_name={
                "available": "AVAILABLE",
                "pending": "PENDING",
                "sold": "SOLD",
            }
        ),
        StrSchema
    ):
        
        @classmethod
        @property
        def AVAILABLE(cls):
            return cls("available")
        
        @classmethod
        @property
        def PENDING(cls):
            return cls("pending")
        
        @classmethod
        @property
        def SOLD(cls):
            return cls("sold")


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        name: name,
        photoUrls: photoUrls,
        id: typing.Union[id, Unset] = unset,
        category: typing.Union['Category', Unset] = unset,
        tags: typing.Union[tags, Unset] = unset,
        status: typing.Union[status, Unset] = unset,
        _configuration: typing.Optional[Configuration] = None,
        **kwargs: typing.Type[Schema],
    ) -> 'Pet':
        return super().__new__(
            cls,
            *args,
            name=name,
            photoUrls=photoUrls,
            id=id,
            category=category,
            tags=tags,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from petstore_api.model.category import Category
from petstore_api.model.tag import Tag

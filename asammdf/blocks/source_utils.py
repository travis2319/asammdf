# -*- coding: utf-8 -*-
"""
asammdf utility functions for source information
"""

from __future__ import annotations

from functools import lru_cache

from . import v2_v3_blocks as v3b
from . import v2_v3_constants as v3c
from . import v4_blocks as v4b
from . import v4_constants as v4c
from ..types import SourceType

SourceEnum = v4c.SourceEnum
BusEnum = v4c.BusEnum


class Source:

    __slots__ = "name", "path", "comment", "source_type", "bus_type"

    SOURCE_OTHER = SourceEnum.SOURCE_OTHER
    SOURCE_ECU = SourceEnum.SOURCE_ECU
    SOURCE_BUS = SourceEnum.SOURCE_BUS
    SOURCE_IO = SourceEnum.SOURCE_IO
    SOURCE_TOOL = SourceEnum.SOURCE_TOOL
    SOURCE_USER = SourceEnum.SOURCE_USER

    BUS_TYPE_NONE = BusEnum.BUS_TYPE_NONE
    BUS_TYPE_OTHER = BusEnum.BUS_TYPE_OTHER
    BUS_TYPE_CAN = BusEnum.BUS_TYPE_CAN
    BUS_TYPE_LIN = BusEnum.BUS_TYPE_LIN
    BUS_TYPE_MOST = BusEnum.BUS_TYPE_MOST
    BUS_TYPE_FLEXRAY = BusEnum.BUS_TYPE_FLEXRAY
    BUS_TYPE_K_LINE = BusEnum.BUS_TYPE_K_LINE
    BUS_TYPE_ETHERNET = BusEnum.BUS_TYPE_ETHERNET
    BUS_TYPE_USB = BusEnum.BUS_TYPE_USB

    def __init__(
        self, name: str, path: str, comment: str, source_type: int, bus_type: int
    ) -> None:
        """Commons reprezentation for source information

        Attributes
        ----------
        name : str
            source name
        path : str
            source path
        comment : str
            source comment
        source_type : int
            source type code
        bus_type : int
            source bus code

        """
        self.name, self.path, self.comment, self.source_type, self.bus_type = (
            name,
            path,
            comment,
            source_type,
            bus_type,
        )

    @classmethod
    @lru_cache(128)
    def from_source(cls, source: SourceType) -> Source:
        if isinstance(source, v3b.ChannelExtension):
            if source.type == v3c.SOURCE_ECU:
                return cls(
                    source.name,
                    source.path,
                    source.comment,
                    cls.SOURCE_OTHER,  # source type other
                    cls.BUS_TYPE_NONE,  # bus type none
                )
            else:
                return cls(
                    source.name,
                    source.path,
                    source.comment,
                    cls.SOURCE_BUS,  # source type bus
                    cls.BUS_TYPE_CAN,  # bus type CAN
                )

        elif isinstance(source, v4b.SourceInformation):
            return cls(
                source.name,
                source.path,
                source.comment,
                source.source_type,
                source.bus_type,
            )
        elif isinstance(source, Source):
            return cls(
                source.name,
                source.path,
                source.comment,
                source.source_type,
                source.bus_type,
            )

    def get_details(self) -> str:
        source_type = SourceEnum.SOURCE_TYPE_TO_STRING[self.source_type]
        bus_type = BusEnum.BUS_TYPE_TO_STRING[self.bus_type]
        return f"     {source_type} source on bus {bus_type}: name=[{self.name}] path=[{self.path}]"

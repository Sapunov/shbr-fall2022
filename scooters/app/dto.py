from __future__ import annotations

import typing as tp
import dataclasses

import asyncpg

from app import models


@dataclasses.dataclass(frozen=True)
class Location:
    lat: float
    lon: float

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Location:
        return cls(lat=row[0], lon=row[1])


@dataclasses.dataclass(frozen=True)
class Scooter(models.Scooter):
    address: str

    @classmethod
    def from_model(
        cls, scooter_model: models.Scooter, address: str
    ) -> Scooter:
        return cls(
            id=scooter_model.id,
            model=scooter_model.model,
            location=scooter_model.location,
            address=address,
        )

from __future__ import annotations

import dataclasses

import asyncpg

from app import dto


@dataclasses.dataclass(frozen=True)
class Scooter:
    id: str
    model: str
    location: dto.Location

    @classmethod
    def from_db(cls, row: asyncpg.Record) -> Scooter:
        return cls(
            id=row['id'],
            model=row['model'],
            location=dto.Location.from_db(row['location']),
        )

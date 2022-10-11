import typing as tp
import asyncio

from app.context import AppContext
from app import storage
from app import dto
from app import models


async def _get_address_map(
    scooters: tp.List[models.Scooter], context: AppContext
) -> tp.Dict[str, str]:
    futures = [
        context.geocoder.get_address(scooter.location) for scooter in scooters
    ]

    result = await asyncio.gather(*futures)

    return {scooter.id: address for scooter, address in zip(scooters, result)}


async def fetchall(context: AppContext) -> tp.List[dto.Scooter]:
    db_scooters = await storage.get_all_scooters(context)

    address_map = await _get_address_map(db_scooters, context)

    return [
        dto.Scooter.from_model(scooter, address_map[scooter.id])
        for scooter in db_scooters
    ]


async def fetchone(context: AppContext, id: str) -> tp.Optional[dto.Scooter]:
    db_scooter = await storage.get_scooter_by_id(context, id)

    if not db_scooter:
        return None

    address_map = await _get_address_map([db_scooter], context)

    return dto.Scooter.from_model(db_scooter, address_map[db_scooter.id])

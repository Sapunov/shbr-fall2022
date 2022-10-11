import typing as tp

from aiohttp import web

from app.context import AppContext
from app import dto
from app.utils import scooters as scooters_utils


async def handle(_: web.Request, context: AppContext) -> web.Response:
    scooters = await scooters_utils.fetchall(context)
    return web.json_response(
        {
            'scooters': [to_response(scooter) for scooter in scooters],
        }
    )


def to_response(scooter: dto.Scooter) -> dict:
    return {
        'id': scooter.id,
        'model': scooter.model,
        'location': {
            'lat': scooter.location.lat,
            'lon': scooter.location.lon,
        },
        'address': scooter.address,
    }

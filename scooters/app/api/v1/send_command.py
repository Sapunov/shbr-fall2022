import typing as tp

from aiohttp import web
from pydantic import BaseModel

from app.context import AppContext
from app import dto
from app.utils import scooters as scooters_utils
from app.utils import telematics as telematics_utils


class Request(BaseModel):
    id: str
    command: str  # enum better

    @classmethod
    async def from_request(cls, request: web.Request):
        data = await request.json()
        return cls(**data)


async def handle(request: Request, context: AppContext) -> web.Response:
    scooter = await scooters_utils.fetchone(context, request.id)

    if not scooter:
        return web.json_response({'error': 'not-found'}, status=404)

    result = await telematics_utils.select_client(scooter).send_command(
        scooter.id, request.command
    )

    return web.json_response({'result': result})

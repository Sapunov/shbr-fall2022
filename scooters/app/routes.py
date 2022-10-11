from aiohttp import web

from app.api.v1 import get_scooters

from app.api.v1 import send_command
from app.context import AppContext


def wrap_handler(handler, context, request_parser=None):
    async def wrapper(request):
        if request_parser:
            try:
                request = await request_parser(request)
            except ValueError as exc:
                return web.json_response(
                    {'code': 'request_error', 'error': str(exc)}, status=400
                )
        return await handler(request, context)

    return wrapper


def setup_routes(app: web.Application, ctx: AppContext) -> None:
    app.router.add_get(
        '/v1/scooters',
        wrap_handler(
            get_scooters.handle,
            ctx,
        ),
    )
    app.router.add_post(
        '/v1/command',
        wrap_handler(
            send_command.handle,
            ctx,
            send_command.Request.from_request,
        ),
    )

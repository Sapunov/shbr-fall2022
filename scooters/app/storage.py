import typing as tp

from app.context import AppContext
from app import models


async def get_all_scooters(ctx: AppContext) -> tp.List[models.Scooter]:
    sql = '''
    select id, model, location from scooters order by id
    '''
    rows = await ctx.db.fetch(sql)
    return [models.Scooter.from_db(row) for row in rows]


async def get_scooter_by_id(
    ctx: AppContext, id: str
) -> tp.Optional[models.Scooter]:
    sql = '''
    select id, model, location from scooters where id = $1
    '''
    row = await ctx.db.fetchrow(sql, id)

    if not row:
        return None

    return models.Scooter.from_db(row)

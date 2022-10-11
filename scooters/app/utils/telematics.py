import abc

from app import dto


class TelematicsClient(abc.ABC):
    @abc.abstractmethod
    async def send_command(self, id: str, command: str) -> str:
        raise NotImplemented


class TelematicsClient2021(TelematicsClient):
    async def send_command(self, id: str, command: str) -> str:
        return 'Command send via TelematicsClient2021'


class TelematicsClient2022(TelematicsClient):
    async def send_command(self, id: str, command: str) -> str:
        return 'Command send via TelematicsClient2022'


def select_client(scooter: dto.Scooter) -> TelematicsClient:
    if scooter.model == '2021':
        return TelematicsClient2021()
    elif scooter.model == '2022':
        return TelematicsClient2022()
    else:
        raise ValueError('Model not supported')

from typing import *
from adapters import ListJsonToCsvFileAdapter
from repositories import DataRepository


class ExportDataToCsvController:

    def __init__(self, repository: Type[DataRepository], adapter: Type[ListJsonToCsvFileAdapter]) -> None:
        self.__repository = repository
        self.__adapter = adapter

    def execute(self, *args, **kwargs):
        itens: List[Dict[str, Any]] = self.__repository.get_transactions_data(*args, **kwargs)
        self.__adapter.execute(itens)


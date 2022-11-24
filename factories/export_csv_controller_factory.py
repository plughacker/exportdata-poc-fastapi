from adapters.json_to_csv_adapter import ListJsonToCsvFileAdapter
from adapters import ListJsonToCsvFileAdapter
from repositories import DataRepository
from controllers import ExportDataToCsvController

def export_data_to_csv_controller_factory(*args, **kwargs) -> ExportDataToCsvController:
    return ExportDataToCsvController(
        adapter=ListJsonToCsvFileAdapter(),
        repository=DataRepository()
    )

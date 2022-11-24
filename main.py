from datetime import datetime
from fastapi import FastAPI

from factories import export_data_to_csv_controller_factory

app = FastAPI()

@app.get('/')
def index():
    controller = export_data_to_csv_controller_factory()
    controller.execute()
    return {'status': 200, 'data': datetime.now().isoformat()}

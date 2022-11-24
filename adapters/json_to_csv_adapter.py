import os
import pandas
from uuid import uuid4
from typing import Any, List, Dict


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class ListJsonToCsvFileAdapter:

    def execute(self, itens: List[Dict[str, Any]]):
        data_frame = pandas.DataFrame(columns=itens[0]['node'].keys(), data=[i['node'].values() for i in itens])
        file_path = os.path.join(BASE_DIR, 'out', f'{uuid4()}.csv')
        data_frame.to_csv(file_path)


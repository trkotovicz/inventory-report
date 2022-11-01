import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.endswith('.json'):
            raise ValueError('Arquivo inválido')

        with open(path, 'r') as file:
            file_list = json.load(file)
            return list(file_list)

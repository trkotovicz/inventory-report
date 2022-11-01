import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.endswith('.csv'):
            raise ValueError('Arquivo inválido')

        with open(path, 'r') as file:
            file_reader = csv.DictReader(file)
            file_list = [row for row in file_reader]
            return list(file_list)

import csv
import json
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @classmethod
    def import_data(self, path: str, type: str):
        with open(path, 'r') as file:
            if path.endswith('.csv'):
                file_reader = csv.DictReader(file)
                list = [row for row in file_reader]
            if path.endswith('.json'):
                list = json.load(file)

        if type == 'simples':
            return SimpleReport.generate(list)
        if type == 'completo':
            return CompleteReport.generate(list)

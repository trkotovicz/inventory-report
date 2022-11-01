import csv
import json
import xmltodict
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
            if path.endswith('.xml'):
                list = xmltodict.parse(file.read())['dataset']['record']
                # list = Inventory.xml_reader(path)

        if type == 'simples':
            return SimpleReport.generate(list)
        else:
            return CompleteReport.generate(list)

    # def xml_reader(self, path):
    #     list = xmltodict.parse(path.read())['dataset']['record']
    #     return list

import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.importer.json_importer import JsonImporter


def type_importer(path: str):
    if path.endswith(".csv"):
        return CsvImporter
    elif path.endswith(".xml"):
        return XmlImporter
    elif path.endswith(".json"):
        return JsonImporter


def main():
    try:
        path, report_type = sys.argv[1:]
        importer = type_importer(path)
        inventory = InventoryRefactor(importer)
        sys.stdout.write(inventory.import_data(path, report_type), end="")
    except IndexError:
        sys.stderr.write("Verifique os argumentos\n")

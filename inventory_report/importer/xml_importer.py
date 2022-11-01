import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path: str):
        if not path.endswith('.xml'):
            raise ValueError('Arquivo inválido')

        with open(path, 'r') as file:
            file_list = xmltodict.parse(file.read())['dataset']['record']
            return list(file_list)

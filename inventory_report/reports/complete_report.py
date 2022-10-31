from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(self, list_products):
        simple_report = super().generate(list_products)
        list = [product["nome_da_empresa"] for product in list_products]
        count = Counter(list)
        complete_report = ""

        for empresa, vezes in count.items():
            complete_report += f"- {empresa}: {vezes}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{complete_report}"
        )

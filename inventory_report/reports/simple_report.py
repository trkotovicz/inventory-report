from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(self, list_products):
        ...

    @classmethod
    def fabricacao_mais_antiga(self, list_products):
        list = [product["data_de_fabricacao"] for product in list_products]
        return min(list)

    @classmethod
    def validade_mais_proxima(self, list_products):
        today = datetime.now().strftime("%Y/%m/%d")
        list = [
            product["data_de_validade"]
            for product in list_products
            if product["data_de_validade"] > today
        ]
        return min(list)

    @classmethod
    def empresa_mais_produtos(self, list_products):
        ...

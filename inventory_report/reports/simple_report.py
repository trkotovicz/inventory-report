from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def generate(self, list_products):
        fabricacao_mais_antiga = self.fabricacao_mais_antiga(list_products)
        validade_mais_proxima = self.validade_mais_proxima(list_products)
        empresa_mais_produtos = self.empresa_mais_produtos(list_products)
        return (
            f"Data de fabricação mais antiga: {fabricacao_mais_antiga}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa_mais_produtos}"
        )

    @classmethod
    def fabricacao_mais_antiga(self, list_products):
        list = [product["data_de_fabricacao"] for product in list_products]
        return min(list)

    @classmethod
    def validade_mais_proxima(self, list_products):
        today = datetime.now().strftime("%Y-%m-%d")
        list = [
            product["data_de_validade"]
            for product in list_products
            if product["data_de_validade"] > today
        ]
        return min(list)

    @classmethod
    def empresa_mais_produtos(self, list_products):
        list = [product["nome_da_empresa"] for product in list_products]
        count = Counter(list).most_common(1)
        return count
        # count = Counter(list)
        # return max(count)

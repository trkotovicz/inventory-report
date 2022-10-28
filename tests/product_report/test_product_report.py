from inventory_report.inventory.product import Product


def test_relatorio_produto():
    cria_produto = Product(
        1,
        "produto x",
        "empresa a",
        "2022-01-01",
        "2022-12-12",
        123456,
        "de qualquer jeito",
    )
    mock_report = (
        f"O produto {cria_produto.nome_do_produto}"
        f" fabricado em {cria_produto.data_de_fabricacao}"
        f" por {cria_produto.nome_da_empresa} com validade"
        f" até {cria_produto.data_de_validade}"
        f" precisa ser armazenado {cria_produto.instrucoes_de_armazenamento}."
    )

    assert str(cria_produto) == mock_report

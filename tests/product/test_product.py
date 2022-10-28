from inventory_report.inventory.product import Product


def test_cria_produto():
    cria_produto = Product(
        1,
        "produto x",
        "empresa a",
        "2022-01-01",
        "2022-12-12",
        123456,
        "guardado de qualquer jeito",
    )

    assert cria_produto.id == 1
    assert cria_produto.nome_do_produto == "produto x"
    assert cria_produto.nome_da_empresa == "empresa a"
    assert cria_produto.data_de_fabricacao == "2022-01-01"
    assert cria_produto.data_de_validade == "2022-12-12"
    assert cria_produto.numero_de_serie == 123456
    assert (
        cria_produto.instrucoes_de_armazenamento
        == "guardado de qualquer jeito"
    )

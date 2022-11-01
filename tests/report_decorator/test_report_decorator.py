from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


RESET = "\033[0m"
AZUL = "\033[36m"
VERDE = "\033[32m"
VERMELHO = "\033[31m"

mock_produto = [
    {
        "id": 1,
        "nome_do_produto": "produto x",
        "nome_da_empresa": "empresa a",
        "data_de_fabricacao": "2022-01-01",
        "data_de_validade": "2022-12-12",
        "numero_de_serie": 123456,
        "instrucoes_de_armazenamento": "de qualquer jeito",
    }
]

mock_fabricacao = f"{VERDE}Data de fabricação mais antiga:{RESET}"
mock_validade = f"{VERDE}Data de validade mais próxima:{RESET}"
mock_empresa = f"{VERDE}Empresa com mais produtos:{RESET}"
mock_result_fabricacao = f"{AZUL}2022-01-01{RESET}"
mock_result_validade = f"{AZUL}2022-12-12{RESET}"
mock_result_empresa = f"{VERMELHO}empresa a{RESET}"


def test_decorar_relatorio():
    report = ColoredReport(SimpleReport).generate(mock_produto)

    assert (
        f"{mock_fabricacao} {mock_result_fabricacao}\n"
        f"{mock_validade} {mock_result_validade}\n"
        f"{mock_empresa} {mock_result_empresa}"
    ) in report

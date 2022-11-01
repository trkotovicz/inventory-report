import pytest
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


@pytest.fixture
def mock():
    return (
        "Data de fabricação mais antiga: 10-05-2022\n"
        "Data de validade mais próxima: 14-06-2021\n"
        "Empresa com mais produtos: Farinini"
    )


mock_fabricacao = "\033[32mData de fabricação mais antiga: \033[0m"
mock_validade = "\033[32mData de validade mais próxima: \033[0m"
mock_empresa = "\033[32mEmpresa com mais produtos: \033[0m"
mock_result_fabricacao = "\033[36m10-05-2022\033[0m"
mock_result_validade = "\033[36m14-06-2021\033[0m"
mock_result_empresa = "\033[31mFarinini\033[0m"


def test_decorar_relatorio(mock):
    report = SimpleReport(ColoredReport(mock))

    assert report == (
        f"{mock_fabricacao}{mock_result_fabricacao}"
        f"{mock_validade}{mock_result_validade}"
        f"{mock_empresa}{mock_result_empresa}"
    )

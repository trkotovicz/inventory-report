# :construction: README customizado em construção ! :construction:
<!-- 

Inventory Reports

No projeto passado você implementou algumas funções que faziam leitura e escrita de arquivos JSON e CSV, correto?

Neste projeto nós vamos fazer algo parecido, mas utilizando a Programação Orientada a Objetos! Você implementará um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:
- Através da importação de um arquivo CSV;
- Através da importação de um arquivo JSON;
- Através da importação de um arquivo XML.

Além disso, o relatório final possuirá duas versões: simples e completa.

🚵 Habilidades a serem trabalhadas:

Aplicar conceitos de Orientação a Objetos em Python;
Aplicar padrões de projeto;
Leitura e escrita de arquivos (XML, CSV, JSON).


---

Ambiente Virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.
criar o ambiente virtual
$ python3 -m venv .venv
ativar o ambiente virtual
$ source .venv/bin/activate
instalar as dependências no ambiente virtual
$ python3 -m pip install -r dev-requirements.txt
Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

O arquivo dev-requirements.txt contém todas as dependências que serão utilizadas no projeto.

---

🛠 Testes

Para executar os testes certifique-se de que você está com o ambiente virtual ativado

Executar os testes

$ python3 -m pytest
O arquivo pyproject.toml já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

python3 -m pytest -s -vv
Caso precise executar apenas um arquivo de testes basta executar o comando:

python3 -m pytest tests/nomedoarquivo.py
Caso precise executar apenas uma função de testes basta executar o comando:

python3 -m pytest -k nome_da_func_de_tests
Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro -x

python3 -m pytest -x tests/test_simple_report.py
Caso queria executar um teste especifico de um arquivo basta executar o comando:

python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
Se quiser saber mais sobre a instalação de dependências com pip, veja esse artigo.


---


🛼 Executando o Projeto
Após implementar o requisito bônus, seu programa deverá ser executável via linha de comando.
O comando a ser executado será inventory_report. Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip: pip install .

Agora você poderá chamar o comando inventory_report passando seus argumentos:

inventory_report argumento1 argumento2

argumento1 deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um csv, json ou xml.

argumento2 pode receber duas strings: simples ou completo, cada uma gerando o respectivo relatório.

Outra opção é invocar o comando assim:

python3 -m inventory_report.main argumento1 argumento2

---

🗃️ Arquivos com os dados de entrada

Três formatos de importação estão disponíveis no diretório data dentro do diretório inventory_report. Confira o exemplo de formato eles:
Arquivos CSV Os arquivos CSV são separados por vírgula, como no exemplo abaixo:

id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
Arquivos JSON Os arquivos JSON seguem o seguinte modelo:

[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
Arquivos XML Os arquivos XML seguem o seguinte modelo:

<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>

---

REQUISITOS

1 - Testar o construtor/inicializador do objeto Produto
Crie o teste em: tests/product/test_product.py

Imagem de construtor em Python

Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada neste arquivo: inventory_report/inventory/product.py, a classe Product.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste, que certifique que o método __init__ da classe Product esta funcionando corretamente.

O nome deste teste deve ser test_cria_produto, ele deve verificar o correto preenchimento dos seguintes atributos:

id (int)
nome_da_empresa (string)
nome_do_produto (string)
data_de_fabricacao (string)
data_de_validade (string)
numero_de_serie (string)
instrucoes_de_armazenamento (string)

2 - Testar o relatório individual do produto
Crie o teste em: tests/product_report/test_product_report.py

Boa novidade, o primeiro relatório já implementamos neste arquivo inventory_report/inventory/product.py. Formulamos uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.

Para desenvolver este relatório, utilizamos o recurso __repr__ do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada.

Dica: A reimplementação do __repr__ não faz o objeto retornar exatamente uma string, fazer um cast para string, pode te ajudar.

Exemplo da frase:

O produto farinha fabricado em 01-05-2021 por Farinini com validade até 02-06-2023 precisa ser armazenado ao abrigo de luz.

Agora para mantermos uma boa cobertura de testes, precisamos que você implemente o teste.

O nome deste teste deve ser test_relatorio_produto, ele deve instanciar um objeto Product e verificar se acessá-lo a frase de retorno esta correta.

3 - Gerar a versão simplificada do relatório
Crie a classe em: inventory_report/reports/simple_report.py

O relatório deve ser gerado através de um método estático ou de classe chamado generate escrito dentro da classe SimpleReport.

Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
Deve ser possível executar o método generate sem instanciar um objeto de SimpleReport
O método deve receber um parâmetro que representa uma list (estrutura de dados), onde cada posição contém um dict(estrutura de dados).
Exemplo de formato de entrada

   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
O método deverá retornar uma string de saída com o seguinte formato:
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
A data de validade mais próxima, somente considera itens que ainda não venceram.


4 - Gerar a versão completa do relatório
Crie em: inventory_report/reports/complete_report.py

O relatório deve ser gerado através de um método generate para a classe CompleteReport. Ele deverá receber dados numa lista contendo estruturas do tipo dict e deverá retornar uma string formatada como um relatório.

A classe CompleteReport deve herdar da classe SimpleReport e sobrescrever o método generate, de modo a especializar seu comportamento.

Deve ser possível executar o método generate sem instanciar um objeto de CompleteReport

O método deve receber de parâmetro uma lista de dicionários no seguinte formato:

[
  {
    "id": 1,
    "nome_do_produto": "MESA",
    "nome_da_empresa": "Forces of Nature",
    "data_de_fabricacao": "2022-05-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
  }
]
O método deverá retornar uma saída com o seguinte formato:

Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE


5 - Gere os relatórios através de um arquivo CSV
Crie em: inventory_report/inventory/inventory.py

A importação do arquivo CSV deve ser realizada através do método import_data que você deve criar em uma classe chamada Inventory.

O método deve ser estático ou de classe, ou seja, deve ser possível chamá-lo sem instanciar um objeto da classe.

O método receberá como primeiro parâmetro uma string como caminho para o arquivo CSV e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:

"simples"
"completo"
De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe Inventory deve chamar o método generate da classe que vai gerar o relatório (SimpleReport, CompleteReport).


6 - Gere os relatórios através de um arquivo JSON
Incremente em: inventory_report/inventory/inventory.py.

📌 Utilize o mesmo método do requisito anterior.

Altere o método import_data para que ele também seja capaz de carregar arquivos JSON.

Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:

"simples"
"completo"
De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe Inventory deve chamar o método generate da classe que vai gerar o relatório (SimpleReport, CompleteReport).


7 - Gere os relatórios através de um arquivo XML
Incremente em: inventory_report/inventory/inventory.py.

📌 Utilize o mesmo método do requisito anterior.

Altere o método import_data para que ele também seja capaz de carregar arquivos XML.

Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:

"simples"
"completo"
De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe Inventory deve chamar o método generate da classe que vai gerar o relatório (SimpleReport, CompleteReport).


8 - Organizar o código de importação com o padrão Strategy
Crie em: inventory_report/importer/importer.py

Como pôde observar até aqui, o método import_data está com muitas responsabilidades, e, com o intuito de resolver isso, podemos dividir a sua complexidade para cada formato de arquivo.

O padrão de projeto Strategy nos ajuda a isolar cada estratégia em um objeto, e por meio de uma Interface podemos padronizar a assinatura dos métodos, garantindo que todas elas possuam o comportamento similar.

Ao rodar os testes localmente, você terá um teste para cada validação de cada informação

Crie uma classe abstrata Importer para ser a interface da estratégia

A Interface será uma classe abstrata Importer terá três classes de estratégias herdeiras: CsvImporter, JsonImporter e XmlImporter.

Crie as classes nos respectivos arquivos:

inventory_report/importer/csv_importer.py inventory_report/importer/json_importer.py inventory_report/importer/xml_importer.py

A classe abstrata deve definir a assinatura do método import_data a ser implementado por cada classe herdeira. Esse método deve ser estático ou de classe, e deve receber como parâmetro o nome do arquivo a ser importado.

O método import_data definido por cada classe herdeira deve lançar uma exceção do tipo ValueError caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um caminho de um arquivo com extensão .csv para o JsonImporter. A mensagem de erro da exceção deve ser "Arquivo inválido".

O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

[
  {
    "id": 1,
    "nome_do_produto": "Cafe",
    "nome_da_empresa": "Cafes Nature",
    "data_de_fabricacao": "2020-07-04",
    "data_de_validade": "2023-02-09",
    "numero_de_serie": "FR48",
    "instrucoes_de_armazenamento": "instrucao"
  }
]


9 - Testar a geração de uma versão do relatório em cores
Crie o teste em: tests/report_decorator/test_report_decorator.py

Uma versão deste relatório será exibida em letreiros em Led, estes letreiros são coloridos, para isso, já implementamos o método responsável por retornar este relatório em cores.

Implementamos em : inventory_report/reports/colored_report.py

Em vez de criarmos uma classe que herda os relatórios originais, utilizamos o padrão Decorator para receber o tipo do relatório por composição (SimpleReport ou CompleteReport) e, assim, colorir o retorno do método generate, que recebe uma lista de produtos e retorna o relatório já colorido.

Para termos confiança que as cores sairão corretamente, precisamos que você implemente o teste, que certifique que o método generate de ColoredReport funciona corretamente.

Para que o Python consiga colorir as strings, é preciso que a string contenha o início do código da cor, e o reset da cor.

📌 Execute este print teste em um terminal interativo python3 -i. O resultado das cores podem não ser exatos, por isso, atente-se aos códigos deste exemplo:

print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")
Logo Flask

O nome deste teste deve ser test_decorar_relatorio, ele deve verificar se o relatório está devidamente colorido. Representamos abaixo como deve ser a disposição das cores:

🟩Data de fabricação mais antiga:🟩 🟦10-05-2022🟦

🟩Data de validade mais próxima:🟩 🟦14-06-2021🟦

🟩Empresa com mais produtos:🟩 🟥Farinini🟥


---


Projeto desenvolvido por [Thais R Kotovicz](https://www.linkedin.com/in/thaiskotovicz/).
</br>

-->

# Inventory Report

Inventory reports é um gerador de relatórios que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

Esses dados de estoque poderão ser obtidos de diversas fontes:
- Através da importação de um arquivo CSV;
- Através da importação de um arquivo JSON;
- Através da importação de um arquivo XML.

Além disso, o relatório final possui duas versões: simples e completa.


## Habilidades desenvolvidas:

Aplicar conceitos de Orientação a Objetos em Python;</br>
Aplicar padrões de projeto;</br>
Leitura e escrita de arquivos (XML, CSV, JSON).</br>



## Relatórios


### Versão simplificada do relatório

O método retorna uma string de saída com o seguinte formato:
```
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
A data de validade mais próxima, somente considera itens que ainda não venceram.
```


### Versão completa do relatório

O método retorna uma string de saída com o seguinte formato:
```
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```


### Versão do relatório em cores

Uma versão deste relatório será exibida em letreiros em Led, estes letreiros são coloridos, para isso, já implementamos o método responsável por retornar este relatório em cores.


Representação abaixo de como será a disposição das cores:

🟩Data de fabricação mais antiga:🟩 🟦10-05-2022🟦</br>
🟩Data de validade mais próxima:🟩 🟦14-06-2021🟦</br>
🟩Empresa com mais produtos:🟩 🟥Farinini🟥</br>

---

<details>
    <summary><strong>💻 Ambiente Virtual</strong></summary><br />

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.</br>

Criar o ambiente virtual
```
$ python3 -m venv .venv
```

Ativar o ambiente virtual
```
$ source .venv/bin/activate
```

Instalar as dependências no ambiente virtual
```
$ python3 -m pip install -r dev-requirements.txt
```
Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Quando precisar desativar o ambiente virtual, execute o comando "deactivate".

O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto.

</details>

<details>
    <summary><strong>🛠 Testes</strong></summary><br />
    
Para executar os testes certifique-se de que você está com o ambiente virtual ativado.</br>

Executar os testes
```
$ python3 -m pytest
```
O arquivo pyproject.toml já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:
```
python3 -m pytest -s -vv
```
Caso precise executar apenas um arquivo de testes basta executar o comando:
```
python3 -m pytest tests/nomedoarquivo.py
```
Caso precise executar apenas uma função de testes basta executar o comando:
```
python3 -m pytest -k nome_da_func_de_tests
```
Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro -x
```
python3 -m pytest -x tests/test_simple_report.py
```
Caso queria executar um teste especifico de um arquivo basta executar o comando:
```
python3 -m pytest -x tests/nomedoarquivo.py::test_nome_do_teste
```

</details>

<details>
    <summary><strong>📟 Executando o Projeto</strong></summary><br />

O programa é executável via linha de comando. O comando a ser executado será `inventory_report`.</br>
Para que ele funcione em seu ambiente é preciso antes instalar o próprio código como um pacote pip: <code>pip install .</code>

</br>

Agora você poderá chamar o comando inventory_report passando seus argumentos:
```
inventory_report argumento1 argumento2
```
argumento1 deve receber o caminho de um arquivo a ser importado. O arquivo pode ser um csv, json ou xml.

argumento2 pode receber duas strings: simples ou completo, cada uma gerando o respectivo relatório.

Outra opção é invocar o comando assim:
```
python3 -m inventory_report.main argumento1 argumento2
```

</details>

<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />

Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato deles:
  
<strong>Arquivos CSV</strong>
Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
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
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
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
```

</details>

---


Projeto desenvolvido por [Thais R Kotovicz](https://www.linkedin.com/in/thaiskotovicz/).
</br>


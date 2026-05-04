# ⛽ Sistema de Gestão de Abastecimento

Este é um projeto modular desenvolvido em Python que simula o sistema interno de um posto de combustível. O sistema permite gerenciar o catálogo de produtos (combustíveis) e realizar operações de venda com cálculo automático de descontos.

## 🚀 Funcionalidades

* **Gestão de Combustíveis:** Cadastro, listagem, busca e alteração de preços e nomes de combustíveis.
* **Simulação de Venda:** Cálculo de abastecimento por litragem com busca dinâmica de preços.
* **Sistema de Descontos:** Lógica integrada para aplicar 10% de desconto em pagamentos via PIX, Dinheiro ou Débito.
* **Tratamento de Erros:** Validação de entradas para tipos de combustíveis inexistentes e formas de pagamento inválidas.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **Modularização:** Divisão de responsabilidades entre arquivos (`abastecimento`, `combustivel`, `pagamento`, `menu`).
* **Dicionários:** Utilizados para simular um banco de dados em memória.

## 📁 Estrutura do Projeto

* `menu.py`: O ponto de entrada da aplicação, contendo o loop principal e a navegação.
* `combustivel.py`: Responsável pelo CRUD (Create, Read, Update, Delete) dos combustíveis.
* `pagamento.py`: Gerencia a regra de negócio de pagamentos e descontos.
* `abastecimento.py`: Orquestra o processo de venda e o cálculo final ao consumidor.

Desenvolvido por **Bruno Machado Brandão** 🚀

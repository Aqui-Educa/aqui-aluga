# Sistema Aqui Aluga


## Projeto

Este projeto refere-se a um sistema de locação de veículos sob o ponto de vista do usuário - backoffice.

## Funcionalidades

- Categoria
    - Id
    - Nome
    - Sigla
- Veículo
    - Id
    - Marca
    - Modelo
    - Ano
- Loja
    - Id
    - Sigla
    - Endereço
- Cliente
    - Id
    - Nome
    - Telefone
    - CPF
- Locação
    - Id
    - Id da Categoria
    - Id do Cliente
    - Id do Veículo
    - Id do Parceiro
    - Id Itens de contrato
    - Id da Forma de Pagamento
    - Data de Início
    - Data Final
    - Valor
- Parceiro
    - Id
    - Nome
- Itens de contrato
    - Id
    - Nome
- Vendas
    - Id
    - Id do Cliente
    - Id do Veículo
    - Id da Forma de Pagamento
    - Data da Venda
    - Valor
- Forma de pagamento
    - Id
    - Nome

## Ações

- Listagens
- Inserções
- Deleções
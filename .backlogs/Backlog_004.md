# BACKLOG

## Projeto: Sumé Software

* Número: 004/2021
* Domínio de gestão: 05 – Suprimentos
* Vigência: 16/11/2021 a 12/12/2021

1. NECESSIDADES
    1. Ficam definidas as seguintes necessidades por ordem decrescente de prioridade:
        1. Cadastro de contrato (100):
            1. Quando: Sprint 1
            2. Onde:
                1. Portal do Administrador / Suprimentos / Contratos / Cadastrar.
            3. O quê:
                1. Formulário de cadastro de contrato contendo:
                    1. Aba Geral:
                        1. Número (nnn/aaaa) → inabilitado ao cadastrar;
                        2. Prestador (razão social) → inabilitado ao cadastrar;
                        3. Valor (total dos itens vinculados) → inabilitado ao cadastrar;
                        4. Início da vigência;
                        5. Término da vigência;
                        6. Objeto (textArea).
                    2. Aba itens:
                        1. Cadastro de itens:
                            1. Prestador (razão social) → listar apenas os fornecedores que atendam à regra de negócio 1.1.1.4.2;
                            2. Ordem → listar as ordens do fornecedor selecionado que atendam à regra de negócio 1.1.1.4.2;
                            3. Item ordem → listar os itens da ordem selecionada que atendam à regra de negócio 1.1.1.4.2.
                        2. Itens cadastrados. Quadro com as seguintes colunas:
                        3. (contador);
                        4. Serviço → ItensOrdem.produto_servico;
                        5. Quantidade → ItensContrato.qtd;
                        6. Valor unitário → ItensContrato.valor_unitario;
                        7. Valor total;
                        8. Itens (ícones):
                            1. Visualizar: abrir modal exibindo o número da ordem e o projeto;
                            2. Lina de valor total.
                    3. Aba projetos. Quadro que exiba as seguintes colunas:
                        1. **(contador)**;
                        2. Projeto → lista os projetos cujos itens de ordens foram vinculados ao contrato;
                        3. Valor → somatório dos itens de ordem vinculados de cada projeto;
                        4. Linha de valor total.
            4. Regras de negócio:
                1. Um contrato deve ter, pelo menos, um item de ordem vinculado;
                2. Requisitos para que um item de ordem possa ser vinculado a um contrato:
                    1. Deve ser relativo à natureza de despesa Serviços pessoa jurídica;
                    2. Atributo vinculado = False.
                3. A vigência do contrato não deve estar fora da vigência dos projetos vinculados;
                4. Um contrato deve ter apenas um prestador de serviços;
                5. O valor e a quantidade do item contrato deverão ser iguais ao valor e quantidade do item da ordem vinculado;
                6. O valor total do contrato deverá ser o somatório dos seus itens de contrato;
                7. Número do contrato deverá ser um sequencial do ano da data de cadastro;
                8. Quando o contratado for cadastrado, os itens de ordem vinculados ao contrato deverão ter o se atributo ItensOrdem vinculado alterado para True.
            5. Comportamento:
                1. Se o cadastro atender a todas as regras de negócio e os dados forem persistidos no banco:
                    1. Uma mensagem de confirmação deverá ser exibida ao usuário;
                    2. O formulário deverá ser carregado com o dicionário retornado pela API da instância cadastrada (Read);
                    3. O formulário carregado deverá exibir o botão Editar que habilitará o campo Objeto para edição. O comportamento descrito em 1.1.1.5.1 e 1.1.1.5.1.1 deverá ser apresentado.
                2. Se os dados não atenderem às regras de negócio, um modal detalhando as inconsistências deverá ser exibido ao usuário.

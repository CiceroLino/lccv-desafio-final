# BACKLOG

## Projeto: Sumé Software

* Número: 005/2021
* Domínio de gestão: 07 – Patrimônio
* Vigência: 16/11/2021 a 12/12/2021

1. NECESSIDADES
    1. Ficam definidas as seguintes necessidades por ordem decrescente de prioridade:
        1. Cadastro de bem (100):
            1. Quando: Sprint 1
            2. Onde:
                1. Portal do Administrador / Patrimônio / Bens / Cadastrar.
            3. O quê:
                1. Formulário de cadastro de bens contendo:
                    1. Aba Geral:
                        1. Número (AAAAXXXXXX) → inabilitado ao cadastrar;
                        2. Fornecedor (razão social) → listar apenas os fornecedores que atendam à regra de negócio 1.1.1.4.2;
                        3. Nota fiscal → listar as notas fiscais do fornecedor selecionado que atendam à regra de negócio 1.1.1.4.2;
                        4. Item nota fiscal → listar os itens da nota fiscal selecionada;
                        5. Quantidade vinculada (inabilitado) → exibir a quantidade bens já vinculada a item de nota fiscal selecionado;
                        6. Quantidade disponível (inabilitado) → exibir a quantidade de bens disponível a ser cadastrada.
                    2. Aba Bens:
                        1. Cadastro de bens:
                        2. Quantidade → deverá ser limitada à quantidade exibida no item 1.1.1.3.1.1.5;
                        3. Marca;
                        4. Valor unitário (inabilitado) → exibir o valor unitário do item de nota fiscal selecionado;
                        5. Data de início de garantia;
                        6. Data de término da garantia;
                        7. Observações.
                    3. Bens cadastrados. Quadro com as seguintes colunas:
                        1. **(contador)**;
                        2. Tombamento;
                        3. Produto → ItensNotaFiscal.produto_servico;
                        4. Valor;
                        5. Itens (ícones):
                            1. Visualizar: abrir modal exibindo o estado, a situação de uso e a marca.
                    4. Aba Observações:
                        1. Observações (textArea).
            4. Regras de negócio:
                1. Um bem deve ter um item de nota fiscal vinculado;
                2. Requisitos para que um item de nota fiscal possa ser vinculado a um bem:
                    1. Deve ser relativo à natureza de despesa equipamentos e material permanente;
                    2. Atributo vinculado = False;
                    3. O quantitativo de bens já gerados a partir do item de nota fiscal deve ser menor que o quantitativo do item de nota fiscal:
                        1. Ex.: ItensNotaFiscal.qtd = 10 < qtd.Bens.
                3. O estado do bem, ao ser cadastrado, deverá ser Bom;
                4. A situação de uso do bom, ao ser cadastrado, deverá ser Em uso;
                5. O valor de aquisição do bem deverá ser o valor unitário do item de nota fiscal;
                6. A data de início de uso deverá ser a data de cadastro;
                7. Tombamento:
                    1. Deverá ser no formato: AAAAXXXXXX. Onde AAAA refere-se ao ano com 4 dígitos e XXXXXX refere-se à sequência com 6 dígitos.
                8. Quando o bem for cadastrado, se a quantidade de bens vinculados ao item de nota fiscal for igual à ItensNotaFiscal.qtd, o atributo ItensNotaFiscal.vinculado deverá se tornar True.
            5. Comportamento:
                1. Se o cadastro atender a todas as regras de negócio e os dados forem persistidos no banco:
                    1. Uma mensagem de confirmação deverá ser exibida ao usuário;
                    2. O formulário deverá ser carregado com o dicionário retornado pela API de um dos bens cadastrados (Read);
                    3. O formulário carregado deverá exibir o botão Editar que habilitará o campo Observações para edição. O comportamento descrito em 1.1.1.5.1.1 e 1.1.1.5.1.2 deverá ser apresentado.
                2. Se os dados não atenderem às regras de negócio, um modal detalhando as inconsistências deverá ser exibido ao usuário.

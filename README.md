# Simulador-de-App-para-gerenciamento-de-restaurante



Este é um sistema desenvolvido em Python para o gerenciamento interno de um restaurante. O programa utiliza os conceitos de Programação Orientada a Objetos (POO) para gerenciar o cadastro de funcionários e a manutenção de um cardápio de pratos de forma dinâmica e organizada.



Funcionalidades

Configuração Inicial: Definição do nome do restaurante no momento da inicialização do sistema.



Controle de IDs Únicos: Geração automática e sequencial de identificadores (IDs) exclusivos para cada funcionário e prato cadastrado.



Gestão de Funcionários: Cadastro de colaboradores com nome e cargo, além da exibição em formato de tabela estruturada.



Gestão de Cardápio: Cadastro de pratos com nome e preço de venda, contendo validação para impedir valores negativos e exibição formatada com alinhamento de texto e moeda (R$).



Validação de Entradas: Sistema inteligente contra erros de digitação (valores vazios ou caracteres inválidos em campos numéricos).



Estrutura do Código

O projeto é baseado em três classes principais:



Funcionario: Representa cada colaborador, contendo um ID auto-incrementado, nome e cargo.



Prato: Representa os itens do menu, contendo um ID auto-incrementado, nome e preço.



Restaurante: Classe controladora responsável por centralizar as listas de dados e fornecer métodos de manipulação (adição e listagem).



Adicionalmente, a função global obter\_input\_valido padroniza o recebimento de dados via console para mitigar falhas de preenchimento.


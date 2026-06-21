class Funcionario:
    _id_counter = 1  # Contador interno para gerar IDs únicos

    def __init__(self, nome, cargo):
        self.id = Funcionario._id_counter
        self.nome = nome
        self.cargo = cargo
        Funcionario._id_counter += 1


class Prato:
    _id_counter = 1  # Contador interno para gerar IDs únicos

    def __init__(self, nome, preco):
        self.id = Prato._id_counter
        self.nome = nome
        self.preco = preco
        Prato._id_counter += 1


class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []
        self.cardapio = []

    def adicionar_funcionario(self, nome, cargo):
        novo_funcionario = Funcionario(nome, cargo)
        self.funcionarios.append(novo_funcionario)
        print(f"\n[ID {novo_funcionario.id}] {novo_funcionario.nome} cadastrado com sucesso!")

    def adicionar_prato(self, nome, preco):
        novo_prato = Prato(nome, preco)
        self.cardapio.append(novo_prato)
        print(f"\n[ID {novo_prato.id}] '{novo_prato.nome}' adicionado ao cardápio!")

    def listar_funcionarios(self):
        if not self.funcionarios:
            print("\nNenhum funcionário registrado no sistema.")
            return

        print(f"\n--- QUADRO DE FUNCIONÁRIOS: {self.nome.upper()} ---")
        print(f"{'ID':<5} | {'NOME':<20} | {'CARGO':<15}")
        print("-" * 46)
        for f in self.funcionarios:
            print(f"{f.id:<5} | {f.nome:<20} | {f.cargo:<15}")

    def listar_cardapio(self):
        if not self.cardapio:
            print("\nO cardápio está vazio no momento.")
            return

        print(f"\n--- CARDÁPIO ATUAL: {self.nome.upper()} ---")
        print(f"{'ID':<5} | {'PRATO':<25} | {'PREÇO':<10}")
        print("-" * 46)
        for p in self.cardapio:
            print(f"{p.id:<5} | {p.nome:<25} | R$ {p.preco:>7.2f}")


# --- FLUXO PRINCIPAL DO SISTEMA ---
def obter_input_valido(mensagem):
    """Garante que o usuário não envie campos em branco."""
    while True:
        entrada = input(mensagem).strip()
        if entrada:
            return entrada
        print("Erro: Este campo não pode ficar vazio. Tente novamente.")

nome_digitado = obter_input_valido("Digite o nome do seu restaurante: ")
restaurante = Restaurante(nome_digitado)

while True:
    print("\n" + "="*40)
    print(f"{restaurante.nome.upper():^40}")
    print("="*40)
    print(" [1] Cadastrar Novo Funcionário")
    print(" [2] Listar Funcionários Ativos")
    print(" [3] Adicionar Prato ao Cardápio")
    print(" [4] Visualizar Cardápio Completo")
    print(" [5] Sair do programa")
    print("="*40)

    opcao = input("Selecione uma opção: ").strip()

    if opcao == "1":
        print("\n--- CADASTRO DE FUNCIONÁRIO ---")
        nome = obter_input_valido("Nome do Funcionário: ")
        cargo = obter_input_valido("Cargo ocupado: ")
        restaurante.adicionar_funcionario(nome, cargo)

    elif opcao == "2":
        restaurante.listar_funcionarios()

    elif opcao == "3":
        print("\n--- CADASTRO DE PRATO ---")
        nome = obter_input_valido("Nome do Prato: ")
        
        while True:
            try:
                preco = float(input("Preço de venda (R$): "))
                if preco >= 0:
                    break
                print("O preço não pode ser um valor negativo.")
            except ValueError:
                print("Digite um valor numérico válido (use ponto para centavos).")
        
        restaurante.adicionar_prato(nome, preco)

    elif opcao == "4":
        restaurante.listar_cardapio()

    elif opcao == "5":
        print(f"\nDesconectando do sistema {restaurante.nome}... Volte sempre!")
        break

    else:
        print("\nOpção inválida. Escolha um número de 1 a 5.")
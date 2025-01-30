# Lista global para armazenar os clientes cadastrados
clientes = []

# Dicionário global para armazenar o histórico de transações de cada cliente (por CPF)
historico_transacoes = {}

# Função para formatar o CPF no padrão XXX.XXX.XXX-XX
def formatar_cpf(cpf):
    """
    Formata o CPF no padrão XXX.XXX.XXX-XX.

    Parâmetros:
        cpf (str): CPF apenas com números.

    Retorna:
        str: CPF formatado.
    """
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

# Função para adicionar um cliente
def adicionar_cliente():
    """
    Adiciona um cliente solicitando os dados pelo terminal.
    """
    print("\nAdicionando um novo cliente...")
    nome = input("Digite o nome do cliente: ")

    # Valida a entrada do CPF apenas com números
    while True:
        cpf = input("Digite o CPF do cliente (apenas números): ")
        if len(cpf) == 11 and cpf.isdigit():
            cpf = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Certifique-se de digitar 11 números.")

    # Verifica se o CPF já está cadastrado
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print("CPF já cadastrado. Use outro CPF.")
            return

    # Solicita a criação de uma senha
    while True:
        senha = input("Crie uma senha para sua conta: ")
        if len(senha) >= 4:
            break
        else:
            print("A senha deve ter pelo menos 4 caracteres.")

    # Gera um ID único baseado no tamanho da lista
    id_cliente = len(clientes) + 1

    # Cria um dicionário para representar o cliente
    cliente = {
        "id": id_cliente,
        "nome": nome,
        "cpf": cpf,
        "senha": senha,
        "saldo": 0.0  # Saldo inicial da conta
    }

    # Adiciona o cliente à lista global
    clientes.append(cliente)

    # Cria um histórico de transações vazio para o cliente
    historico_transacoes[cpf] = []

    print(f"Cliente {nome} adicionado com sucesso!\n")

# Função para adicionar dinheiro à conta
def adicionar_dinheiro():
    """
    Permite adicionar dinheiro à conta de um cliente mediante verificação de CPF e senha.
    """
    print("\nAdicionando dinheiro à conta...")

    # Verifica o CPF
    while True:
        cpf = input("Digite o CPF do cliente (apenas números): ")
        if len(cpf) == 11 and cpf.isdigit():
            cpf = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Certifique-se de digitar 11 números.")

    # Verifica se o cliente existe
    cliente = next((cliente for cliente in clientes if cliente["cpf"] == cpf), None)
    if not cliente:
        print("Cliente não encontrado. Verifique o CPF.")
        return

    # Solicita a senha
    senha = input("Digite a senha: ")
    if senha != cliente["senha"]:
        print("Senha incorreta. Operação cancelada.")
        return

    # Solicita o valor a ser depositado
    valor = float(input("Digite o valor a ser adicionado à conta: R$ "))
    if valor <= 0:
        print("Valor inválido. Insira um valor positivo.")
        return

    # Atualiza o saldo do cliente
    cliente["saldo"] += valor

    # Atualiza o histórico de transações
    historico_transacoes[cpf].append(f"Depósito de R${valor:.2f} realizado com sucesso.")

    print(f"Depósito de R${valor:.2f} registrado com sucesso!")
    print("Boleto enviado ao e-mail para depósito bancário.\n")

# Função para transferência de fundos
# Função para transferência de fundos
def transferencia_fundos():
    """
    Realiza uma transferência de fundos entre clientes.
    """
    print("\nIniciando transferência de fundos...")

    # Solicita o CPF de origem
    while True:
        cpf_origem = input("Digite o CPF do cliente de origem (apenas números): ")
        if len(cpf_origem) == 11 and cpf_origem.isdigit():
            cpf_origem = formatar_cpf(cpf_origem)
            break
        else:
            print("CPF inválido. Certifique-se de digitar 11 números.")

    # Solicita o CPF de destino
    while True:
        cpf_destino = input("Digite o CPF do cliente de destino (apenas números): ")
        if len(cpf_destino) == 11 and cpf_destino.isdigit():
            cpf_destino = formatar_cpf(cpf_destino)
            break
        else:
            print("CPF inválido. Certifique-se de digitar 11 números.")
    
    # Solicita o valor da transferência
    valor = float(input("Digite o valor a ser transferido: R$ "))
    if valor <= 0:
        print("Valor inválido. Insira um valor positivo.")
        return

    # Localiza os clientes na lista
    cliente_origem = next((cliente for cliente in clientes if cliente["cpf"] == cpf_origem), None)
    cliente_destino = next((cliente for cliente in clientes if cliente["cpf"] == cpf_destino), None)

    # Verifica se os clientes existem
    if not cliente_origem:
        print("Cliente de origem não encontrado. Verifique o CPF.")
        return
    if not cliente_destino:
        print("Cliente de destino não encontrado. Verifique o CPF.")
        return

    # Verifica a senha do cliente de origem
    senha = input("Digite a senha: ")
    if senha != cliente_origem["senha"]:
        print("Senha incorreta. Operação cancelada.")
        return

    # Realiza a transferência
    cliente_origem["saldo"] -= valor
    cliente_destino["saldo"] += valor

    # Atualiza o histórico de transações
    historico_transacoes[cpf_origem].append(f"Transferência enviada: R${valor:.2f} para {cliente_destino['nome']}.")
    historico_transacoes[cpf_destino].append(f"Transferência recebida: R${valor:.2f} de {cliente_origem['nome']}.")

    print(f"Transferência de R${valor:.2f} realizada com sucesso!")
    print(f"Novo saldo de {cliente_origem['nome']}: R${cliente_origem['saldo']:.2f}")
    print(f"Novo saldo de {cliente_destino['nome']}: R${cliente_destino['saldo']:.2f}\n")


   
# Função para exibir o histórico de transações de um cliente
def exibir_historico():
    """
    Exibe o histórico de transações de um cliente mediante verificação de CPF.
    """
    print("\nExibindo histórico de transações...")

    # CPF do cliente
    while True:
        cpf = input("Digite o CPF do cliente (apenas números): ")
        if len(cpf) == 11 and cpf.isdigit():
            cpf = formatar_cpf(cpf)
            break
        else:
            print("CPF inválido. Certifique-se de digitar 11 números.")

    # Verifica se o cliente existe
    if cpf not in historico_transacoes:
        print("Cliente não encontrado.")
        return

    # Exibe o histórico de transações
    print(f"Histórico de transações para o CPF {cpf}:")
    for transacao in historico_transacoes[cpf]:
        print(f"- {transacao}")
    print()

# Função principal para gerenciar o fluxo interativo
def menu_interativo():
    """
    Apresenta um menu interativo para gerenciar clientes e transações.
    """
    while True:
        print("Menu:")
        print("1. Adicionar cliente")
        print("2. Realizar transferência")
        print("3. Exibir histórico de transações")
        print("4. Adicionar dinheiro à conta")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_cliente()
        elif opcao == "2":
            transferencia_fundos()
        elif opcao == "3":
            exibir_historico()
        elif opcao == "4":
            adicionar_dinheiro()
        elif opcao == "5":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

# Executa o programa interativo
if __name__ == "__main__":
    menu_interativo()


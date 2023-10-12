
def menu():

    menu ="""\nQual acao voce ira executar hoje?
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Criar Conta
    [5] Listar Contas
    [6] Criar Usuario
    [0] Sair\n"""
    op = int(input(f"{menu}\nOpçao: "))

    return op

def deposito(valor, saldo, extrato):

    if valor <= 0 :
            print("Esse valor não pode ser depositado!!")

    else:
        print("Depositando....")
        saldo += valor
        extrato += f"\nDeposito de {valor:.2f}"
        print(f"Saldo total: {saldo}")
    return saldo, extrato


def saque(*, valor, saldo, extrato):

    n_saque = 0
    limite_saques = 3 
    limite = 501

    if valor < limite:
        if valor > saldo:
                print("Valor indiponivel")

        elif n_saque < limite_saques:
            print("Sancando.....")
            saldo -= valor
            n_saque += 1
            extrato += f"\nSaque de {valor:.2f}"
            print(f"Saldo atual: R${saldo}")
        else: 
                print("Numero de saque atingido")

    else:
            print('Valor não permitido, max 500')

    return saldo, extrato

def ex_extrato(saldo, /, *, extrato):
            
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo total: R$ {saldo:.2f}")

l_contas = list()

def criar_conta(agencia, numero_conta):
        conta = dict()
        
        while True:
            op = input("deseja criar??S/N: ").upper()
            if op == "S":
                agencia += 1
                numero_conta += 1
                cpf = conta["cpf"] = input("cpf:")
                conta["agencia"] = agencia
                conta["numero_conta"] = numero_conta
                v = verificar_cpf(cpf= cpf, clientes= l_contas)
                if v == "v":
                    print("cpf existente")
                    break
                else:
                    l_contas.append(conta.copy())
                    print("conta criada!!")
            else:
                break

        return agencia, numero_conta
                
def listar_conta(contas= l_contas):
    print(contas)
    for conta in l_contas:
        linha = f"""Agência: {conta['agencia']}\nC/C: {conta['numero_conta']}\nTitular:{conta['cpf']}"""
        print(linha)


def verificar_cpf(cpf, clientes):

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return "v"
        else:
            continue
        


def criar_cliente():
    clientes = list()
    cliente = dict()

    while True:
            cliente.clear()
            op = input("vamos continuar?? S/N: ").upper()
            if op == "S":
                cliente["nome"] = str(input("Qual o seu nome? "))
                cpf = cliente["cpf"] = str(input("Seu cpf: "))
                v = verificar_cpf(cpf=cpf, clientes= clientes)
                if v == "v":
                    print("cpf existe")
                    print(clientes)
                    break
                clientes.append(cliente.copy())
            else:
                break
    

def main():
    
    extrato = ""
    saldo = 0
    opcao = 0

    while True:

        opcao = menu()
        agencia = 0000
        numero_conta = 00

        if opcao == 1:
            valor = float(input("\nqual valor sera depositado?? R$ "))
            saldo, extrato = deposito(valor= valor, saldo= saldo, extrato= extrato)

        elif opcao == 2 :
            valor = float(input("Qual o valor de saque? "))
            saldo, extrato = saque(valor= valor, saldo= saldo, extrato=extrato)
        

        elif opcao == 3:
            ex_extrato(saldo, extrato= extrato)

        elif opcao == 4:
            criar_conta(agencia= agencia, numero_conta = numero_conta)

        elif opcao == 5:
            listar_conta()
        
        elif opcao == 6:
            criar_cliente()

        else:
            print("Saindo.....")
            break

    print("Execucao finalizada, ate logo")

main()
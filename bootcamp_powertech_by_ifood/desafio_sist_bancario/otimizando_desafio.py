
n_deposito = 0
n_saque = 0
extrato = ""
saldo = 3000.00
opcao = 0

menu = """\nQual acao voce ira executar hoje?
[1] Deposito
[2] Saque
[3] Extrato
[0] Sair\n
"""

def deposito(valor_deposito: float):

    if valor_deposito <= 0 :
            print("Esse valor não pode ser depositado!!")

    else:
        print("Depositando....")


def saque(valor_saque, saldo = saldo, saque= n_saque):

    if valor_saque < 501:
        if valor_saque > saldo:
                print("Valor indiponivel")

        elif saque < 3 :
            print("Sancando.....")
            saque += 1
        else: 
                print("Numero de saque atingido")

    else:
            print('Valor não permitido, max 500')

def extrato():
        print(f"""\nForam executados: \n
            {n_deposito} Depositos\n
            {n_saque} Saques de no maximo R$500,00\n
            Saldo atual: R$ {saldo:.2f}""")

while True:

    opcao = int(input(menu + "Opcao: "))

    if opcao == 1:
        valor_deposito = float(input("\nqual valor sera depositado?? R$ "))
        deposito(valor_deposito=valor_deposito)
        saldo += valor_deposito
        n_deposito +=1
        print(f"total na conta: {saldo:.2f}")



    elif opcao == 2 :
        valor_saque = float(input("Qual o valor de saque? "))
        saque(valor_saque=valor_saque)
        saldo -= valor_saque
        n_saque += 1
        print(f"Saldo: {saldo:.2f}")
    

    elif opcao == 3:
        extrato()

    else:
        print("Saindo.....")
        break

print("Execucao finalizada, ate logo")
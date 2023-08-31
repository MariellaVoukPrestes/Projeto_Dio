
#Neste projeto, você terá a oportunidade de criar um Sistema Bancário em Python.
#O objetivo é implementar três operações essenciais: depósito, saque e extrato.
#O sistema será desenvolvido para um banco que busca monetizar suas operações. 
#Durante o desafio, você terá a chance de aplicar seus conhecimentos em programação Python e criar um 
#sistema funcional que simule as operações bancárias. Prepare-se para aprimorar suas habilidades e 
#demonstrar sua capacidade de desenvolver soluções práticas e eficientes.


#operacao deposito
deposito = 0
saque = 0
extrato = ""
saldo = 3000
opcao = 0

menu = """Qual acao voce ira executar hoje?
[1] Deposito
[2] Saque
[3] Extrato
[0] Sair
"""

opcao = int(input(menu + "Opcao: "))

while opcao != 0:
    if opcao == 1:
        valor_deposito = int(input("qual valor sera depositado??  "))
        if valor_deposito <= 0 :
            print("Esse valor não pode ser depositado!!")
            continue
        else:
            saldo += valor_deposito
            deposito +=1
            print("Depositando....")
            print(f"{saldo}")
            opcao = int(input(menu + "Opcao: "))

            

    elif opcao == 2 :
        valor_saque = int(input("Qual o valor de saque? "))
        if valor_saque < 500:
    
            if valor_saque > saldo:
                print("Valor indiponivel")
                opcao = int(input(menu + "Opcao: "))


            elif saque < 3 :
                print("Sancando.....")
                saque += 1
                saldo -= valor_saque
                print(f"{saldo}")
                opcao = int(input("Proxima execução: "))

            else: 
                print("Numero de saque atingido")
                opcao = int(input(menu + "Opcao: "))


        else:
            print('Valor não permitido, max 500')
            opcao = int(input(menu + "Opcao: "))


    elif opcao == 3:
        print(f"Foram executados: \n{deposito} Depositos\n{saque} Saques de no maximo R$500,00\nSaldo atual: R${saldo:2f}")
        opcao = int(input(menu + "Opcao: "))
        
    else:
        print("Saindo.....")
        opcao = int(input(menu + "Opcao: "))

print("fim")
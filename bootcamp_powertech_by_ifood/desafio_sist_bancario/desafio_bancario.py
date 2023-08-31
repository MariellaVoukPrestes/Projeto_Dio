
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

while True:

    opcao = int(input(menu + "Opcao: "))

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

    elif opcao == 2 :
        valor_saque = int(input("Qual o valor de saque? "))
        if valor_saque < 500:
    
            if valor_saque > saldo:
                print("Valor indiponivel")


            elif saque < 3 :
                print("Sancando.....")
                saque += 1
                saldo -= valor_saque
                print(f"{saldo}")

            else: 
                print("Numero de saque atingido")

        else:
            print('Valor não permitido, max 500')

    elif opcao == 3:

        print(f"Foram executados: \n{deposito} Depositos\n{saque} Saques de no maximo R$500,00\nSaldo atual: R${saldo:.2f}")
        
    else:
        print("Saindo.....")
        break

print("fim")
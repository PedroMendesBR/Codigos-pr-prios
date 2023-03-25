print(
    """""
    ------------- MENU --------------------

    [1] - Depositar
    [2] - sacar
    [3] - extrato
    [4] - sair

    ---------------------------------------
    
    """""
)

saldo = 0
limite_por_saque = 500
deposito = 0
saque = 0
extrato = [""]
LIMITE_DE_SAQUE = 0

opcao = int(input("Qual operação deseja fazer? \n"))

while True:
    if opcao == 1:
        print("Depósito \n")
        deposito = float(input("Qual valor deseja depositar? \n"))
        while deposito < 1:
            print("O valor depositado não pode ser menor que 1! \n")
            deposito = float(input("Digite um valor positivo para seu depósito! \n"))
        if deposito > 1:
            saldo = saldo + deposito
            extrato.append(deposito)
            print("Você depositou", deposito, "seu saldo agora é de: \n", saldo)
            opcao = int(input("Deseja efetuar outra operação? [1] Depósito / [2] Saque / [3] Extrato / [4] Sair \n"))

    elif opcao == 2:
        print("Saque \n")
        saque = float(input("Qual valor você deseja sacar? \n"))
        if saldo >= saque:
            while saque > 500:
                    print("Você pode sacar até 500 reais por saque: \n")
                    saque = float(input("Digite um valor menor ou igual a 500: \n"))
            LIMITE_DE_SAQUE = LIMITE_DE_SAQUE + 1

            if LIMITE_DE_SAQUE > 3:
                print("Você já alcançou seu limite de saques diários de apenas três saques.")
                opcao = int(input("Deseja efetuar outra operação? [1] Depósito / [2] Saque / [3] Extrato / [4] Sair \n"))
            else:   
                saldo = saldo - saque
                extrato.append(-saque)
                print("Você sacou ", saque, "seu saldo agora é de: \n", saldo) 
                opcao = int(input("Deseja efetuar outra operação? [1] Depósito / [2] Saque / [3] Extrato / [4] Sair \n"))
        else:
            print("Seu saldo é insuficiente! \n") 
            opcao = int(input("Deseja efetuar outra operação? [1] Depósito / [2] Saque / [3] Extrato / [4] Sair \n"))
           
    elif opcao == 3:
        deposito = "R${:.2f}".format(deposito)
        saque = "R$ {:.2f}".format(saque)
        saldo = "R$ {:.2f}".format(saldo)
        print(extrato)
        extrato.append(print("seu saldo é de: \n",saldo))
        opcao = int(input("Deseja efetuar outra operação? [1] Depósito / [2] Saque / [3] Extrato / [4] Sair \n"))
        
    elif opcao == 4:
        print("Obrigado por utilizar nosso sistema! \n")
        break
    else: 
        print("Operação inválida! Digite uma opção válida")    

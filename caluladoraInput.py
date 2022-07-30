def calculador(num1, num2, op):
    if(op == 1):
        return num1 + num2
    elif(op == 2):
        return num1 - num2
    elif(op == 3):
        return num1 * num2
    elif(op == 4):
        return num1 / num2
    else:
        print("Essa opção não existe")

while(True):
    operacao = 10
    while(True):
        print(" 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")
        operacao = int(input("Digite a operação desejada: "))

        if not(operacao >= 0 and operacao <= 4):
            print("\nEssa opção não existe\n")
        if(operacao >= 0 and operacao <= 4):
            break
        if(operacao == 0):
            break
    if(operacao == 0):
        break

    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    resultado = calculador(numero1, numero2, operacao)


    print(f" \n Resultado: {resultado} \n")
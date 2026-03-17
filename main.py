num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = input("Digite a operacao (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    if num2 == 0:
        print("Erro: divisao por zero.")
    else:
        resultado = num1 / num2
else:
    print("Operacao invalida.")
    resultado = None

if resultado is not None:
    print(f"Resultado: {resultado}")

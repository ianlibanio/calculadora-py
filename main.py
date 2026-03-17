while True:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))
    except ValueError:
        print("Entrada invalida. Digite apenas numeros.")
        continue

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
            continue
        resultado = num1 / num2
    else:
        print("Operacao invalida.")
        continue

    print(f"Resultado: {resultado}")

    continuar = input("Deseja fazer outra conta? (s/n): ").strip().lower()
    if continuar != "s":
        print("Encerrando calculadora...")
        break

def calcular(num1, num2, operador):
    if operador == "+":
        return num1 + num2
    if operador == "-":
        return num1 - num2
    if operador == "*":
        return num1 * num2
    if operador == "/":
        if num2 == 0:
            raise ZeroDivisionError("Divisao por zero nao permitida.")
        return num1 / num2
    raise ValueError("Operacao invalida.")


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")


def main():
    print("Calculadora - Fase 3")

    while True:
        num1 = ler_numero("Digite o primeiro numero: ")
        num2 = ler_numero("Digite o segundo numero: ")
        operador = input("Digite a operacao (+, -, *, /): ").strip()

        try:
            resultado = calcular(num1, num2, operador)
            print(f"Resultado: {resultado}")
        except (ValueError, ZeroDivisionError) as erro:
            print(f"Erro: {erro}")

        continuar = input("Deseja continuar? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break


if __name__ == "__main__":
    main()


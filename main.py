def calcular(num1, num2, operador):
    operacoes = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }

    if operador not in operacoes:
        raise ValueError("Operacao invalida.")

    if operador == "/" and num2 == 0:
        raise ZeroDivisionError("Divisao por zero nao permitida.")

    return operacoes[operador](num1, num2)


def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada invalida. Digite um numero valido.")


def mostrar_historico(historico):
    if not historico:
        print("Historico vazio.")
        return

    print("\nHistorico de operacoes:")
    for item in historico:
        print(item)
    print()


def main():
    historico = []

    while True:
        print("\n=== Calculadora - Fase 4 ===")
        print("1. Nova operacao")
        print("2. Ver historico")
        print("3. Sair")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            num1 = ler_numero("Digite o primeiro numero: ")
            num2 = ler_numero("Digite o segundo numero: ")
            operador = input("Digite a operacao (+, -, *, /): ").strip()

            try:
                resultado = calcular(num1, num2, operador)
                registro = f"{num1} {operador} {num2} = {resultado}"
                historico.append(registro)
                print(f"Resultado: {resultado}")
            except (ValueError, ZeroDivisionError) as erro:
                print(f"Erro: {erro}")

        elif opcao == "2":
            mostrar_historico(historico)

        elif opcao == "3":
            print("Encerrando calculadora...")
            break

        else:
            print("Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()

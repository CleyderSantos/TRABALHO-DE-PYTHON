def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero!"
    else:
        return x / y

def exibir_menu():
    print("\nSelecione a operação:")
    print("1. Adicionar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

def calcular():
    while True:
        exibir_menu()
        opcao = input("Digite o número da operação desejada: ")

        if opcao == '5':
            print("Obrigado por usar a calculadora. Até logo!")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                if opcao == '1':
                    print("Resultado:", adicionar(num1, num2))
                elif opcao == '2':
                    print("Resultado:", subtrair(num1, num2))
                elif opcao == '3':
                    print("Resultado:", multiplicar(num1, num2))
                elif opcao == '4':
                    print("Resultado:", dividir(num1, num2))
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")
        else:
            print("Opção inválida. Por favor, escolha uma opção de 1 a 5.")

if __name__ == "__main__":
    calcular()
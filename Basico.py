# Criando as funções

def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divisao(a, b):
    if b != 0:
        return a / b
    else:
        print("Erro: divisão por zero!\n")
        return 0


def multiplicacao(a, b):
    return a * b


# Ajustando as opções
print(" ====== [ CALCULADORA ] ====== \n")
print(" ========== [ MENU ] ========= \n")
print(" [1] = SOMA \n")
print(" [2] = SUBTRAÇÃO \n")
print(" [3] = DIVISÃO \n")
print(" [4] = MULTIPLICAÇÃO \n")
print(" [0] = SAIR \n")

# Verificando se a opção é verdadeira
try:
    Op = int(input("Digite sua opção: "))
    print("\n")

    if Op == 0:
        print("Programa encerrado!!")

    elif 1 <= Op <= 4:
        N1 = float(input("Digite o primeiro número: "))
        N2 = float(input("Digite o segundo número: "))

        match Op:
            case 1:
                operador = "soma"
                resultado = soma(N1, N2)
            case 2:
                operador = "subtração"
                resultado = subtracao(N1, N2)
            case 3:
                operador = "divisão"
                resultado = divisao(N1, N2)
            case 4:
                operador = "multiplicação"
                resultado = multiplicacao(N1, N2)

        print(f"O resultado da {operador} entre {N1} e {N2} é: {resultado}")

    else:
        print("Opção inválida!!")

except ValueError:
    print("Você digitou um valor inválido!")

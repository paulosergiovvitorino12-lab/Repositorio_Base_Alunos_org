# Funções das operações básicas

def somar(n1, n2):
    return n1 + n2


def multiplicar(n1, n2):
    return n1 * n2


def subtrair(n1, n2):
    return n1 - n2


# Boa prática (evitar erro)
def divisao(n1, n2):
    if n2 == 0:
        return "Erro: divisão por zero"
    return n1 / n2


def calcular(n1, n2, operacao):
    if operacao == "+":
        return somar(n1, n2)
    elif operacao == "-":
        return subtrair(n1, n2)
    elif operacao == "*":
        return multiplicar(n1, n2)
    elif operacao == "/":
        return divisao(n1, n2)
    else:
        return "Operação invalida"
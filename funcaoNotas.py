def lerNotas():
    nota = float(input("Digite a nota: "))
    return nota

def calcMedia(n1, n2):
    soma = n1 + n2
    media = soma / 2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, "Resultado: ", end="")
    if media > 7:
        print("Aprovado")
    else:
        print("Reprovado")

a = lerNotas()
b = lerNotas()
calcMedia(a, b)
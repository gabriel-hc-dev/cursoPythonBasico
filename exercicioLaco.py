qtd = 0
soma = 0
media = 0
n1 = float(input("Digite um valor (para encerrar, digie um valor negativo: "))

while(n1 > 0.0):
    soma = soma + n1
    qtd = qtd + 1
    n1 = float(input("Digite um valor (para encerrar, digie um valor negativo): "))

media = soma / qtd
print("Soma: ", soma)
print("Média: ", media)
print("Quantidade de valores digitados: ", qtd)
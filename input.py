cod = int(input("Insira seu código: "))
nome = input("Insira seu nome: ")
salario = float(input("Insira seu salário (usando o ponto): "))
status = int(input("Digite 0 para Inativo e 1 para Ativo: "))

if(status == 0):
    status = "Inativo"
if(status == 1):
    status = "Ativo"

print("Código: %d "% cod)
print("Nome: %s "% nome)
print("Salário: %2.f "% salario)
print("Status: %d "% status)
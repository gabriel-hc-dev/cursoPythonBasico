cod = 105
nome = "José Junqueira Júnior"
salario = 1650.00
status = True

if(status == False):
    status = "Inativo"
else:
    status = "Ativo"

print("Código: %d "% cod)
print("Nome: %s "% nome)
print("Salário: %2.f "% salario)
print("Status: %r "% status)
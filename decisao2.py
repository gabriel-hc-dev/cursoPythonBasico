a = int(input("Digite um valor de a: "))
b = int(input("Digite um valor de b: "))

if(a>b):
    aux=a;
    a=b;
    b=aux;
print("Valor de a:", a);
print("Valor de b:", b);
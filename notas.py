n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
media = (n1+n2) / 2

if(media >= 6):
    print("Aprovado, com %.1f"% media,"de média")
else:
    print("Reprovado, com %.1f"% media,"de média")
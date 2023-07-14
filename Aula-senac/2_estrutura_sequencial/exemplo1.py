media = float(input("Qual a media: "))
aprovado = media >= 70
reprovado = media < 30

if aprovado:
    print("Parabens, vc foi aprovado!")
elif reprovado:
    print('reprovado')
else:
    print("4º prova")
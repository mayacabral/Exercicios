#Faça um programa para imprimir:
#   1
#   2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

def questao1(numero):
    resultado = ""
    for n in range(1, numero + 1):
            #range(início, fim, passo) inicio: o valor inicial da sequencia; fim: o valor final da sequencia;passo: o tamanho do incremento.
        for i in range(1, n + 1):
            resultado += f"{str(n)}"
        resultado += '\n'
    return resultado

print(questao1(int(input("Entre com um número"))))

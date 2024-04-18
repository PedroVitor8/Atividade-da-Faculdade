def calcula_soma_digitos(numero):
    if len(numero) == 0:
        return 0
    else:
        return numero % 10 + calcula_soma_digitos(numero//10)

numero = int(input("Digite um número: "))
print(calcula_soma_digitos(numero))
def encontrar_anagramas(palavra):
    if len(palavra) <= 1:
        return [palavra]
    else:
        lista = []
        for i in encontrar_anagramas(palavra[1:]):
            for e in range(len(i) + 1):
                lista.append(i[:e] + palavra[0] + i[e:])
        return lista

palavra = input("Digite uma palavra: ")
print(encontrar_anagramas(palavra))
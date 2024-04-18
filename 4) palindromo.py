def inverter_string(palavra):
    if len(palavra) == 0:
        return palavra
    else:
        return palavra[-1] + inverter_string(palavra[:-1])

palavra = input("Digite uma palavra para verificar: ")
if palavra == inverter_string(palavra):
    print(palavra, 'é um palindromo')
else:
    print(palavra, 'não é um palindromo')
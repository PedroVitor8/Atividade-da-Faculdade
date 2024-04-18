def potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * potencia(x, n-1)

x, n = 2, 10
print(potencia(x, n))
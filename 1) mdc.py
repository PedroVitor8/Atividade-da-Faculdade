def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a%b)
a, b = 15, 10
print(mdc(a, b))
gerador = (i ** 2 for i in range(10) if i % 2 == 0)
a = next(gerador)
print(next(gerador))
b = next(gerador)
print(a)
print(b)

print('-------------')
for numero in gerador:
    print(numero)

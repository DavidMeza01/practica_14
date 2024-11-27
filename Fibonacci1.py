print("David Meza Rincon y gonzales muños jose fernando")
limite = int(input("Ingresa el número de términos para la serie de Fibonacci: "))
x, y = 0, 1
print(x, end=" ")
if limite > 1:
    print(y, end=" ")
    for _ in range(2, limite):
        x, y = y, x + y
        print(y, end=" ")
print()  
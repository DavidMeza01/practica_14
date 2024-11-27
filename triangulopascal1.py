def generar_triangulo_pascal(filas):
    triángulo = []  
    
    for n in range(filas):
        fila = [1] * (n + 1) 
    
        for k in range(1, n):
            fila[k] = triángulo[n-1][k-1] + triángulo[n-1][k]
        triángulo.append(fila)  
    
    return triángulo

def mostrar_triangulo_pascal(triángulo):
    for fila in triángulo:
        print(" ".join(map(str, fila)).center(len(triángulo[-1])*3))


filas = int(input("Introduce el número de filas del Triángulo de Pascal: "))
triángulo = generar_triangulo_pascal(filas)
mostrar_triangulo_pascal(triángulo)
print ("Hecho Por David Meza Rincon y gonzales muños jose fernando")
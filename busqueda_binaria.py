def busqueda_binaria (objetivo, epsilon):
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2
    intento = 0
    # absoluto = abs(respuesta**2 - objetivo)
    # print(f'absoluto: {absoluto}')

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'intentos= {intento} : bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta
        intento += 1
        respuesta = (alto + bajo) / 2   

        print(f'La raiz cuadrada de {objetivo} es {respuesta}')  

if __name__ == '__main__':
    busqueda_binaria(9, 0.0001)
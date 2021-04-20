def enumeracion_exhaustiva(objetivo):
    respuesta = 0

    while respuesta ** 2 < objetivo:
        print(respuesta)
        respuesta += 1

    if respuesta ** 2 == objetivo:
        print(f'la raiz de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada exacta.')

if __name__ == '__main__':
    enumeracion_exhaustiva(25)
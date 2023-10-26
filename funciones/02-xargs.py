def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)

# keywords argumens como empaquetar todos los parametros


suma(2, 5, 8)
suma(2, 5)
suma(2, 5, 21, 25)

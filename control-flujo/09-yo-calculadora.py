print("Bienvenidos a mi calculadora")
print("las operaciones son:")
print("suma,resta,multiplicar y dividir")


resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese un numero: ")
        if resultado.lower() == "salir":
            break

        resultado = int(resultado)

    opcion = input("elija una operacion: ")
    if opcion.lower() == "salir":
        break

    n2 = input("Ingresa segundo numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if opcion.lower() == "suma":
        resultado += n2

    elif opcion.lower() == "resta":
        resultado -= n2

    elif opcion.lower() == "multiplicar":
        resultado *= n2

    elif opcion.lower() == "dividir":
        resultado /= n2

    else:
        print("Opcion no valida")
        break

    print(f"""el resultado es {resultado}""")

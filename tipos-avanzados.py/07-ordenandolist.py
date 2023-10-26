numeros = [2, 6, 4, 88, 66, 77, 85, 92]

# sort ordena lista
# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True)  # nueva lista sorted
print(numeros)
print(numeros2)

usuarios = [["carlitos", 4],
            ["felipe", 1],
            ["pulga", 5]
            ]


# def ordena(elemento):
#     return elemento[1]


# usuarios.sort(key=ordena, reverse=True)

usuarios.sort(key=lambda el: el[1])
# lambda se utiliza unicamente si utilizare una funcion solo una vez

print(usuarios)

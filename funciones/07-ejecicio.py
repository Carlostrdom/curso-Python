def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_invertido = ""
    for char in texto:
        texto_al_invertido = char + texto_al_invertido
    return texto_al_invertido


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_invertido = reverse(texto)
    return texto.lower() == texto_al_invertido.lower()

    # texto = texto.replace(" ", "").lower()
    # return texto == texto[::-1]


print(es_palindromo("amo la paloma"))
print(es_palindromo("hola mundo"))
print(es_palindromo("reconocer"))

def cifrar_cesar(texto, clave):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            if caracter.isupper():
                resultado += chr((ord(caracter) + clave - 65) % 26 + 65)
            else:
                resultado += chr((ord(caracter) + clave - 97) % 26 + 97)
        else:
            resultado += caracter
    return resultado

def cifrar_rot26(texto):
    return cifrar_cesar(texto, 13)

def cifrar_rot13(texto):
    return cifrar_cesar(texto, 13)

def cifrar_rot18(texto):
    return cifrar_cesar(texto, 18)

def cifrar_rot26(texto):
    return cifrar_cesar(texto, 26)

mensaje_original = "Marco Antonio Prada"
print(f'Mensaje original: {mensaje_original}')

# Cifrado César con clave 3
mensaje_cifrado_rot3 = cifrar_cesar(mensaje_original, 3)
print(f'Cifrado César ROT3: {mensaje_cifrado_rot3}')

# Cifrado ROT13
mensaje_cifrado_rot13 = cifrar_rot13(mensaje_original)
print(f'Cifrado ROT13: {mensaje_cifrado_rot13}')

# Cifrado ROT18
mensaje_cifrado_rot18 = cifrar_rot18(mensaje_original)
print(f'Cifrado ROT18: {mensaje_cifrado_rot18}')

# Cifrado ROT26
mensaje_cifrado_rot26 = cifrar_rot26(mensaje_original)
print(f'Cifrado ROT26: {mensaje_cifrado_rot26}')

import sys

def cifrar_cesar(texto, desplazamiento):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    corrimiento_efectivo = desplazamiento % 26
    texto_cifrado = ""
    
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            posicion_actual = ord(caracter) - ord('A')
            nueva_posicion = (posicion_actual + corrimiento_efectivo) % 26
            nuevo_caracter = chr(ord('A') + nueva_posicion)
            texto_cifrado += nuevo_caracter
        else:
            texto_cifrado += caracter
    
    return texto_cifrado

def descifrar_cesar(texto_cifrado, desplazamiento):
    return cifrar_cesar(texto_cifrado, -desplazamiento)

def main():
    if len(sys.argv) != 3:
        print("Uso: python cesar.py \"texto\" desplazamiento")
        return
    
    texto = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")
        return
    
    texto_cifrado = cifrar_cesar(texto, desplazamiento)
    print(f"{texto_cifrado}")

if __name__ == "__main__":
    main()
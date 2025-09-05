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

def descifrar_cesar(texto, desplazamiento):
    """Descifra texto usando cifrado César"""
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    corrimiento_efectivo = desplazamiento % 26
    texto_descifrado = ""
    
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            posicion_actual = ord(caracter) - ord('A')
            nueva_posicion = (posicion_actual - corrimiento_efectivo) % 26
            nuevo_caracter = chr(ord('A') + nueva_posicion)
            texto_descifrado += nuevo_caracter
        else:
            texto_descifrado += caracter
    
    return texto_descifrado

def main():
    if len(sys.argv) != 3:
        print("Uso: python cesar.py \"texto\" desplazamiento")
        print("Ejemplo: python cesar.py \"LARYCXPAJORJ H BNPDARMJM NW ANMNB\" 9")
        return
    
    texto = sys.argv[1]
    try:
        desplazamiento = int(sys.argv[2])
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")
        return
    
    # Mostrar tanto cifrado como descifrado
    texto_cifrado = cifrar_cesar(texto, desplazamiento)
    texto_descifrado = descifrar_cesar(texto, desplazamiento)
    
    print(f"Texto original: {texto}")
    print(f"Cifrado (+{desplazamiento}): {texto_cifrado}")
    print(f"Descifrado (-{desplazamiento}): {texto_descifrado}")

if __name__ == "__main__":
    main()
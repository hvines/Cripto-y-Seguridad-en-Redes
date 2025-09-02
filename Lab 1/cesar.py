import sys

def cifrar_cesar(texto, desplazamiento):
    """
    Cifra un texto utilizando el algoritmo César.
    
    Parámetros:
    - texto (str): El texto a cifrar
    - desplazamiento (int): El corrimiento de caracteres
    
    Reglas:
    1) El corrimiento se aplica únicamente sobre las letras mayúsculas A-Z
    2) Los caracteres que no estén en A-Z quedan sin cambios
    3) El corrimiento se hace tomando como referencia los primeros 26 caracteres de Base64
    4) Si desplazamiento > 25, se calcula como desplazamiento % 26
    
    Retorna:
    - str: El texto cifrado
    """
    # Los primeros 26 caracteres de la tabla Base64 son:
    # ABCDEFGHIJKLMNOPQRSTUVWXYZ

    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Calcular el corrimiento efectivo
    corrimiento_efectivo = desplazamiento % 26
    
    texto_cifrado = ""
    
    for caracter in texto:
        # Solo procesar letras mayúsculas A-Z
        if caracter in base64_chars:
            # Encontrar la posición del carácter en el alfabeto
            posicion_actual = base64_chars.index(caracter)
            # Aplicar el corrimiento con módulo para manejar el wrap-around
            nueva_posicion = (posicion_actual + corrimiento_efectivo) % 26
            # Obtener el nuevo carácter
            nuevo_caracter = base64_chars[nueva_posicion]
            texto_cifrado += nuevo_caracter
        else:
            # Los caracteres que no están en A-Z quedan sin cambios
            texto_cifrado += caracter
    
    return texto_cifrado


def descifrar_cesar(texto_cifrado, desplazamiento):
    """
    Descifra un texto que fue cifrado con el algoritmo César.
    
    Parámetros:
    - texto_cifrado (str): El texto cifrado
    - desplazamiento (int): El corrimiento original usado para cifrar
    
    Retorna:
    - str: El texto descifrado
    """
    # Para descifrar, aplicamos el corrimiento en sentido contrario
    return cifrar_cesar(texto_cifrado, -desplazamiento)


def main():
    """
    Función principal para usar desde línea de comandos.
    Uso: python cesar.py "texto" desplazamiento
    """
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
    print(f"Texto cifrado: '{texto_cifrado}'")
    
    texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
    print(f"Texto descifrado: '{texto_descifrado}'")


if __name__ == "__main__":
    main()
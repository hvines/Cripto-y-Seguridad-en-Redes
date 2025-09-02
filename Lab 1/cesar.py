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
    Función principal para probar el algoritmo César.
    """
    print("=== Algoritmo de Cifrado César ===\n")
    
    # Ejemplos de prueba
    ejemplos = [
        ("HOLA MUNDO", 3),
        ("PYTHON ES GENIAL", 5),
        ("ABC XYZ 123", 1),
        ("TEXTO CON SIMBOLOS!", 10),
        ("CORRIMIENTO MAYOR", 30)  # Para probar módulo 26
    ]
    
    for texto, desplazamiento in ejemplos:
        print(f"Texto original: '{texto}'")
        print(f"Desplazamiento: {desplazamiento}")
        
        texto_cifrado = cifrar_cesar(texto, desplazamiento)
        print(f"Texto cifrado: '{texto_cifrado}'")
        
        texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
        print(f"Texto descifrado: '{texto_descifrado}'")
        
        # Verificar que el descifrado es correcto
        if texto == texto_descifrado:
            print("✓ Verificación exitosa")
        else:
            print("✗ Error en la verificación")
        
        print("-" * 50)
    
    # Modo interactivo
    print("\n=== Modo Interactivo ===")
    try:
        while True:
            texto = input("\nIngrese el texto a cifrar (o 'salir' para terminar): ")
            if texto.lower() == 'salir':
                break
            
            desplazamiento = int(input("Ingrese el desplazamiento: "))
            
            texto_cifrado = cifrar_cesar(texto, desplazamiento)
            print(f"Texto cifrado: '{texto_cifrado}'")
            
            # Opción para descifrar
            opcion = input("¿Desea descifrar el texto? (s/n): ")
            if opcion.lower() == 's':
                texto_descifrado = descifrar_cesar(texto_cifrado, desplazamiento)
                print(f"Texto descifrado: '{texto_descifrado}'")
    
    except KeyboardInterrupt:
        print("\n\nPrograma terminado por el usuario.")
    except ValueError:
        print("Error: El desplazamiento debe ser un número entero.")


if __name__ == "__main__":
    main()
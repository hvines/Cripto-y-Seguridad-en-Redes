import sys
import struct

class Colors:
    GREEN = '\033[92m'
    RESET = '\033[0m'

def leer_pcapng(archivo_pcapng):
    caracteres = []
    
    try:
        with open(archivo_pcapng, 'rb') as f:
            data = f.read()
            pos = 0
            
            while pos < len(data):
                if pos + 12 > len(data):
                    break
                
                block_type = struct.unpack('<I', data[pos:pos+4])[0]
                block_length = struct.unpack('<I', data[pos+4:pos+8])[0]
                
                if block_length < 12 or pos + block_length > len(data):
                    break
                
                if block_type == 0x00000006:
                    if block_length >= 32:
                        epb_start = pos + 8
                        captured_len = struct.unpack('<I', data[epb_start+12:epb_start+16])[0]
                        packet_start = epb_start + 20
                        packet_data = data[packet_start:packet_start + captured_len]
                        
                        caracter = extraer_caracter(packet_data)
                        if caracter:
                            caracteres.append(caracter)
                
                pos += block_length
    except:
        pass
    
    return caracteres

def extraer_caracter(packet_data):
    try:
        if len(packet_data) < 42:
            return None
        
        eth_type = struct.unpack('!H', packet_data[12:14])[0]
        if eth_type != 0x0800:
            return None
        
        ip_version = packet_data[14] >> 4
        if ip_version != 4:
            return None
        
        ip_header_len = (packet_data[14] & 0x0F) * 4
        ip_protocol = packet_data[23]
        ip_dst = packet_data[30:34]
        
        if ip_protocol != 1 or ip_dst != bytes([8, 8, 8, 8]):
            return None
        
        icmp_start = 14 + ip_header_len
        if len(packet_data) < icmp_start + 8:
            return None
        
        icmp_type = packet_data[icmp_start]
        if icmp_type != 8:
            return None
        
        icmp_payload = packet_data[icmp_start + 8:]
        if len(icmp_payload) == 0:
            return None
        
        ultimo_byte = icmp_payload[-1]
        
        if 32 <= ultimo_byte <= 126:
            caracter = chr(ultimo_byte)
            if 'a' <= caracter <= 'z':
                caracter = caracter.upper()
            return caracter
        
        return None
    except:
        return None

def descifrar_cesar(texto, desplazamiento):
    resultado = ""
    for caracter in texto:
        if 'A' <= caracter <= 'Z':
            posicion = ord(caracter) - ord('A')
            nueva_posicion = (posicion - desplazamiento) % 26
            resultado += chr(ord('A') + nueva_posicion)
        else:
            resultado += caracter
    return resultado

def contar_palabras_validas(texto):
    palabras_validas = {
        'criptografia', 'seguridad', 'redes', 'en', 'y'
    }
    
    palabras = texto.lower().split()
    contador = 0
    for palabra in palabras:
        palabra_limpia = ''.join(c for c in palabra if c.isalpha())
        if palabra_limpia in palabras_validas:
            contador += 1
    return contador

def main():
    if len(sys.argv) != 2:
        print("Uso: python pcap_native_decoder.py archivo.pcapng")
        return
    
    caracteres = leer_pcapng(sys.argv[1])
    
    if not caracteres:
        print("No se encontraron caracteres")
        return
    
    texto_original = ''.join(caracteres)
    print(f"Texto original extraído: {texto_original}")
    
    mejor_puntuacion = 0
    mejor_indice = -1
    resultados = []
    
    for corrimiento in range(26):
        texto_descifrado = descifrar_cesar(texto_original, corrimiento)
        resultados.append((corrimiento, texto_descifrado))
        
        puntuacion = contar_palabras_validas(texto_descifrado)
        if puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            mejor_indice = corrimiento
    
    for corrimiento, texto in resultados:
        if corrimiento == mejor_indice and mejor_puntuacion > 0:
            print(f"{Colors.GREEN}{corrimiento}\t\t{texto}{Colors.RESET}")
        else:
            print(f"{corrimiento}\t\t{texto}")

if __name__ == "__main__":
    main()
class NodoHuffman:
    def __init__(self, valor, frecuencia):
        self.valor = valor
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

def construir_arbol_huffman(tabla_frecuencias):
    nodos = [NodoHuffman(jeroglifico, frecuencia) for jeroglifico, frecuencia in tabla_frecuencias.items()]
    while len(nodos) > 1:
        nodos = sorted(nodos, key=lambda x: x.frecuencia)
        izquierda = nodos.pop(0)
        derecha = nodos.pop(0)
        nuevo_nodo = NodoHuffman(None, izquierda.frecuencia + derecha.frecuencia)
        nuevo_nodo.izquierda = izquierda
        nuevo_nodo.derecha = derecha
        nodos.append(nuevo_nodo)
    return nodos[0]

def decodificar_mensaje(codigo, arbol_huffman):
    nodo_actual = arbol_huffman
    mensaje_decodificado = ""
    for bit in codigo:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        if nodo_actual.valor is not None:
            mensaje_decodificado += nodo_actual.valor + " "
            nodo_actual = arbol_huffman
    return mensaje_decodificado.strip()  # Elimina el espacio al final del mensaje

def reemplazar_palabras(mensaje, diccionario):
    for palabra, significado in diccionario.items():
        mensaje = mensaje.replace(palabra, significado)
    return mensaje

# Tabla de frecuencias y códigos de Huffman
tabla_frecuencias = {
    "Ankh": 15,
    "Scarab": 9,
    "Eye of Horus": 12,
    "Pyramid": 7,
    "Sphinx": 5,
    "Djed": 11,
    "Lotus": 8,
    "Obelisk": 10
}

arbol_huffman = construir_arbol_huffman(tabla_frecuencias)

# Diccionario de palabras y sus significados
diccionario_significados = {
    "Ankh": "vida",
    "Scarab": "protección",
    "Eye of Horus": "salud",
    "Pyramid": "inmortalidad",
    "Sphinx": "sabiduría",
    "Djed": "estabilidad",
    "Lotus": "renacimiento",
    "Obelisk": "faraón"
}

# Mensajes codificados proporcionados
mensaje_codificado_1 = "10001011101011000010111010001110000011011000000111100111101001011000011010011100110100010111010111111101000011110011111100111101000110001100000010110101111011111110111010110110111001110110111100111111100101001010010100000101101011000101100110100011100100101100001100100011010110101011111111111011011101110010000100101011000111111100010001110110011001011010001101111101011010001101110000000111001001010100011111100001100101101011100110011110100011000110000001011010111110011100"
mensaje_codificado_2 = "0110101011011100101000111101011100110111010110110100001000111010100101111010011111110111001010001111010111001101110101100001100010011010001110010010001100010110011001110010010000111101111010"

# Decodificar mensajes
mensaje_decodificado_1 = decodificar_mensaje(mensaje_codificado_1, arbol_huffman)
mensaje_decodificado_2 = decodificar_mensaje(mensaje_codificado_2, arbol_huffman)

# Reemplazar palabras por sus significados
mensaje_decodificado_1 = reemplazar_palabras(mensaje_decodificado_1, diccionario_significados)
mensaje_decodificado_2 = reemplazar_palabras(mensaje_decodificado_2, diccionario_significados)

# Imprimir los mensajes decodificados y los espacios de memoria
print("Mensaje decodificado 1:", mensaje_decodificado_1)
print("Mensaje decodificado 2:", mensaje_decodificado_2)

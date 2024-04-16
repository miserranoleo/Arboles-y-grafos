from collections import defaultdict
import heapq

class Grafo:
    def __init__(self):
        self.vertices = set()
        self.vecinos = defaultdict(list)

    def agregar_vertice(self, vertice):
        self.vertices.add(vertice)

    def agregar_arista(self, desde_vertice, a_vertice, peso):
        self.vecinos[desde_vertice].append((a_vertice, peso))
        self.vecinos[a_vertice].append((desde_vertice, peso))

    def dijkstra(self, origen, destino):
        distancias = {v: float('inf') for v in self.vertices}
        distancias[origen] = 0
        cola = [(0, origen)]
        padres = {}

        while cola:
            distancia_actual, vertice_actual = heapq.heappop(cola)

            if vertice_actual == destino:
                break

            if distancia_actual > distancias[vertice_actual]:
                continue

            for vecino, peso in self.vecinos[vertice_actual]:
                distancia_total = distancia_actual + peso
                if distancia_total < distancias[vecino]:
                    distancias[vecino] = distancia_total
                    padres[vecino] = vertice_actual
                    heapq.heappush(cola, (distancia_total, vecino))

        # Reconstruir la ruta
        ruta = [destino]
        while destino != origen:
            destino = padres[destino]
            ruta.append(destino)
        ruta.reverse()

        return distancias[ruta[-1]], ruta

def main():
    grafo_tierra_media = Grafo()
    ciudades_desvios = ['Rivendell', 'Minas Tirith', 'Gondor', 'Moria', 'Mirkwood', 'Lothlórien', 'Isengard', 'Fangorn']

    for ciudad in ciudades_desvios:
        grafo_tierra_media.agregar_vertice(ciudad)

    grafo_tierra_media.agregar_arista('Rivendell', 'Minas Tirith', 120)
    grafo_tierra_media.agregar_arista('Rivendell', 'Mirkwood', 90)
    grafo_tierra_media.agregar_arista('Minas Tirith', 'Gondor', 100)
    grafo_tierra_media.agregar_arista('Gondor', 'Moria', 80)
    grafo_tierra_media.agregar_arista('Mirkwood', 'Lothlórien', 40)
    grafo_tierra_media.agregar_arista('Lothlórien', 'Isengard', 70)
    grafo_tierra_media.agregar_arista('Isengard', 'Fangorn', 60)
    grafo_tierra_media.agregar_arista('Fangorn', 'Moria', 50)

    print("Bienvenido a la red de ferrocarriles de la Tierra Media")
    origen = input("Ingrese el punto de origen: ")
    destino = input("Ingrese el destino: ")

    if origen not in ciudades_desvios or destino not in ciudades_desvios:
        print("Error: Una de las ciudades ingresadas no está en la red de ferrocarriles.")
        return

    distancia_minima, ruta = grafo_tierra_media.dijkstra(origen, destino)
    print(f"La ruta más corta desde {origen} hasta {destino} es de {distancia_minima} millas:")
    print(" -> ".join(ruta))

if __name__ == "__main__":
    main()
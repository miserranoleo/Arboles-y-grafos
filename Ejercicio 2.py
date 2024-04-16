class Mision:
    def __init__(self, tipo, reino, dios):
        self.tipo = tipo
        self.reino = reino
        self.dios = dios

class Recurso:
    def __init__(self, valkirias, unidades):
        self.valkirias = valkirias
        self.unidades = unidades

def asignar_recursos(mision):
    if mision.dios == "Odín" or mision.dios == "Loki":
        print("La misión tiene alta prioridad.")
        if mision.tipo == "defensa":
            print("Se asignan 50 valkirias y 100 unidades.")
            return Recurso(50, 100)
        elif mision.tipo == "exploración":
            print("Se asignan 30 valkirias y 50 unidades.")
            return Recurso(30, 50)
        elif mision.tipo == "conquista":
            print("Se asignan 100 valkirias y 200 unidades.")
            return Recurso(100, 200)
    else:
        print("La misión tiene prioridad estándar.")
        if mision.tipo == "defensa":
            print("Se asignan 20 valkirias y 50 unidades.")
            return Recurso(20, 50)
        elif mision.tipo == "exploración":
            print("Se asignan 10 valkirias y 20 unidades.")
            return Recurso(10, 20)
        elif mision.tipo == "conquista":
            print("Se asignan 50 valkirias y 100 unidades.")
            return Recurso(50, 100)

def main():
    while True:
        tipo = input("Ingrese el tipo de misión (defensa, exploración, conquista): ")
        reino = input("Ingrese el reino destino: ")
        dios = input("Ingrese el dios que solicita la misión (Odín, Loki u otro): ")
        mision = Mision(tipo, reino, dios)
        recursos = asignar_recursos(mision)
        print("Recursos asignados - Valquirias:", recursos.valkirias, "Unidades:", recursos.unidades)
        continuar = input("¿Desea ingresar otra solicitud? (s/n): ")
        if continuar.lower() != "s":
            break

if __name__ == "__main__":
    main()

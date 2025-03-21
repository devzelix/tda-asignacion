class NodoMusica:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.anterior = None
        self.siguiente = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None

    def obtener_longitud(self):
        if not self.cabeza:
            return 0
        else:
            longitud = 0
            nodo_actual = self.cabeza
            while nodo_actual:
                longitud += 1
                nodo_actual = nodo_actual.siguiente
            return longitud

    def insertar_nodo_al_final(self, nodo_nuevo):
        if not self.cabeza:
            self.cabeza = nodo_nuevo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_nuevo
            nodo_nuevo.anterior = nodo_actual
        print(f"\nSe agrego correctamente '{nodo_nuevo.titulo}' a la cola de reproduccion.")

    def insertar_nodo(self, nodo_nuevo, indice):
        if self.obtener_longitud() > 0:
            if indice >= 0 and indice <= self.obtener_longitud() - 1:
                if indice == 0:
                    nodo_nuevo.siguiente = self.cabeza
                    self.cabeza.anterior = nodo_nuevo
                    self.cabeza = nodo_nuevo
                else:
                    nodo_actual = self.cabeza
                    for i in range(1, indice):
                        nodo_actual = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_nuevo
                    nodo_nuevo.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente = nodo_nuevo
                    nodo_nuevo.anterior = nodo_actual
                print(f"\nSe agrego correctamente '{nodo_nuevo.titulo}' a la cola de reproduccion.")
            else:
                print("\nEl indice esta fuera del rango.")
        else:
            print("\nLa cola de reproduccion esta vacia.")

    def eliminar_nodo(self, titulo):
        if self.obtener_longitud() > 0:
            nodo_actual = self.cabeza
            while nodo_actual:
                if nodo_actual.titulo == titulo:
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                    break
                nodo_actual = nodo_actual.siguiente
            if nodo_actual:
                print(f"\nSe elimino correctamente '{nodo_actual.titulo}' de la cola de reproduccion.")
            else:
                print(f"\n'{nodo_actual.titulo}' no se encontro en la cola de reproduccion.")
        else:
            print("\nLa cola de reproduccion esta vacia.")

    def listar_nodos(self):
        if self.obtener_longitud() > 0:
            nodo_actual = self.cabeza
            i = 1
            print("\nLista de canciones:\n")
            while nodo_actual:
                print(f"{"0" * (len(str(self.obtener_longitud())) - len(str(i)))}{i}) {nodo_actual.titulo}, {nodo_actual.autor}")
                nodo_actual = nodo_actual.siguiente
                i += 1
        else:
            print("\nLa cola de reproduccion esta vacia.")

def main():
    musica_1 = NodoMusica("Hasta que te conoci", "Juan Gabriel")
    musica_2 = NodoMusica("DtMf", "Bad Bunny")
    musica_3 = NodoMusica("De sol a sol", "Salserin")
    musica_4 = NodoMusica("Virgen", "Adolescentes")
    musica_5 = NodoMusica("La mudanza", "Bad Bunny")
    cola_reproduccion = ListaDoblementeEnlazada()
    cola_reproduccion.insertar_nodo_al_final(musica_1)
    cola_reproduccion.insertar_nodo_al_final(musica_2)
    cola_reproduccion.insertar_nodo_al_final(musica_3)
    cola_reproduccion.listar_nodos()
    cola_reproduccion.insertar_nodo(musica_4, 0)
    cola_reproduccion.listar_nodos()
    cola_reproduccion.eliminar_nodo("DtMf")
    cola_reproduccion.listar_nodos()
    cola_reproduccion.insertar_nodo(musica_2, 2)
    cola_reproduccion.listar_nodos()
    cola_reproduccion.insertar_nodo_al_final(musica_5)
    cola_reproduccion.listar_nodos()
    print()

if __name__ == "__main__":
    main()
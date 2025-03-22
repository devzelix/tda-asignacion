class NodoCancion:
    # Clase que representa un nodo de una canción dentro de una lista doblemente enlazada
    def __init__(self, titulo, autor):
        self.titulo = titulo  # Título de la canción
        self.autor = autor    # Autor de la canción
        self.anterior = None  # Referencia al nodo anterior en la lista
        self.siguiente = None # Referencia al siguiente nodo en la lista

class ListaDoblementeEnlazada:
    # Clase que representa una lista doblemente enlazada
    def __init__(self):
        self.cabeza = None  # Inicialmente, la lista está vacía

    def obtener_longitud(self):
        # Método para obtener la longitud de la lista
        if not self.cabeza:
            return 0  # Si la lista está vacía, la longitud es 0
        else:
            longitud = 0
            nodo_actual = self.cabeza
            while nodo_actual:
                longitud += 1  # Contamos los nodos de la lista
                nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo
            return longitud

    def insertar_nodo_final(self, nodo_nuevo):
        # Método para insertar un nodo al final de la lista
        if not self.cabeza:
            # Si la lista está vacía, el nuevo nodo se convierte en la cabeza
            self.cabeza = nodo_nuevo
        else:
            # Si la lista no está vacía, buscamos el último nodo
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente  # Avanzamos hasta el último nodo
            nodo_actual.siguiente = nodo_nuevo  # El último nodo apunta al nuevo nodo
            nodo_nuevo.anterior = nodo_actual  # El nuevo nodo apunta al anterior
        # Imprimir mensaje de éxito
        print(f"\nSe agrego correctamente '{nodo_nuevo.titulo}' a la cola de reproduccion.")

    def insertar_nodo(self, nodo_nuevo, indice):
        # Método para insertar un nodo en una posición específica de la lista
        if self.cabeza:
            # Verificamos si el índice está dentro de los límites de la lista
            if indice >= 0 and indice <= self.obtener_longitud() - 1:
                if indice == 0:
                    # Insertar al principio de la lista
                    nodo_nuevo.siguiente = self.cabeza
                    self.cabeza.anterior = nodo_nuevo
                    self.cabeza = nodo_nuevo  # El nuevo nodo se convierte en la cabeza
                else:
                    # Insertar en una posición intermedia de la lista
                    nodo_actual = self.cabeza
                    for i in range(1, indice):
                        nodo_actual = nodo_actual.siguiente  # Avanzamos hasta el nodo anterior
                    # Actualizamos las referencias para insertar el nuevo nodo
                    nodo_actual.siguiente.anterior = nodo_nuevo
                    nodo_nuevo.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente = nodo_nuevo
                    nodo_nuevo.anterior = nodo_actual
                # Imprimir mensaje de éxito
                print(f"\nSe agrego correctamente '{nodo_nuevo.titulo}' a la cola de reproduccion.")
            else:
                # Si el índice está fuera de rango, mostramos un mensaje de error
                print("\nEl indice esta fuera del rango.")
        else:
            # Si la lista está vacía, mostramos un mensaje de error
            print("\nLa cola de reproduccion esta vacia.")

    def eliminar_nodo(self, titulo):
        # Método para eliminar un nodo por su título
        if self.obtener_longitud() > 0:
            if not self.cabeza.siguiente:
                # Si hay solo un nodo, eliminamos la cabeza
                self.cabeza = None
            else:
                # Buscamos el nodo a eliminar
                nodo_actual = self.cabeza
                while nodo_actual:
                    if nodo_actual.titulo == titulo:
                        break  # Si encontramos el nodo, salimos del bucle
                    nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.cabeza:
                    # Si el nodo a eliminar es la cabeza de la lista
                    self.cabeza = self.cabeza.siguiente
                    self.cabeza.anterior = None  # La nueva cabeza no tiene anterior
                    print(f"\nSe elimino correctamente '{titulo}' de la cola de reproduccion.")
                elif nodo_actual.siguiente == None:
                    # Si el nodo a eliminar es el último nodo
                    nodo_actual.anterior.siguiente = None
                    print(f"\nSe elimino correctamente '{titulo}' de la cola de reproduccion.")
                elif nodo_actual:
                    # Si el nodo está en el medio de la lista
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                    print(f"\nSe elimino correctamente '{titulo}' de la cola de reproduccion.")
                else:
                    # Si no se encuentra el nodo
                    print(f"\n'{titulo}' no se encontro en la cola de reproduccion.")
        else:
            # Si la lista está vacía
            print("\nLa cola de reproduccion esta vacia.")

    def listar_nodos(self):
        # Método para listar todos los nodos de la lista
        longitud = self.obtener_longitud()
        if longitud > 0:
            nodo_actual = self.cabeza
            i = 1
            print("\nLista de canciones:\n")
            ancho = len(str(longitud))  # Calculamos el ancho necesario para los índices
            while nodo_actual:
                # Imprimimos los nodos con un índice con ceros a la izquierda
                print(f"{str(i).zfill(ancho)}) {nodo_actual.titulo}, {nodo_actual.autor}")
                nodo_actual = nodo_actual.siguiente  # Avanzamos al siguiente nodo
                i += 1
        else:
            # Si la lista está vacía
            print("\nLa cola de reproduccion esta vacia.")

def main():
    # Crear nodos de canciones
    musica_1 = NodoCancion("Hasta que te conoci", "Juan Gabriel")
    musica_2 = NodoCancion("DtMf", "Bad Bunny")
    musica_3 = NodoCancion("De sol a sol", "Salserin")
    musica_4 = NodoCancion("Virgen", "Adolescentes")
    musica_5 = NodoCancion("La mudanza", "Bad Bunny")
    # Crear la lista de reproducción
    cola_reproduccion = ListaDoblementeEnlazada()
    # Insertar nodos al final
    cola_reproduccion.insertar_nodo_final(musica_1)
    cola_reproduccion.insertar_nodo_final(musica_2)
    cola_reproduccion.insertar_nodo_final(musica_3)
    # Listar los nodos de la lista de reproducción
    cola_reproduccion.listar_nodos()
    # Insertar un nodo al principio de la lista
    cola_reproduccion.insertar_nodo(musica_4, 0)
    cola_reproduccion.listar_nodos()
    # Eliminar un nodo por su título
    cola_reproduccion.eliminar_nodo("DtMf")
    cola_reproduccion.listar_nodos()
    # Insertar un nodo en el índice 2
    cola_reproduccion.insertar_nodo(musica_2, 2)
    cola_reproduccion.listar_nodos()
    # Insertar un nodo al final
    cola_reproduccion.insertar_nodo_final(musica_5)
    cola_reproduccion.listar_nodos()
    # Fin de la ejecución del programa
    print()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
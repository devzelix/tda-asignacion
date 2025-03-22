class NodoCliente:
    # Clase que representa un nodo de un cliente en una lista circular
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre  # Nombre del cliente
        self.apellido = apellido  # Apellido del cliente
        self.cedula = cedula  # Cédula de identidad del cliente
        self.siguiente = None  # Puntero al siguiente nodo (se inicializa como None)

class ListaCircular:
    # Clase que representa una lista circular de clientes
    def __init__(self):
        self.cabeza = None  # La lista comienza vacía, sin cabeza

    def verificar_existencia_cedula(self, cedula):
        # Método para verificar si una cédula ya existe en la lista
        nodo_actual = self.cabeza
        # Recorremos la lista circular hasta volver a la cabeza
        while nodo_actual.siguiente != self.cabeza:
            if nodo_actual.cedula == cedula:  # Si la cédula ya existe
                return True
            nodo_actual = nodo_actual.siguiente
        return False  # Si no se encuentra la cédula, devolvemos False

    def insertar_nodo_inicio(self, nodo_nuevo):
        # Método para insertar un nuevo nodo al inicio de la lista
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nodo_nuevo  # El nuevo nodo se convierte en la cabeza
            nodo_nuevo.siguiente = self.cabeza  # El siguiente del nuevo nodo apunta a la cabeza
            print("\nSe registro correctamente al cliente.")
        else:
            # Verificamos si la cédula ya existe en la lista
            if not self.verificar_existencia_cedula(nodo_nuevo.cedula):
                nodo_actual = self.cabeza
                # Recorremos la lista circular hasta el último nodo
                while nodo_actual.siguiente != self.cabeza:
                    nodo_actual = nodo_actual.siguiente
                # Insertamos el nuevo nodo al principio
                nodo_nuevo.siguiente = self.cabeza
                self.cabeza = nodo_nuevo  # La cabeza ahora es el nuevo nodo
                nodo_actual.siguiente = self.cabeza  # El último nodo apunta de vuelta a la cabeza
                print("\nSe registro correctamente al cliente.")
            else:
                print("\nYa se encuentra registrado.")  # Si ya existe, mostramos mensaje

    def insertar_nodo_final(self, nodo_nuevo):
        # Método para insertar un nuevo nodo al final de la lista
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nodo_nuevo  # El nuevo nodo se convierte en la cabeza
            nodo_nuevo.siguiente = self.cabeza  # El siguiente del nuevo nodo apunta a la cabeza
            print("\nSe registro correctamente al cliente.")
        else:
            # Verificamos si la cédula ya existe en la lista
            if not self.verificar_existencia_cedula(nodo_nuevo.cedula):
                nodo_actual = self.cabeza
                # Recorremos la lista circular hasta el último nodo
                while nodo_actual.siguiente != self.cabeza:
                    nodo_actual = nodo_actual.siguiente
                # Insertamos el nuevo nodo al final
                nodo_actual.siguiente = nodo_nuevo
                nodo_nuevo.siguiente = self.cabeza  # El nuevo nodo apunta de vuelta a la cabeza
                print("\nSe registro correctamente al cliente.")
            else:
                print("\nYa se encuentra registrado.")  # Si ya existe, mostramos mensaje

    def eliminar_nodo(self, cedula):
        # Método para eliminar un nodo basado en la cédula
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:  # Si hay solo un nodo
                if self.cabeza.cedula == cedula:  # Si la cédula es la de la cabeza
                    self.cabeza = None  # Eliminamos el único nodo
                    print("\nSe elimino correctamente al cliente.")
                else:
                    print("\nNo se encontro el cliente.")
            else:
                nodo_actual = self.cabeza
                eliminado = False
                # Recorremos la lista circular hasta encontrar el nodo con la cédula
                while nodo_actual.siguiente != self.cabeza:
                    if nodo_actual.siguiente.cedula == cedula:
                        nodo_actual.siguiente = nodo_actual.siguiente.siguiente  # Borramos el nodo
                        eliminado = True
                        break
                    nodo_actual = nodo_actual.siguiente
                # Si el nodo a eliminar está en la cabeza
                if nodo_actual.siguiente.cedula == cedula:
                    self.cabeza = nodo_actual.siguiente.siguiente
                    nodo_actual.siguiente = self.cabeza
                    eliminado = True
                if eliminado:
                    print("\nSe elimino correctamente al cliente.")
                else:
                    print("\nNo se encontro el cliente.")
        else:
            print("\nLa lista esta vacia.")  # Si la lista está vacía

    def listar_nodos(self):
        # Método para listar todos los nodos de la lista
        if self.cabeza:
            nodo_actual = self.cabeza
            print("\nClientes:\n")
            # Recorremos la lista circular e imprimimos los detalles de cada cliente
            while nodo_actual.siguiente != self.cabeza:
                print(f" - Nombre y Apellido: {nodo_actual.nombre} {nodo_actual.apellido}, C.I: {nodo_actual.cedula}")
                nodo_actual = nodo_actual.siguiente
            # Imprimimos el último nodo
            if not nodo_actual == self.cabeza:
                print(f" - Nombre y Apellido: {nodo_actual.nombre} {nodo_actual.apellido}, C.I: {nodo_actual.cedula}")
        else:
            print("\nLa lista esta vacia.")  # Si la lista está vacía

def main():
    # Creamos algunos nodos de clientes
    cliente_1 = NodoCliente("Jose", "Solett", "31456615")
    cliente_2 = NodoCliente("Richerd", "Ferrer", "30500781")
    cliente_3 = NodoCliente("Nathaly", "Bustamante", "12522462")
    cliente_4 = NodoCliente("Jose", "Solett", "15564297")
    # Creamos la lista circular de clientes
    lista_clientes = ListaCircular()
    # Insertamos clientes al final de la lista
    lista_clientes.insertar_nodo_final(cliente_1)
    lista_clientes.insertar_nodo_final(cliente_2)
    # Listamos los clientes registrados
    lista_clientes.listar_nodos()
    # Insertamos un cliente al principio de la lista
    lista_clientes.insertar_nodo_inicio(cliente_3)
    lista_clientes.listar_nodos()
    # Eliminamos un cliente por su cédula
    lista_clientes.eliminar_nodo("12522462")
    lista_clientes.listar_nodos()
    # Insertamos otro cliente al final
    lista_clientes.insertar_nodo_final(cliente_4)
    lista_clientes.listar_nodos()
    print()

# Ejecutamos la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
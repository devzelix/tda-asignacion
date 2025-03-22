class NodoCliente:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def verificar_existencia_cedula(self, cedula):
        nodo_actual = self.cabeza
        while nodo_actual.siguiente != self.cabeza:
            if nodo_actual.cedula == cedula:
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def insertar_nodo_inicio(self, nodo_nuevo):
        if not self.cabeza:
            self.cabeza = nodo_nuevo
            nodo_nuevo.siguiente = self.cabeza
            print("\nSe registro correctamente al cliente.")
        else:
            if not self.verificar_existencia_cedula(nodo_nuevo.cedula):
                nodo_actual = self.cabeza
                while nodo_actual.siguiente != self.cabeza:
                    nodo_actual = nodo_actual.siguiente
                nodo_nuevo.siguiente = self.cabeza
                self.cabeza = nodo_nuevo
                nodo_actual.siguiente = self.cabeza
                print("\nSe registro correctamente al cliente.")
            else:
                print("\nYa se encuentra registrado.")

    def insertar_nodo_final(self, nodo_nuevo):
        if not self.cabeza:
            self.cabeza = nodo_nuevo
            nodo_nuevo.siguiente = self.cabeza
            print("\nSe registro correctamente al cliente.")
        else:
            if not self.verificar_existencia_cedula(nodo_nuevo.cedula):
                nodo_actual = self.cabeza
                while nodo_actual.siguiente != self.cabeza:
                    nodo_actual = nodo_actual.siguiente
                nodo_actual.siguiente = nodo_nuevo
                nodo_nuevo.siguiente = self.cabeza
                print("\nSe registro correctamente al cliente.")
            else:
                print("\nYa se encuentra registrado.")

    def eliminar_nodo(self, cedula):
        if self.cabeza:
            if self.cabeza.siguiente == self.cabeza:
                if self.cabeza.cedula == cedula:
                    self.cabeza = None
                    print("\nSe elimino correctamente al cliente.")
                else:
                    print("\nNo se encontro el cliente.")
            else:
                nodo_actual = self.cabeza
                eliminado = False
                while nodo_actual.siguiente != self.cabeza:
                    if nodo_actual.siguiente.cedula == cedula:
                        nodo_actual.siguiente = nodo_actual.siguiente.siguiente
                        eliminado = True
                        break
                    nodo_actual = nodo_actual.siguiente
                if nodo_actual.siguiente.cedula == cedula:
                    self.cabeza = nodo_actual.siguiente.siguiente
                    nodo_actual.siguiente = self.cabeza
                    eliminado = True
                if eliminado:
                    print("\nSe elimino correctamente al cliente.")
                else:
                    print("\nNo se encontro el cliente.")
        else:
            print("\nLa lista esta vacia.")

    def listar_nodos(self):
        if self.cabeza:
            nodo_actual = self.cabeza
            i = 1
            print("\nClientes:\n")
            while nodo_actual.siguiente != self.cabeza:
                print(f" - Nombre y Apellido: {nodo_actual.nombre} {nodo_actual.apellido}, C.I: {nodo_actual.cedula}")
                nodo_actual = nodo_actual.siguiente
                i += 1
            if not nodo_actual == self.cabeza:
                print(f" - Nombre y Apellido: {nodo_actual.nombre} {nodo_actual.apellido}, C.I: {nodo_actual.cedula}")
        else:
            print("\nLa lista esta vacia.")

def main():
    cliente_1 = NodoCliente("Jose", "Solett", "31456615")
    cliente_2 = NodoCliente("Richerd", "Ferrer", "30500781")
    cliente_3 = NodoCliente("Nathaly", "Bustamante", "12522462")
    cliente_4 = NodoCliente("Jose", "Solett", "15564297")
    lista_clientes = ListaCircular()
    lista_clientes.insertar_nodo_final(cliente_1)
    lista_clientes.insertar_nodo_final(cliente_2)
    lista_clientes.listar_nodos()
    lista_clientes.insertar_nodo_inicio(cliente_3)
    lista_clientes.listar_nodos()
    lista_clientes.eliminar_nodo("12522462")
    lista_clientes.listar_nodos()
    lista_clientes.insertar_nodo_final(cliente_4)
    lista_clientes.listar_nodos()
    print()

if __name__ == "__main__":
    main()
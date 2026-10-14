from empleado import Empleado


class Proyecto:
    def __init__(self, id_proyecto: int, nombre_proyecto: str):
        self.__id_proyecto = id_proyecto
        self.__nombre_proyecto = nombre_proyecto
        self.__equipo = []

    @property
    def id_proyecto(self):
        return self.__id_proyecto

    @property
    def nombre_proyecto(self):
        return self.__nombre_proyecto

    def agregar_integrante(self, empleado: Empleado):
        self.__equipo.append(empleado)
        print(
            f"Empleado '{empleado.nombre}' asignado "
            f"al proyecto '{self.__nombre_proyecto}'."
        )

    def listar_equipo(self):
        print(f"\nEquipo del Proyecto: {self.__nombre_proyecto}")

        for empleado in self.__equipo:
            print(empleado.obtener_detalles())

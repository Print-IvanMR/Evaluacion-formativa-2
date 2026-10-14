from empleado import Empleado

class Tecnico(Empleado):
    def __init__(
        self,
        id_empleado: int,
        nombre: str,
        email: str,
        especialidad: str
    ):
        super().__init__(id_empleado, nombre, email)
        self.__especialidad = especialidad

    @property
    def especialidad(self):
        return self.__especialidad

    def obtener_detalles(self) -> str:
        detalles = super().obtener_detalles()
        return f"{detalles} | Especialidad: {self.__especialidad}"

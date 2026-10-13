
class Empleado:
    def __init__(self, id_empleado: int, nombre: str, email: str):
        self._id_empleado = id_empleado
        self._nombre = nombre
        self.__email = email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email: str):
        if "@" in nuevo_email:
            self.__email = nuevo_email
        else:
            raise ValueError("Email inválido")

    def obtener_detalles(self) -> str:
        return f"ID: {self._id_empleado} | Nombre: {self._nombre} | Email: {self.__email}"

class Tecnico(Empleado):
    def __init__(self, id_empleado: int, nombre: str, email: str, especialidad: str):
        super().__init__(id_empleado, nombre, email)
        self.especialidad = especialidad

    def obtener_detalles(self) -> str:
        base = super().obtener_detalles()
        return f"{base} | Especialidad: {self.especialidad}"

class Proyecto:
    def __init__(self, id_proyecto: int, nombre_proyecto: str):
        self.id_proyecto = id_proyecto
        self.nombre_proyecto = nombre_proyecto
        self.__equipo = []

    def agregar_integrante(self, empleado: Empleado):
        self.__equipo.append(empleado)
        print(f"Empleado '{empleado._nombre}' asignado al proyecto '{self.nombre_proyecto}'.")

    def listar_equipo(self):
        print(f"\n--- Equipo del Proyecto: {self.nombre_proyecto} ---")
        for emp in self.__equipo:
            print(emp.obtener_detalles())
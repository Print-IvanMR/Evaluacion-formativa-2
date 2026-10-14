
class Empleado:
    def __init__(self, id_empleado: int, nombre: str, email: str):
        self.__id_empleado = id_empleado
        self.__nombre = nombre
        self.__email = email

    @property
    def id_empleado(self):
        return self.__id_empleado

    @property
    def nombre(self):
        return self.__nombre

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
        return (
            f"ID: {self.__id_empleado} | "
            f"Nombre: {self.__nombre} | "
            f"Email: {self.__email}"
        )

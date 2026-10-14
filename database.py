import sqlite3


class ConexionBD:
    def __init__(self, db_file="ecotech.db"):
        self.__db_file = db_file
        self.__conexion = None

    def conectar(self):
        try:
            self.__conexion = sqlite3.connect(self.__db_file)
            print(
                f"Conexión establecida con la base de datos "
                f"'{self.__db_file}'."
            )
            return self.__conexion
        except sqlite3.Error as error:
            print(f"Error de conexión: {error}")
            return None

    def inicializar_tablas(self):
        conexion = self.conectar()

        if conexion is None:
            return False

        try:
            cursor = conexion.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL,
                    tipo TEXT NOT NULL,
                    especialidad TEXT
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS proyectos (
                    id INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL
                )
            """)

            conexion.commit()
            print("Tablas listas.")
            return True

        except sqlite3.Error as error:
            print(f"error al crear las tablas: {error}")
            return False

        finally:
            self.cerrar()

    def cerrar(self):
        if self.__conexion is not None:
            self.__conexion.close()
            self.__conexion = None
            print("Conexion cerrada")

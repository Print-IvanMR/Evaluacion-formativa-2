import sqlite3
from sqlite3 import Error

class ConexionBD:
    def __init__(self, db_file="ecotech.db"):
        self.__db_file = db_file
        self.__conexion = None

    def conectar(self):
        try:
            self.__conexion = sqlite3.connect(self.__db_file)
            print(f"Conexion establecida con la base de datos '{self.__db_file}'.")
            return self.__conexion
        except Error as e:
            print(f"Fallo en la conexion: {e}")
            return None

    def inicializar_tablas(self):
        conn = self.conectar()
        if conn is not None:
            try:
                cursor = conn.cursor()
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
                conn.commit()
                print("Tablas verificadas y listas")
            except Error as e:
                print(f"No se pudieron crear las tablas: {e}")
            finally:
                self.cerrar()

    def cerrar(self):
        if self.__conexion:
            self.__conexion.close()
            print("Conexion cerrada.")
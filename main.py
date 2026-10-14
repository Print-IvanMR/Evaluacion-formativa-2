
from empleado import Empleado
from tecnico import Tecnico
from proyecto import Proyecto
from database import ConexionBD


def main():
    print("ECOTECH SOLUTIONS - SISTEMA DE GESTION")

    print("\nPrueba de conexion a la base de datos")

    gestor_bd = ConexionBD()
    conexion_exitosa = gestor_bd.inicializar_tablas()

    if not conexion_exitosa:
        print("No se pudo completar la prueba de conexion")
        return

    print("\nCreacion de empleados")

    empleado = Empleado(
        1,
        "Ana Gomez",
        "agomez@ecotech.cl"
    )

    tecnico = Tecnico(
        2,
        "Carlos Ruiz",
        "cruiz@ecotech.cl",
        "Eficiencia energetica"
    )

    print(empleado.obtener_detalles())
    print(tecnico.obtener_detalles())

    print("\nAsignacion de empleados al proyecto")

    proyecto = Proyecto(
        101,
        "Optimizacion de planta solar"
    )

    proyecto.agregar_integrante(empleado)
    proyecto.agregar_integrante(tecnico)
    proyecto.listar_equipo()


if __name__ == "__main__":
    main()

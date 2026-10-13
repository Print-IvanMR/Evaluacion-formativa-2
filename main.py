from database import ConexionBD
from models import Empleado, Tecnico, Proyecto

def main():
    print("ECOTECH SOLUTIONS, SISTEMA DE GESTION")
    
    print("\nPrueba de conexión a base de datos")
    gestor_bd = ConexionBD()
    gestor_bd.inicializar_tablas()

    print("\nCreacion de Objetos y encapsulamiento")
    emp_base = Empleado(1, "Ana Gómez", "agomez@ecotech.cl")
    tec_esp = Tecnico(2, "Carlos Ruiz", "cruiz@ecotech.cl", "Eficiencia energetica")

    print(emp_base.obtener_detalles())
    print(tec_esp.obtener_detalles())

    print("\nAsignacion de Recursos a proyecto")
    proyecto_opt = Proyecto(101, "Optimizacion de planta solar")
    proyecto_opt.agregar_integrante(emp_base)
    proyecto_opt.agregar_integrante(tec_esp)

    proyecto_opt.listar_equipo()

if __name__ == "__main__":
    main()
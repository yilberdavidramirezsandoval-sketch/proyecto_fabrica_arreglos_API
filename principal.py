from base_de_datos_empleados import base_datos_empleados
from empleado_modelo import Empleado_modelo


# creo la base de datos de empleados
obj_bd_Empleado_lista = base_datos_empleados()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("jose", "Perez", "987654321", "5677878543")
obj_empleado2 = Empleado_modelo("luisa", "Gomez", "5677878543", "987654321")


#creo una lista para guardar masivamente 
lista_nuevos_empleados = [obj_empleado2,obj_empleado]

# llamo el metodo de la base de datos que guarda al objeto
obj_bd_Empleado_lista.agregar_empleado(obj_empleado)#guardando un obj
obj_bd_Empleado_lista.agregar_empleado(obj_empleado2)

obj_bd_Empleado_lista.extender_varios_empleador(lista_nuevos_empleados)

#imprimir toda la lista de empleados
obj_bd_Empleado_lista.imprimir_info()
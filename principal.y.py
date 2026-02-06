from base_datos_empleados import base_datos_empleados
from empleado_modelo import Empleado_modelo


# creo la base de datos de empleados
obj_bd_Empleado_lista = base_datos_empleados()
# creo el objeto empleado que voy a agregar
obj_empleado = Empleado_modelo("Jose","perez","123456789","987654321")
obj_empleado2 = Empleado_modelo("luisa","gomez","987654321","123456789")
obj_empleado3 = Empleado_modelo("arturo","lopez","456778987","678825356")
obj_empleado4 = Empleado_modelo("ana","ramirez","786543346","667384567")
obj_empleado5 = Empleado_modelo("axel","gutierrez","567892967","234567891")
obj_empleado6 = Empleado_modelo("julian","maldonado","456789912","987654872")


# llamo el metodo de la base de datos que guarda al objeto
#creo una lista para guardar masivamente

lista_nuevos_modelos = [obj_empleado, obj_empleado2, obj_empleado3, obj_empleado4, obj_empleado5, obj_empleado6]

# guardar varios empleados a la vez
obj_bd_Empleado_lista.guardar_varios_empleados(lista_nuevos_modelos) 

# inserta el empleado en la posicion que escojas
obj_bd_Empleado_lista.insertar_empleados(3, obj_empleado)  

# elimina el último empleado de la lista
obj_bd_Empleado_lista.eliminar_ult_lista()  

# elimina el empleado en la posición que indiques 
obj_bd_Empleado_lista.eliminar_empleado_por_posicion(5)  

print("\n--- Lista Despues de las eliminaciones ---")
obj_bd_Empleado_lista.imprimir_info()

# ordena la lista por nombre del empleado alfabéticamente
print("\n--- Lista ordenada por nombre (sort) ---")
obj_bd_Empleado_lista.sort_empleados()  
obj_bd_Empleado_lista.imprimir_info()

# invierte el orden de la lista de empleados
print("\n--- Lista invertida (reverse) ---")
obj_bd_Empleado_lista.reverse_empleados()  
obj_bd_Empleado_lista.imprimir_info()
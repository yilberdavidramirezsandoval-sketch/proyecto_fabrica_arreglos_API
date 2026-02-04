class base_datos_empleados:
    def _init_(self):
        self.db_empleado_lista = []
    def agregar_empleado(self, obj_empleado):
        self.db_empleado_lista.append(obj_empleado)
        print("xxxx:" , self.db_empleado_lista) 
        print("aaaa" , self.db_empleado_lista[0].get_nombre_empleado())
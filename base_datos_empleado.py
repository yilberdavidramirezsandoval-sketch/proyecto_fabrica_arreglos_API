class base_datos_empleados:
    def __init__(self):
        self.db_empleado_lista = []

    def guardar_empleado(self,obj_empleado):
        self.db_empleado_lista.append(obj_empleado)
        return True
    
    def guardar_varios_empleados(self,varios_obj):
        self.db_empleado_lista.extend(varios_obj)
    
    def imprimir_info(self):
        for i in range(len(self.db_empleado_lista)):
            nombre = self.db_empleado_lista[i].get_nombre_empleado()
            apellido = self.db_empleado_lista[i].get_apellido_empleado()
            cedula = self.db_empleado_lista[i].get_cedula_empleado()
            print(f"nombre empleado {nombre} - apellido: {apellido} - cedula: {cedula}")
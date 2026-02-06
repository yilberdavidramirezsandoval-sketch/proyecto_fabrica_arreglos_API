class Empleado_modelo:
    def __init__(self, nombre , apellido, cedula , telefono):
        self.nombre_empleado = nombre
        self.apellido_empleado = apellido
        self.cedula_empleado =cedula
        self.telefono_empleado = telefono

    def set_nombre_empleado(self ,nuevo_nombre):
        self.nombre_empleado=nuevo_nombre
    
    def get_nombre_empleado(self):
        return self.nombre_empleado
    
    def set_apellido_empleado(self ,nuevo_apellido):
        self.apellido_empleado=nuevo_apellido
    
    def get_apellido_empleado(self):
        return self.apellido_empleado
    
    def set_cedula_empleado(self ,nuevo_cedula):
        self.cedula_empleado=nuevo_cedula
    
    def get_cedula_empleado(self):
        return self.cedula_empleado
    
    def set_telefono_empleado(self ,nuevo_telefono):
        self.telefono_empleado=nuevo_telefono
    
    def get_telefono_empleado(self):
        return self.telefono_empleado
    
    def ver_info(self):
        info="nombre empleado" + self.nombre_empleado + "apellido empleado" + self.apellido_empleado 
        info = info + "cedula empleado" + self.cedula_empleado + "telefono empleado" + self.telefono_empleado
        return info
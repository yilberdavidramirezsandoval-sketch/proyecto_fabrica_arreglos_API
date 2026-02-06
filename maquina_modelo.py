class maquina_modelo:
    def _init_(self,codigo, nombre, modelo, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.modelo = modelo
        self.estado = estado
    
    def set_codigo(self, codigo):
        self.codigo = codigo
    
    def get_codigo(self):
        return self.codigo  
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_modelo(self, modelo):
        self.modelo = modelo
        
    def get_modelo(self):
        return self.modelo
    
    def set_estado(self, estado):
        self.estado = estado
        
    def get_estado(self):
        return self.estado
    
    def ver_info_maquina(self):
        return f"Codigo: {self.codigo}, Nombre: {self.nombre}, Modelo: {self.modelo}, Estado: {self.estado}"
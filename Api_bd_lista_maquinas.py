class Api_bd_lista_maquinas:
    def __init__(self):
        self.Api_maquinas = [
            ["codigo", "nombre", "Modelo Maquina", "Estado maquina"],
            ["cod 1921", "brazo mecanico", "x102", "Apagada"],
            ["cod 1234", "cinta transportadora", "zx400", "Requiere mantenimiento"],
            ["cod 5564", "Monobrazo", "j102", "Encendida"],
        ]
    
    def imprimir_info(self):
        for i in range(len(self.Api_maquinas)):
            print(self.Api_maquinas[i])
    
    def buscar_info(self):
        return self.Api_maquinas[0][1]
from datetime import datetime

class Tarea:
    # atributo de clase
    __ultimo_id = 0

    @classmethod
    def generar_siguiente_id(cls)->int:
        cls.__ultimo_id += 1
        return cls.__ultimo_id
    
    @classmethod
    def establecer_ultimo_id(cls, ultimo_id:int):
        if not isinstance(ultimo_id, int) or ultimo_id < 0:
            raise ValueError(f'El último id debe ser un entero positivo')
        cls.__ultimo_id = ultimo_id

    @classmethod
    def obtener_ultimo_id(cls)->int:
        return cls.__ultimo_id

    @classmethod
    def fromDiccionario(cls, diccionario:dict):
        if not isinstance(diccionario, dict):
            raise ValueError(f'El diccionario debe ser de tipo dict')
        if "id" in diccionario and "fecha_creacion" in diccionario:
            return cls(diccionario['titulo'], diccionario['descripcion'], diccionario['completada'], diccionario['id'], diccionario['fecha_creacion'])
        else:
            return cls(diccionario['titulo'], diccionario['descripcion'], diccionario['completada'])


    def __init__(self, titulo:str, descripcion:str, completada:bool, id:int = None, fecha_creacion:str = None):
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError(f'El titulo debe ser de tipo string y no estar vacío')
        if not isinstance(descripcion, str) or descripcion == "" or descripcion.isspace():
            raise ValueError(f'La descripción debe ser de tipo string y no estar vacía')
        if not isinstance(completada, bool):
            raise ValueError(f'El campo completada debe ser de tipo booleano')
        if id is not None:
            if not isinstance(id, int) or id < 0:
                raise ValueError(f'El id debe ser un entero positivo')
        if fecha_creacion is not None:
            if not isinstance(fecha_creacion, str) or fecha_creacion == "":
                raise ValueError(f'La fecha de creación debe ser un string y no estar vacía')
        
        self.__titulo = titulo
        self.__descripcion = descripcion
        self.__completada = completada
        
        if id is not None:
            self.__id = id
        else:
            self.__id = Tarea.generar_siguiente_id()
        
        if fecha_creacion is not None:
            self.__fecha_creacion = fecha_creacion
        else:
            self.__fecha_creacion = "28/11/2024"
    
    def establecer_titulo(self, titulo:str):
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError(f'El titulo debe ser de tipo string y no estar vacío')
        self.__titulo = titulo

    def establecer_descripcion(self, descripcion:str):
        if not isinstance(descripcion, str) or descripcion == "" or descripcion.isspace():
            raise ValueError(f'La descripción debe ser de tipo string y no estar vacía')
        self.__descripcion = descripcion

    def establecer_completada(self, completada:bool):
        if not isinstance(completada, bool):
            raise ValueError(f'El campo completada debe ser de tipo booleano')
        self.__completada = completada

    def obtener_titulo(self)->str:
        return self.__titulo
    
    def obtener_descripcion(self)->str:
        return self.__descripcion
    
    def obtener_completada(self)->bool:
        return self.__completada
    
    def obtener_id(self)->int:
        return self.__id
    
    def obtener_fecha_creacion(self):
        return self.__fecha_creacion
    
    def toDiccionario(self):
        return {
            "id": self.__id,
            "titulo": self.__titulo,
            "descripcion": self.__descripcion,
            "completada": self.__completada,
            "fecha_creacion": self.__fecha_creacion
        }
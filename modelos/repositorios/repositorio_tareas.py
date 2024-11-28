from modelos.entidades.tarea import Tarea
import json

class RepositorioTareas:
    #atributo de clase
    __ruta_archivo = 'datos/tareas.json'

    def __init__(self):
        self.__tareas = []
        self.__cargarDatos()

    def __cargarDatos(self):
        try:
            with open(RepositorioTareas.__ruta_archivo, 'r', encoding="utf8") as archivo:
                dicc_guardado = json.load(archivo)
                Tarea.establecer_ultimo_id(dicc_guardado['ultimo_id'])
                lista_datos = dicc_guardado['tareas']
                for tarea in lista_datos:
                    self.__tareas.append(Tarea.fromDiccionario(tarea))
        except FileNotFoundError:
            print(f'No se encontró el archivo tareas.json')

    def __guardarDatos(self):
        try:
            with open(RepositorioTareas.__ruta_archivo, 'w', encoding="utf8") as archivo:
                lista_datos = []
                for tarea in self.__tareas:
                    lista_datos.append(tarea.toDiccionario())

                dicc_a_guardar = {
                    "ultimo_id": Tarea.obtener_ultimo_id(),
                    "tareas": lista_datos
                }                
                json.dump(dicc_a_guardar, archivo, indent=4)
        except FileNotFoundError:
            print(f'No se encontró el archivo tareas.json')

    def obtenerTodas(self):
        return self.__tareas
    
    def obtenerPorId(self, id:int)->Tarea:
        if not isinstance(id, int) or id < 0:
            raise ValueError(f'El id debe ser un entero positivo')
        for tarea in self.__tareas:
            if isinstance(tarea, Tarea) :
                if tarea.obtener_id() == id:
                    return tarea
        return None
    
    def existeTarea(self, titulo:str)->bool:
        if not isinstance(titulo, str) or titulo == "" or titulo.isspace():
            raise ValueError(f'El titulo debe ser de tipo string y no estar vacío')
        for tarea in self.__tareas:            
            if tarea.obtener_titulo() == titulo:
                return True
        return False

    def agregar(self, tarea:Tarea):
        if not isinstance(tarea, Tarea):
            raise ValueError(f'El objeto tarea debe ser de tipo Tarea')
        if not self.existeTarea(tarea.obtener_titulo()):
            self.__tareas.append(tarea)
            self.__guardarDatos()
        else:
            raise ValueError(f'La tarea ya existe con el título: {tarea.obtener_titulo()}')
    
    def actualizar(self, id: int, dicc: dict):
        if not isinstance(dicc, dict):
            raise ValueError(f'El diccionario debe ser de tipo dict')
        if not isinstance(id, int) or id < 0:
            raise ValueError(f'El id debe ser un entero positivo')
        tarea = self.obtenerPorId(id)
        if tarea is not None:
            if "titulo" in dicc:
                tarea.establecer_titulo(dicc['titulo'])
            if "descripcion" in dicc:
                tarea.establecer_descripcion(dicc['descripcion'])
            if "completada" in dicc:
                tarea.establecer_completada(dicc['completada'])
            self.__guardarDatos()
            
        return tarea #aca puede ser None o un objeto de Tarea con los datos actualizados
    
    def eliminar(self, id:int):
        if not isinstance(id, int) or id < 0:
            raise ValueError(f'El id debe ser un entero positivo')
        for t in self.__tareas:
            if t.obtener_id() == id:
                self.__tareas.remove(t)
                self.__guardarDatos()
                return True
        return False
    
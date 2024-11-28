from modelos.repositorios.repositorio_tareas import RepositorioTareas

tareas= None

def obtenerRepoTareas():
    global tareas
    if tareas is None:
        tareas = RepositorioTareas()
    return tareas

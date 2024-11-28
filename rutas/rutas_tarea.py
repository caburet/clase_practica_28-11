from flask import Blueprint, jsonify, request
from modelos.entidades.tarea import Tarea
from modelos.repositorios.repositorios import obtenerRepoTareas

repo_tareas = obtenerRepoTareas()
bp_tareas = Blueprint("bp_tareas", __name__)

# /tareas    get    TODAS LAS TAREAS
# /tareas/id GET    UNA TAREA, con ese id
# /tareas/   POST   AGREGAR UNA TAREA
# /tareas/ID  PUT    MODIFICAR UNA TAREA
# /tareas/ID  DELETE  BORRAR UNA TAREA

# CRUD (ABM) Alta Baja y Modificaciones

@bp_tareas.route('/tareas', methods=['GET'])
def obtener_tareas():
    todas= repo_tareas.obtenerTodas()
    if todas:
        return jsonify (tarea.toDiccionario() for tarea in repo_tareas.obtenerTodas())
    else:
        return []

@bp_tareas.route('/tareas/<int:id>', methods=['GET'])
def obtener_tarea(id):
    tarea = repo_tareas.obtenerPorId(id)
    if tarea:
        return jsonify(tarea.toDiccionario()),200
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    

            #     "titulo": self.__titulo,
            # "descripcion": self.__descripcion,
            # "completada": self.__completada,
            # "fecha_creacion": self.__fecha_creacion  STRING
@bp_tareas.route('/tareas', methods=['POST'])
def agregar_tarea():
    if request.is_json:
        tarea_data = request.get_json()
        if "titulo" in tarea_data and "descripcion" in tarea_data and "completada" in tarea_data and "fecha_creacion" in tarea_data:
            try:
                tarea = Tarea.fromDiccionario(tarea_data)
                repo_tareas.agregar(tarea) # tarea ya exista? No tiene que crear de nuevo
                return jsonify(tarea.toDiccionario()), 201
            except ValueError as e:
                return jsonify({'error': str(e)}), 400
        else:
            return jsonify({'error': 'Faltan datos en el request. Necesita titulo,descripcion, completada y fecha de creacion '}), 400            
    else:
        return jsonify({'error': 'Solicitud incorrecta, debe ser en formato JSON'}), 400

@bp_tareas.route('/tareas/<int:id>', methods=['PUT'])
def modificar_tarea(id):
    if request.is_json:
        tarea_data = request.get_json()
        tarea = repo_tareas.obtenerPorId(id)
        if tarea:
            tarea_return= repo_tareas.actualizar(id,tarea_data)
            return jsonify(tarea_return.toDiccionario()), 200
        else:
            return jsonify({'error': 'Tarea no encontrada'}), 404
    else:
        return jsonify({'error': 'Solicitud incorrecta, debe ser en formato JSON'}),

@bp_tareas.route('/tareas/<int:id>', methods=['DELETE'])
def eliminar_tarea(id):
    tarea = repo_tareas.obtenerPorId(id)
    if tarea:
        repo_tareas.eliminar(id)
        return jsonify({'message': 'Tarea eliminada'}), 200
    else:
        return jsonify({'error': 'Tarea no encontrada'}), 404
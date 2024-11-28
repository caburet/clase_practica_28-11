from flask import Flask
from rutas.rutas_tarea import bp_tareas

app = Flask(__name__)

app.register_blueprint(bp_tareas)

if __name__ == "__main__":
    app.run(debug=True)
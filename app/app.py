"""
Aplicación web de to-do list simple usando Flask.
Permite agregar, eliminar y marcar todos como completados
a través de un formulario HTML.
"""

# app/app.py
import os
from flask import Flask, render_template, request
from .todo import (
    agregar_todo,
    eliminar_todo,
    marcar_completado,
    obtener_todos,
    limpiar_completados,
)

app = Flask(__name__)
app.config["DEBUG"] = False

# Lista global simple en memoria
todos_globales = []


@app.route("/health")
def health():
    return "OK", 200


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja la página principal y el formulario de la to-do list."""
    global todos_globales
    todos = todos_globales
    mensaje = None

    if request.method == "POST":
        try:
            accion = request.form["accion"]

            if accion == "agregar":
                texto = request.form["texto"]
                if texto.strip():  # Verificar que no esté vacío
                    agregar_todo(todos, texto)
                    mensaje = "Todo agregado exitosamente"
                else:
                    mensaje = "Error: El texto no puede estar vacío"
            elif accion == "eliminar":
                todo_id = int(request.form["todo_id"])
                if eliminar_todo(todos, todo_id):
                    mensaje = "Todo eliminado exitosamente"
                else:
                    mensaje = "Error: Todo no encontrado"
            elif accion == "completar":
                todo_id = int(request.form["todo_id"])
                resultado = marcar_completado(todos, todo_id)
                if resultado:
                    mensaje = "Todo marcado como completado"
                else:
                    # Verificar si el todo existe pero ya está completado
                    todo_existe = any(todo["id"] == todo_id for todo in todos)
                    if todo_existe:
                        mensaje = "Error: Este todo ya está completado"
                    else:
                        mensaje = "Error: Todo no encontrado"
            elif accion == "limpiar":
                limpiar_completados(todos)
                mensaje = "Todos completados eliminados"
            else:
                mensaje = "Acción no válida"
        except ValueError as e:
            mensaje = f"Error: {str(e)}"
        except Exception as e:
            mensaje = f"Error inesperado: {str(e)}"

    return render_template("index.html", todos=todos, mensaje=mensaje)


if __name__ == "__main__":  # pragma: no cover
    app_port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=app_port, host="0.0.0.0")

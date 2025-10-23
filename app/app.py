"""
Aplicación web de to-do list simple usando Flask.
Permite agregar, eliminar y marcar todos como completados
a través de un formulario HTML.
"""

# app/app.py
import os
from flask import Flask, render_template, request
from .todo import agregar_todo, eliminar_todo, marcar_completado, obtener_todos, limpiar_completados

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/health")
def health():
    return "OK", 200


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja la página principal y el formulario de la to-do list."""
    # Lista simple en memoria (en producción usarías una base de datos)
    todos = obtener_todos([])
    mensaje = None
    
    if request.method == "POST":
        try:
            accion = request.form["accion"]
            
            if accion == "agregar":
                texto = request.form["texto"]
                agregar_todo(todos, texto)
                mensaje = "Todo agregado exitosamente"
            elif accion == "eliminar":
                todo_id = int(request.form["todo_id"])
                eliminar_todo(todos, todo_id)
                mensaje = "Todo eliminado exitosamente"
            elif accion == "completar":
                todo_id = int(request.form["todo_id"])
                marcar_completado(todos, todo_id)
                mensaje = "Todo marcado como completado"
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

"""
Aplicación web de to-do list simple usando Flask.
Permite agregar, eliminar y marcar todos como completados
a través de un formulario HTML.
"""

# app/app.py
import os
from flask import Flask, render_template, request, session
from todo import (
    agregar_todo,
    eliminar_todo,
    marcar_completado,
    obtener_todos,
    limpiar_completados,
)

app = Flask(__name__)
app.config["DEBUG"] = False
app.secret_key = "tu_clave_secreta_aqui"  # Para usar sesiones


@app.route("/health")
def health():
    return "OK", 200


@app.route("/", methods=["GET", "POST"])
def index():
    """Maneja la página principal y el formulario de la to-do list."""
    # Usar sesión para mantener los todos entre requests
    if "todos" not in session:
        session["todos"] = []

    todos = session["todos"]
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
                if marcar_completado(todos, todo_id):
                    mensaje = "Todo marcado como completado"
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

        # Guardar los todos actualizados en la sesión
        session["todos"] = todos

    return render_template("index.html", todos=todos, mensaje=mensaje)


if __name__ == "__main__":  # pragma: no cover
    app_port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, port=app_port, host="0.0.0.0")

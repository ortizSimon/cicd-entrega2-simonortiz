"""
Aplicación web de to-do list
Funciones Basicas: agregar, eliminar, marcar_completado, obtener_todos
"""


# app/todo.py
def agregar_todo(todos, texto):
    """Agrega un nuevo todo a la lista."""
    if not texto or not texto.strip():
        raise ValueError("El texto del todo no puede estar vacío")

    # Generar ID único basado en el ID más alto existente + 1
    max_id = max([todo["id"] for todo in todos], default=0)
    nuevo_todo = {"id": max_id + 1, "texto": texto.strip(), "completado": False}
    todos.append(nuevo_todo)
    return nuevo_todo


def eliminar_todo(todos, todo_id):
    """Elimina un todo de la lista por ID."""
    if todo_id <= 0:
        return False
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos.pop(i)
            return True
    return False


def marcar_completado(todos, todo_id):
    """Marca un todo como completado."""
    if todo_id <= 0:
        return False
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completado"] = True
            return True
    return False


def obtener_todos(todos):
    """Devuelve todos los todos."""
    return todos


def limpiar_completados(todos):
    """Elimina todos los todos completados."""
    todos_completados = [todo for todo in todos if todo["completado"]]
    todos[:] = [todo for todo in todos if not todo["completado"]]
    return todos_completados

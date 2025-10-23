"""
Aplicación web de to-do list
Funciones Basicas: agregar, eliminar, marcar_completado, obtener_todos
"""


# app/todo.py
def agregar_todo(todos, texto):
    """Agrega un nuevo todo a la lista."""
    if not texto or not texto.strip():
        raise ValueError("El texto del todo no puede estar vacío")
    nuevo_todo = {"id": len(todos) + 1, "texto": texto.strip(), "completado": False}
    todos.append(nuevo_todo)
    return nuevo_todo


def eliminar_todo(todos, todo_id):
    """Elimina un todo de la lista por ID."""
    if todo_id <= 0:
        raise ValueError("ID de todo inválido")
    for i, todo in enumerate(todos):
        if todo["id"] == todo_id:
            return todos.pop(i)
    raise ValueError("Todo no encontrado")


def marcar_completado(todos, todo_id):
    """Marca un todo como completado."""
    if todo_id <= 0:
        raise ValueError("ID de todo inválido")
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completado"] = True
            return todo
    raise ValueError("Todo no encontrado")


def obtener_todos(todos):
    """Devuelve todos los todos."""
    return todos


def limpiar_completados(todos):
    """Elimina todos los todos completados."""
    todos_completados = [todo for todo in todos if todo["completado"]]
    todos[:] = [todo for todo in todos if not todo["completado"]]
    return todos_completados

# tests/test_todo.py
import pytest
from app.todo import agregar_todo, eliminar_todo, marcar_completado, obtener_todos, limpiar_completados

def test_agregar_todo():
    todos = []
    todo = agregar_todo(todos, "Hacer ejercicio")
    assert todo["texto"] == "Hacer ejercicio"
    assert todo["completado"] == False
    assert len(todos) == 1
    assert todos[0]["id"] == 1

def test_eliminar_todo():
    todos = []
    agregar_todo(todos, "Todo 1")
    agregar_todo(todos, "Todo 2")
    todo_eliminado = eliminar_todo(todos, 1)
    assert todo_eliminado["texto"] == "Todo 1"
    assert len(todos) == 1
    assert todos[0]["texto"] == "Todo 2"

def test_marcar_completado():
    todos = []
    agregar_todo(todos, "Todo pendiente")
    todo_completado = marcar_completado(todos, 1)
    assert todo_completado["completado"] == True
    assert todos[0]["completado"] == True

def test_obtener_todos():
    todos = []
    agregar_todo(todos, "Todo 1")
    agregar_todo(todos, "Todo 2")
    todos_obtenidos = obtener_todos(todos)
    assert len(todos_obtenidos) == 2
    assert todos_obtenidos[0]["texto"] == "Todo 1"

def test_limpiar_completados():
    todos = []
    agregar_todo(todos, "Todo 1")
    agregar_todo(todos, "Todo 2")
    marcar_completado(todos, 1)
    completados_eliminados = limpiar_completados(todos)
    assert len(todos) == 1
    assert len(completados_eliminados) == 1
    assert todos[0]["texto"] == "Todo 2"

def test_agregar_todo_texto_vacio():
    todos = []
    with pytest.raises(ValueError):
        agregar_todo(todos, "")

def test_eliminar_todo_id_invalido():
    todos = []
    with pytest.raises(ValueError):
        eliminar_todo(todos, 0)

def test_eliminar_todo_no_encontrado():
    todos = []
    with pytest.raises(ValueError):
        eliminar_todo(todos, 999)

def test_marcar_completado_id_invalido():
    todos = []
    with pytest.raises(ValueError):
        marcar_completado(todos, 0)

def test_marcar_completado_no_encontrado():
    todos = []
    with pytest.raises(ValueError):
        marcar_completado(todos, 999)

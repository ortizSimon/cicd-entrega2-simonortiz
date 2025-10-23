# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert '<!DOCTYPE html>' in response.data.decode('utf-8')

def test_index_post_agregar(client):
    response = client.post('/', data={'accion': 'agregar', 'texto': 'Nuevo todo'})
    assert response.status_code == 200
    assert 'Nuevo todo' in response.data.decode('utf-8')

def test_index_post_eliminar(client):
    # Primero agregar un todo
    client.post('/', data={'accion': 'agregar', 'texto': 'Todo a eliminar'})
    # Luego eliminarlo
    response = client.post('/', data={'accion': 'eliminar', 'todo_id': '1'})
    assert response.status_code == 200
    assert 'Todo eliminado exitosamente' in response.data.decode('utf-8')

def test_index_post_completar(client):
    # Primero agregar un todo
    client.post('/', data={'accion': 'agregar', 'texto': 'Todo a completar'})
    # Luego completarlo
    response = client.post('/', data={'accion': 'completar', 'todo_id': '1'})
    assert response.status_code == 200
    assert 'Todo marcado como completado' in response.data.decode('utf-8')

def test_index_post_limpiar(client):
    # Primero agregar y completar un todo
    client.post('/', data={'accion': 'agregar', 'texto': 'Todo a limpiar'})
    client.post('/', data={'accion': 'completar', 'todo_id': '1'})
    # Luego limpiar completados
    response = client.post('/', data={'accion': 'limpiar'})
    assert response.status_code == 200
    assert 'Todos completados eliminados' in response.data.decode('utf-8')

def test_index_post_texto_vacio(client):
    response = client.post('/', data={'accion': 'agregar', 'texto': ''})
    assert response.status_code == 200
    assert 'Error:' in response.data.decode('utf-8')

def test_index_post_id_invalido(client):
    response = client.post('/', data={'accion': 'eliminar', 'todo_id': '0'})
    assert response.status_code == 200
    assert 'Error:' in response.data.decode('utf-8')

def test_index_post_accion_invalida(client):
    response = client.post('/', data={'accion': 'invalid', 'texto': 'test'})
    assert response.status_code == 200
    assert 'Acción no válida' in response.data.decode('utf-8')
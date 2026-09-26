import pytest
from fastapi.testclient import TestClient
from Maria.main import app

client = TestClient(app)

def test_obtener_videojuegos():
    """Prueba unitaria para verificar que el endpoint GET responde 200 y retorna una lista"""
    response = client.get("/videojuegos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_crear_y_eliminar_videojuego():
    """Prueba el flujo completo: crear un registro (POST) y luego eliminarlo (DELETE)"""
    nuevo_juego = {
        "titulo": "Juego Prueba Pytest",
        "plataforma": "PC",
        "genero": "Aventura",
        "precio": 10.0
    }
    # 1. Crear
    post_response = client.post("/videojuegos", json=nuevo_juego)
    assert post_response.status_code == 201
    data = post_response.json()
    assert "id" in data
    juego_id = data["id"]

    # 2. Eliminar
    delete_response = client.delete(f"/videojuegos/{juego_id}")
    assert delete_response.status_code == 204
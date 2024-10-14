from http import HTTPStatus
from fast_zero.app import app
from fastapi.testclient import TestClient


def test_read_root_return_ok():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}

def test_read_root_html_return_ok():
    client = TestClient(app)

    response = client.get('/challange')
    response_html = '<h1> Olá Mundo </h1>'

    assert response.status_code == HTTPStatus.OK
    assert response_html in response.text
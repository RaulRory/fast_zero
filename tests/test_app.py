from http import HTTPStatus


def test_read_root_return_ok(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}

def test_read_root_html_return_ok(client):
    response = client.get('/challange')
    response_html = '<h1> Olá Mundo </h1>'

    assert response.status_code == HTTPStatus.OK
    assert response_html in response.text

def test_create_user(client):
    response = client.post("/users", 
                json={
                    'username': 'user_test',
                    'password': 'password',
                    'email': 'test@io.com.br'
                }
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'user_test',
        'email': 'test@io.com.br',
        'id': 1
    }

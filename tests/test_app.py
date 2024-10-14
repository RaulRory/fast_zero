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


def test_read_user(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'user_test',
                'email': 'test@io.com.br',
                'id': 1
            }
        ]
    }


def test_find_user(client):
    response = client.get('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
                'username': 'user_test',
                'email': 'test@io.com.br',
                'id': 1
            }

def test_find_user_not_found(client):
    response = client.get('/users/99')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == { 'detail': 'User not found'}


def test_update_user(client):
    response = client.put('/users/1',
                          json={
                              'password': 'password',
                              'username': 'user_test_update',
                              'email': 'update@io.com.br',
                            }
                        )

    assert response.status_code == HTTPStatus.OK
    assert response.json() ==  {
                'username': 'user_test_update',
                'email': 'update@io.com.br',
                'id': 1
            }


def test_update_user_not_found(client):
    response = client.put('/users/99',
                          json={
                              'password': 'password',
                              'username': 'user_test_update',
                              'email': 'update@io.com.br',
                            }
                        )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == { 'detail': 'User not found'}


def test_delete_user_not_found(client):
    response = client.delete('/users/99')

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == { 'detail': 'User not found'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deletd!'}

import pytest
import allure

@allure.feature("Posts")
@allure.story("CRUD Operations")
def test_get_all_posts(api_client):
    with allure.step("Отправляем запрос на получение всех постов"):
        response = api_client.get_all_posts()
    assert response.status_code == 200
    posts = response.json()
    with allure.step("Проверяем количество постов"):
        assert len(posts) == 100
    with allure.step("Проверяем структуру данных первого поста"):
        assert all(key in posts[0] for key in ['userId', 'id', 'title', 'body'])

@allure.feature("Posts")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("post_id,expected_user", [(1, 1), (50, 5), (100, 10)])
def test_get_post_by_id(api_client, post_id, expected_user):
    with allure.step(f"Получаем пост с ID {post_id}"):
        response = api_client.get_post_by_id(post_id)
    assert response.status_code == 200
    post = response.json()
    with allure.step(f"Проверяем, что ID поста равен {post_id}"):
        assert post['id'] == post_id
    with allure.step(f"Проверяем, что userId равен {expected_user}"):
        assert post['userId'] == expected_user

@allure.feature("Posts")
@allure.story("CRUD Operations")
def test_create_post(api_client):
    new_post = {"title": "foo", "body": "bar", "userId": 1}
    with allure.step("Создаём новый пост"):
        response = api_client.create_post(new_post)
    assert response.status_code == 201
    created_post = response.json()
    with allure.step("Проверяем, что новый пост имеет ID=101"):
        assert created_post['id'] == 101  # API возвращает фиксированный ID

@allure.feature("Posts")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_update_post(api_client, post_id):
    updated_data = {
        "title": "Updated Title",
        "body": "Updated Content",
        "userId": 1
    }
    with allure.step(f"Обновляем пост с ID {post_id}"):
        response = api_client.update_post(post_id, updated_data)
    assert response.status_code == 200
    updated_post = response.json()
    with allure.step("Проверяем обновлённые данные"):
        assert updated_post["title"] == updated_data["title"]
        assert updated_post["body"] == updated_data["body"]

@allure.feature("Posts")
@allure.story("Фильтрация")
def test_get_posts_with_query_params(api_client):
    with allure.step("Получаем посты пользователя с ID=1"):
        response = api_client.get_posts_by_user(1)
    assert response.status_code == 200
    posts = response.json()
    with allure.step("Проверяем, что все посты принадлежат пользователю ID=1"):
        assert all(post["userId"] == 1 for post in posts)
    with allure.step("Проверяем количество постов"):
        assert len(posts) == 10

@allure.feature("Posts")
@allure.story("CRUD Operations")
def test_delete_post(api_client):
    with allure.step("Удаляем пост с ID=1"):
        response = api_client.delete_post(1)
    assert response.status_code == 200

# Тесты для USERS
@allure.feature("Users")
@allure.story("CRUD Operations")
def test_get_all_users(api_client):
    with allure.step("Отправляем запрос на получение всех пользователей"):
        response = api_client.get_all_users()
    assert response.status_code == 200
    users = response.json()
    with allure.step("Проверяем количество пользователей"):
        assert len(users) == 10
    with allure.step("Проверяем наличие ключей 'id' и 'name' у каждого пользователя"):
        assert all('id' in user and 'name' in user for user in users)

@allure.feature("Users")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("user_id", [1, 5, 10])
def test_get_user_by_id(api_client, user_id):
    with allure.step(f"Получаем пользователя с ID {user_id}"):
        response = api_client.get_user_by_id(user_id)
    assert response.status_code == 200
    user = response.json()
    with allure.step(f"Проверяем, что ID пользователя равен {user_id}"):
        assert user["id"] == user_id
    with allure.step("Проверяем наличие ключей 'name', 'email', 'address'"):
        assert "name" in user and "email" in user and "address" in user

@allure.feature("Users")
@allure.story("Data Structure")
def test_user_address_structure(api_client):
    with allure.step("Получаем список всех пользователей"):
        response = api_client.get_all_users()
    assert response.status_code == 200
    users = response.json()
    with allure.step("Проверяем структуру поля 'address' у каждого пользователя"):
        for user in users:
            assert "address" in user
            address = user["address"]
            assert all(key in address for key in ['street', 'suite', 'city', 'zipcode'])

# Тесты для ALBUMS
@allure.feature("Albums")
@allure.story("CRUD Operations")
def test_get_all_albums(api_client):
    with allure.step("Отправляем запрос на получение всех альбомов"):
        response = api_client.get_all_albums()
    assert response.status_code == 200
    albums = response.json()
    with allure.step("Проверяем количество альбомов"):
        assert len(albums) == 100
    with allure.step("Проверяем структуру данных первого альбома"):
        assert all(key in albums[0] for key in ['userId', 'id', 'title'])

@allure.feature("Albums")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("album_id", [1, 50, 100])
def test_get_album_by_id(api_client, album_id):
    with allure.step(f"Получаем альбом с ID {album_id}"):
        response = api_client.get_album_by_id(album_id)
    assert response.status_code == 200
    album = response.json()
    with allure.step(f"Проверяем, что ID альбома равен {album_id}"):
        assert album["id"] == album_id
    with allure.step("Проверяем наличие ключей 'title' и 'userId'"):
        assert "title" in album and "userId" in album

@allure.feature("Albums")
@allure.story("Фильтрация")
def test_get_albums_by_user(api_client):
    with allure.step("Получаем альбомы пользователя с ID=1"):
        response = api_client.get_albums_by_user(1)
    assert response.status_code == 200
    albums = response.json()
    with allure.step("Проверяем, что все альбомы принадлежат пользователю ID=1"):
        assert all(album['userId'] == 1 for album in albums)

@allure.feature("Albums")
@allure.story("CRUD Operations")
def test_create_album(api_client):
    new_album = {
        "title": "New Album",
        "userId": 1
    }
    with allure.step("Создаём новый альбом"):
        response = api_client.create_album(new_album)
    assert response.status_code == 201
    created_album = response.json()
    with allure.step("Проверяем данные созданного альбома"):
        assert created_album["title"] == new_album["title"]
        assert created_album["userId"] == new_album["userId"]

# Тесты для PHOTOS
@allure.feature("Photos")
@allure.story("CRUD Operations")
def test_get_photos_in_album(api_client):
    with allure.step("Получаем фото из альбома с ID=1"):
        response = api_client.get_photos_in_album(1)
    assert response.status_code == 200
    photos = response.json()
    with allure.step("Проверяем, что все фото принадлежат альбому ID=1"):
        assert all(photo['albumId'] == 1 for photo in photos)

@allure.feature("Photos")
@allure.story("CRUD Operations")
def test_get_photo_by_id(api_client):
    with allure.step("Получаем фото с ID=1"):
        response = api_client.get_photo_by_id(1)
    assert response.status_code == 200
    photo = response.json()
    with allure.step("Проверяем, что ID фото равен 1"):
        assert photo["id"] == 1
    with allure.step("Проверяем структуру данных фото"):
        assert all(key in photo for key in ['albumId', 'title', 'url', 'thumbnailUrl'])

@allure.feature("Photos")
@allure.story("CRUD Operations")
def test_get_all_photos(api_client):
    with allure.step("Отправляем запрос на получение всех фото"):
        response = api_client.get_all_photos()
    assert response.status_code == 200
    photos = response.json()
    with allure.step("Проверяем количество фото"):
        assert len(photos) == 5000
    with allure.step("Проверяем структуру данных первого фото"):
        assert all(key in photos[0] for key in ['id', 'albumId', 'title', 'url'])

# Тесты для COMMENTS
@allure.feature("Comments")
@allure.story("CRUD Operations")
def test_get_all_comments(api_client):
    with allure.step("Отправляем запрос на получение всех комментариев"):
        response = api_client.get_all_comments()
    assert response.status_code == 200
    comments = response.json()
    with allure.step("Проверяем количество комментариев"):
        assert len(comments) == 500
    with allure.step("Проверяем структуру данных первого комментария"):
        assert all(key in comments[0] for key in ['postId', 'id', 'name', 'email', 'body'])

@allure.feature("Comments")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("post_id", [1, 10, 50])
def test_get_comments_by_post_id(api_client, post_id):
    with allure.step(f"Получаем комментарии для поста с ID {post_id}"):
        response = api_client.get_comments_by_post_id(post_id)
    assert response.status_code == 200
    comments = response.json()
    with allure.step(f"Проверяем, что все комментарии принадлежат посту ID={post_id}"):
        assert all(comment["postId"] == post_id for comment in comments)

@allure.feature("Comments")
@allure.story("CRUD Operations")
def test_create_comment(api_client):
    new_comment = {
        "postId": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "body": "Great post!"
    }
    with allure.step("Создаём новый комментарий"):
        response = api_client.create_comment(new_comment)
    assert response.status_code == 201
    created_comment = response.json()
    with allure.step("Проверяем данные созданного комментария"):
        assert created_comment["postId"] == new_comment["postId"]
        assert created_comment["email"] == new_comment["email"]

# Тесты для TODOS
@allure.feature("Todos")
@allure.story("CRUD Operations")
def test_get_all_todos(api_client):
    with allure.step("Отправляем запрос на получение всех задач"):
        response = api_client.get_all_todos()
    assert response.status_code == 200
    todos = response.json()
    with allure.step("Проверяем количество задач"):
        assert len(todos) == 200
    with allure.step("Проверяем структуру данных первой задачи"):
        assert all(key in todos[0] for key in ['userId', 'id', 'title', 'completed'])

@allure.feature("Todos")
@allure.story("CRUD Operations")
def test_create_todo(api_client):
    new_todo = {
        "userId": 1,
        "title": "Buy a guitar",
        "completed": False
    }
    with allure.step("Создаём новую задачу"):
        response = api_client.create_todo(new_todo)
    assert response.status_code == 201
    created_todo = response.json()
    with allure.step("Проверяем данные созданной задачи"):
        assert created_todo["title"] == new_todo["title"]
        assert created_todo["userId"] == new_todo["userId"]
        assert created_todo["completed"] == new_todo["completed"]

@allure.feature("Todos")
@allure.story("CRUD Operations")
def test_update_todo(api_client):
    updated_data = {
        "title": "Learn to play guitar",
        "completed": True
    }
    with allure.step("Обновляем задачу с ID=1"):
        response = api_client.update_todo(1, updated_data)
    assert response.status_code == 200
    updated_todo = response.json()
    with allure.step("Проверяем обновлённые данные"):
        assert updated_todo["title"] == updated_data["title"]
        assert updated_todo["completed"] == updated_data["completed"]

@allure.feature("Todos")
@allure.story("CRUD Operations")
@pytest.mark.parametrize("todo_id", [1, 100, 200])
def test_get_todo_by_id(api_client, todo_id):
    with allure.step(f"Получаем задачу с ID {todo_id}"):
        response = api_client.get_todo_by_id(todo_id)
    assert response.status_code == 200
    todo = response.json()
    with allure.step(f"Проверяем, что ID задачи равен {todo_id}"):
        assert todo["id"] == todo_id
    with allure.step("Проверяем наличие ключей 'userId', 'title', 'completed'"):
        assert "userId" in todo and "title" in todo and "completed" in todo

@allure.feature("Todos")
@allure.story("CRUD Operations")
def test_delete_todo(api_client):
    with allure.step("Удаляем задачу с ID=1"):
        response = api_client.delete_todo(1)
    assert response.status_code == 200

@allure.feature("Todos")
@allure.story("Фильтрация")
def test_get_todos_by_user(api_client):
    with allure.step("Получаем задачи пользователя с ID=1"):
        response = api_client.get_todos_by_user(1)
    assert response.status_code == 200
    todos = response.json()
    with allure.step("Проверяем, что все задачи принадлежат пользователю ID=1"):
        assert all(todo['userId'] == 1 for todo in todos)
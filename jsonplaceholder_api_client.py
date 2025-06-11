import requests

class JsonPlaceholderApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    # Posts endpoints
    def get_all_posts(self):
        return self.session.get(f"{self.base_url}/posts")

    def get_post_by_id(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}")

    def create_post(self, data):
        return self.session.post(f"{self.base_url}/posts", json=data)

    def update_post(self, post_id, data):
        return self.session.put(f"{self.base_url}/posts/{post_id}", json=data)

    def delete_post(self, post_id):
        return self.session.delete(f"{self.base_url}/posts/{post_id}")

    def get_comments_for_post(self, post_id):
        return self.session.get(f"{self.base_url}/posts/{post_id}/comments")

    def get_posts_by_user(self, user_id):
        return self.session.get(f"{self.base_url}/posts?userId={user_id}")

    # Users endpoints
    def get_all_users(self):
        return self.session.get(f"{self.base_url}/users")

    def get_user_by_id(self, user_id):
        return self.session.get(f"{self.base_url}/users/{user_id}")

    # Comments endpoints
    def get_all_comments(self):
        return self.session.get(f"{self.base_url}/comments")

    def get_comments_by_post_id(self, post_id):
        return self.session.get(f"{self.base_url}/comments?postId={post_id}")

    # Albums endpoints
    def get_all_albums(self):
        return self.session.get(f"{self.base_url}/albums")

    def get_album_by_id(self, album_id):
        return self.session.get(f"{self.base_url}/albums/{album_id}")

    def create_album(self, data):
        return self.session.post(f"{self.base_url}/albums", json=data)

    def get_photos_in_album(self, album_id):
        return self.session.get(f"{self.base_url}/albums/{album_id}/photos")

    def get_albums_by_user(self, user_id):
        return self.session.get(f"{self.base_url}/albums?userId={user_id}")

    # Photos endpoints
    def get_all_photos(self):
        return self.session.get(f"{self.base_url}/photos")

    def get_photo_by_id(self, photo_id):
        return self.session.get(f"{self.base_url}/photos/{photo_id}")

    # Todos endpoints
    def get_all_todos(self):
        return self.session.get(f"{self.base_url}/todos")

    def get_todo_by_id(self, todo_id):
        return self.session.get(f"{self.base_url}/todos/{todo_id}")

    def get_todos_by_user(self, user_id):
        return self.session.get(f"{self.base_url}/todos?userId={user_id}")

    def create_todo(self, data):
        return self.session.post(f"{self.base_url}/todos", json=data)

    def update_todo(self, todo_id, data):
        return self.session.put(f"{self.base_url}/todos/{todo_id}", json=data)

    # Comments endpoints
    def create_comment(self, data):
        return self.session.post(f"{self.base_url}/comments", json=data)

    # Todos endpoints
    def delete_todo(self, todo_id):
        return self.session.delete(f"{self.base_url}/todos/{todo_id}")
import requests


class APIClient:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_post(self, post_id):
        url = f"{self.BASE_URL}/posts/{post_id}"
        response = requests.get(url)
        return response

    def create_post(self, title, body, user_id):
        url = f"{self.BASE_URL}/posts"

        data = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        response = requests.post(url, json=data)
        return response
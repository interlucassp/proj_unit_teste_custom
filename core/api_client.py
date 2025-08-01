import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_users(self):
        return requests.get(f"{self.base_url}/users")

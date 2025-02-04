from playwright.sync_api import sync_playwright


class APIClient:
    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.playwright = sync_playwright().start()
        self.request = self.playwright.request.new_context()
        self.token = None

        if username and password:
            self.authenticate(username, password)


    def authenticate(self, username, password):
        response = self.request.post(f"{self.base_url}/auth/login", data={"username": username, "password": password})
        if response.status == 200:
            self.token = response.json().get("access_token")
        else:
            raise Exception("Authorization error!")

    def _add_auth_header(self, headers=None):
        if self.token:
            if headers is None:
                headers = {}
            headers["Authorization"] = f"Bearer {self.token}"

    
    def post(self, endpoint, data=None, headers=None):
        response = self.request.post(f"{self.base_url}{endpoint}", data = data, headers = headers)
        return response

    def get(self, endpoint, params=None, headers=None):
        response = self.request.get(f"{self.base_url}{endpoint}", params=params, headers=headers)
        return response

    def put(self, endpoint, data=None, headers=None):
        response = self.request.put(f"{self.base_url}{endpoint}", data=data, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        response = self.request.delete(f"{self.base_url}{endpoint}", headers=headers)
        return response

    def close(self):
        self.request.dispose()
        self.playwright.stop()

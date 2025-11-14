import requests
import allure


class Authorize:
    url = 'http://memesapi.course.qa-practice.com/authorize'
    token = None

    @allure.step("Authorize user and get token")
    def get_token(self, name):
        response = requests.post(self.url, json={"name": name})
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        self.token = response.json()["token"]
        return self.token

    @allure.step("Check if token is alive")
    def check_token(self, token):
        response = requests.get(f"{self.url}/{token}")
        self.response = response
        return response

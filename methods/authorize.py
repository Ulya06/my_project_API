import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class Authorize(MemeEndpoint):

    url = "http://memesapi.course.qa-practice.com/authorize"

    token = None


    @allure.step("Get token")
    def get_token(self, name):

        self.response = requests.post(
            self.url,
            json={"name": name}
        )

        self.check_status_code(200)

        self.token = self.json["token"]

        return self.token


    @allure.step("Check token")
    def check_token(self, token):

        self.response = requests.get(
            f"{self.url}/{token}"
        )

        return self.response

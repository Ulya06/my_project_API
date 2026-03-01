import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class Authorize(MemeEndpoint):
    url = "http://memesapi.course.qa-practice.com/authorize"

    @allure.step("Get token")
    def get_token(self, name):
        self.response = requests.post(
            self.url,
            json={"name": name}
        )

        return self.response


    @allure.step("Check token validity")
    def check_token(self, token):
        self.response = requests.get(
            f"{self.url}/{token}"
        )

        return self.response

import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class CreateMeme(MemeEndpoint):
    @allure.step("Create new meme")
    def create_new_meme(self, body):
        self.response = requests.post(self.url, json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response

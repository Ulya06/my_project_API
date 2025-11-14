import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class GetMeme(MemeEndpoint):
    @allure.step("Get meme by ID")
    def get_meme(self, meme_id):
        self.response = requests.get(f"{self.url}/{meme_id}", headers=self.headers)
        self.json = self.response.json() if self.response.ok else None
        return self.response

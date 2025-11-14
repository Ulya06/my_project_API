import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class PutMeme(MemeEndpoint):
    @allure.step("Update meme with PUT")
    def put_meme(self, body, meme_id):
        self.response = requests.put(f"{self.url}/{meme_id}", json=body, headers=self.headers)
        self.json = self.response.json()
        return self.response

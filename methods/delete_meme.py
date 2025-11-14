import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class DeleteMeme(MemeEndpoint):
    @allure.step("Delete meme")
    def delete_meme(self, meme_id):
        self.response = requests.delete(f"{self.url}/{meme_id}", headers=self.headers)
        return self.response

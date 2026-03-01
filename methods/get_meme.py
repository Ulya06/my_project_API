import requests
import allure


from methods.meme_endpoint import MemeEndpoint


class GetMeme(MemeEndpoint):

    @allure.step("Get meme by id")
    def get_meme(self, meme_id):
        self.response = requests.get(
            f"{self.url}/{meme_id}",
            headers=self.headers
        )

        return self.response

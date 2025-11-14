import allure


class MemeEndpoint:
    url = 'http://memesapi.course.qa-practice.com/meme'
    headers = None
    response = None
    json = None

    def set_token(self, token):
        self.headers = {"Authorization": token, "Content-Type": "application/json"}


    @allure.step("Check status code 200")
    def check_statuscode_is_200(self):
        assert self.response.status_code == 200, f"Expected 200, got {self.response.status_code}"


    @allure.step("Check status code 404")
    def check_statuscode_is_404(self):
        assert self.response.status_code == 404, f"Expected 404, got {self.response.status_code}"

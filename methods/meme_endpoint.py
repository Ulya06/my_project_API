import allure


class MemeEndpoint:
    url = "http://memesapi.course.qa-practice.com/meme"
    headers = None
    response = None

    @property
    def json(self):
        try:
            return self.response.json()
        except (ValueError, AttributeError):
            return None

    def set_token(self, token):
        self.headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }

    @allure.step("Check status code is 200")
    def check_status_code_200(self):
        assert self.response.status_code == 200, f"Expected status code 200, got {self.response.status_code}"

    @allure.step("Check status code is 400")
    def check_status_code_400(self):
        assert self.response.status_code == 400, f"Expected status code 400, got {self.response.status_code}"

    @allure.step("Check status code is 401")
    def check_status_code_401(self):
        assert self.response.status_code == 401, f"Expected status code 401, got {self.response.status_code}"

    @allure.step("Check status code is 404")
    def check_status_code_404(self):
        assert self.response.status_code == 404, f"Expected status code 404, got {self.response.status_code}"

    @allure.step("Check response status code")
    def check_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, (f"Expected status code {expected_status_code}, "
                                                                   f"got {self.response.status_code}")

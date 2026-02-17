import allure


class MemeEndpoint:


    url = "http://memesapi.course.qa-practice.com/meme"

    headers = None
    response = None


    @property
    def json(self):
        try:
            return self.response.json()
        except Exception:
            return None


    @allure.step("Set token")
    def set_token(self, token):
        self.headers = {
            "Authorization": token,
            "Content-Type": "application/json"
        }


    @allure.step("Check status code")
    def check_status_code(self, expected_status_code):
        assert self.response.status_code == expected_status_code, (
            f"Expected {expected_status_code}, got {self.response.status_code}"
        )


    @allure.step("Check meme equals expected")
    def check_meme_equals(self, expected_data):
        for key in expected_data:
            assert self.json[key] == expected_data[key], (
                f"Expected {key}={expected_data[key]}, got {self.json[key]}"
            )


    @allure.step("Check id exists")
    def check_id_exists(self):
        assert "id" in self.json, "Response has no id"

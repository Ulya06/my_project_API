import allure


from methods.authorize import Authorize


@allure.story("Get token success")
def test_get_token_success():
    auth = Authorize()
    auth.get_token("Uliana")
    auth.check_status_code(200)
    assert "token" in auth.json


@allure.story("Get token empty body")
def test_get_token_empty():
    auth = Authorize()
    auth.get_token("")
    auth.check_status_code(400)


@allure.story("Check valid token")
def test_check_valid_token(auth_token):
    auth = Authorize()
    auth.check_token(auth_token)
    auth.check_status_code(200)


@allure.story("Check invalid token")
def test_check_invalid_token():
    auth = Authorize()
    auth.check_token("invalid")
    auth.check_status_code(404)

import allure


from methods.create_meme import CreateMeme


@allure.story("Create without token")
def test_create_without_token():
    api = CreateMeme()
    api.create_new_meme({
        "text": "test",
        "url": "url",
        "tags": [],
        "info": {}
    })

    api.check_status_code(401)


@allure.story("Create with invalid token")
def test_create_invalid_token():
    api = CreateMeme()
    api.headers = {"Authorization": "invalid"}
    api.create_new_meme({
        "text": "test",
        "url": "url",
        "tags": [],
        "info": {}
    })

    api.check_status_code(401)

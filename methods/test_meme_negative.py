import allure


@allure.feature("Meme API")
@allure.story("Unauthorized access")
def test_get_meme_without_token_returns_401():
    from methods.get_meme import GetMeme

    get_meme = GetMeme()
    get_meme.get_meme(1)
    get_meme.check_status_code_401()


@allure.feature("Meme API")
@allure.story("Get non-existent meme")
def test_get_nonexistent_meme_returns_404(get_meme):
    non_existing_meme_id = 999999

    get_meme.get_meme(non_existing_meme_id)
    get_meme.check_status_code_404()


@allure.feature("Meme API")
@allure.story("Create meme with empty text")
def test_create_meme_with_empty_text_returns_400(create_meme):
    body = {
        "text": "",
        "url": "https://example.com/image.png",
        "tags": ["test"],
        "info": {"color": ["black"]},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


@allure.feature("Meme API")
@allure.story("Create meme with missing required field")
def test_create_meme_without_url_returns_400(create_meme):
    body = {
        "text": "meme without url",
        "tags": ["test"],
        "info": {"color": ["red"]},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


@allure.feature("Meme API")
@allure.story("Delete non-existent meme")
def test_delete_nonexistent_meme_returns_404(delete_meme):
    non_existing_meme_id = 999999

    delete_meme.delete_meme(non_existing_meme_id)
    delete_meme.check_status_code_404()

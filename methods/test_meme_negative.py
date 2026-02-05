import allure
import pytest


@allure.feature("Meme API")
@allure.story("Unauthorized access")
def test_get_meme_without_token_returns_401():
    from methods.get_meme import GetMeme

    get_meme = GetMeme()
    get_meme.get_meme(1)
    get_meme.check_status_code_401()


@pytest.mark.parametrize(
    "body",
    [
        {},
        {"text": ""},
        {"text": 12},
        {"url": 123},
        {"tags": "tags"},
        {"info": "info"},
    ]
)
def test_create_meme_with_invalid_body_returns_400(create_meme, body):
    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


@pytest.mark.parametrize(
    "body",
    [
        {},
        {"text": ""},
        {"text": 123},
        {"tags": "tags"},
    ]
)
def test_update_meme_with_invalid_body_returns_400(created_meme, update_meme, body):
    update_meme.put_meme(body, created_meme["id"])
    update_meme.check_status_code_400()


def test_get_nonexistent_meme_returns_404(get_meme):
    get_meme.get_meme(999999)
    get_meme.check_status_code_404()


def test_delete_nonexistent_meme_returns_404(delete_meme):
    delete_meme.delete_meme(999999)
    delete_meme.check_status_code_404()


def test_update_nonexistent_meme_returns_404(update_meme):
    update_meme.put_meme({"text": "test"}, 999999)
    update_meme.check_status_code_404()


def test_create_meme_without_url_returns_400(create_meme):
    body = {"text": "no url", "tags": [], "info": {}}
    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


def test_create_meme_without_text_returns_400(create_meme):
    body = {"url": "https://example.com/img.png", "tags": [], "info": {}}
    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


def test_create_meme_with_null_body_returns_400(create_meme):
    create_meme.create_new_meme(None)
    create_meme.check_status_code_400()


def test_update_meme_without_token_returns_401(created_meme):
    from methods.put_meme import PutMeme

    update = PutMeme()
    update.put_meme({"text": "test"}, created_meme["id"])
    update.check_status_code_401()


def test_delete_meme_without_token_returns_401(created_meme):
    from methods.delete_meme import DeleteMeme

    delete = DeleteMeme()
    delete.delete_meme(created_meme["id"])
    delete.check_status_code_401()


def test_get_meme_with_invalid_token_returns_401(get_meme):
    get_meme.headers = {"Authorization": "invalid"}
    get_meme.get_meme(1)
    get_meme.check_status_code_401()


def test_create_meme_with_invalid_token_returns_401(create_meme):
    create_meme.headers = {"Authorization": "invalid"}
    create_meme.create_new_meme({"text": "test"})
    create_meme.check_status_code_401()


def test_update_meme_with_empty_body_returns_400(created_meme, update_meme):
    update_meme.put_meme({}, created_meme["id"])
    update_meme.check_status_code_400()


def test_delete_meme_twice_returns_404(created_meme, delete_meme):
    meme_id = created_meme["id"]
    delete_meme.delete_meme(meme_id)
    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code_404()

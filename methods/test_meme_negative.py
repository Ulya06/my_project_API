import pytest
import allure


from methods.get_meme import GetMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme


@allure.feature("Meme API")
@allure.story("Unauthorized access")
def test_get_meme_without_token_returns_401():
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
        None
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
        {"info": "info"},
        None
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


@pytest.mark.parametrize(
    "body",
    [
        {"text": "no url", "tags": [], "info": {}},
        {"url": "https://example.com/img.png", "tags": [], "info": {}}
    ]
)
def test_create_meme_missing_required_fields_returns_400(create_meme, body):
    create_meme.create_new_meme(body)
    create_meme.check_status_code_400()


@pytest.mark.parametrize(
    "endpoint_class, action",
    [
        (PutMeme, "put_meme"),
        (DeleteMeme, "delete_meme")
    ]
)
def test_actions_without_token_return_401(created_meme, endpoint_class, action):
    instance = endpoint_class()
    getattr(instance, action)({"text": "test"} if action == "put_meme" else created_meme["id"])
    instance.check_status_code_401()


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

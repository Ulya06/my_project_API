import pytest
import allure


from methods.authorize import Authorize
from methods.create_meme import CreateMeme
from methods.get_meme import GetMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme


@allure.feature("Meme API")
@allure.story("Check token is alive")
def test_check_token_alive(auth_token):
    auth = Authorize()
    response = auth.check_token(auth_token)
    assert response.status_code == 200


@allure.feature("Meme API")
@allure.story("Create meme with different bodies")
@pytest.mark.parametrize(
    "body",
    [
        {"text": "hello", "url": "https://example.com/img.png", "tags": ["tag"], "info": {}},
        {"text": "", "url": "https://example.com/img.png", "tags": [], "info": {}},
        {"text": "123", "url": "https://example.com/img.png", "tags": ["a", "b"], "info": {"color": ["red"]}},
        {"text": "long text " * 20, "url": "https://example.com/img.png", "tags": ["tag"], "info": {}},
    ]
)
def test_create_meme_variants(create_meme, delete_meme, body):
    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])
    delete_meme.check_status_code_200()


@allure.feature("Meme API")
@allure.story("Get meme functionality")
def test_get_created_meme(created_meme, get_meme):
    get_meme.get_meme(created_meme["id"])
    get_meme.check_status_code_200()


@allure.feature("Meme API")
@allure.story("Update meme fields separately")
@pytest.mark.parametrize(
    "update_body",
    [
        {"text": "updated text"},
        {"url": "https://example.com/new.png"},
        {"tags": ["newtag"]},
        {"info": {"size": "big"}},
    ]
)
def test_update_meme_fields(created_meme, update_meme, get_meme, update_body):
    meme_id = created_meme["id"]
    update_meme.put_meme(update_body, meme_id)
    update_meme.check_status_code_200()
    get_meme.get_meme(meme_id)
    get_meme.check_status_code_200()


@allure.feature("Meme API")
@allure.story("Delete meme")
def test_delete_meme(created_meme, delete_meme, get_meme):
    meme_id = created_meme["id"]
    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code_200()
    get_meme.get_meme(meme_id)
    get_meme.check_status_code_404()


@allure.feature("Meme API")
@allure.story("Negative tests for invalid data")
@pytest.mark.parametrize(
    "invalid_body",
    [
        {"text": 123, "url": "https://example.com/img.png", "tags": ["tag"], "info": {}},
        {"text": "test", "url": "", "tags": ["tag"], "info": {}},
        {"text": "test", "url": "https://example.com/img.png", "tags": "notlist", "info": {}},
        {"text": "test", "url": "https://example.com/img.png", "tags": ["tag"], "info": "notdict"},
        {},
    ]
)
def test_create_meme_invalid_data(create_meme, invalid_body):
    create_meme.create_new_meme(invalid_body)
    create_meme.check_status_code_400()

import pytest
import allure


from methods.create_meme import CreateMeme
from methods.get_meme import GetMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme
from methods.authorize import Authorize


@pytest.fixture(scope="session")
def auth_token():
    return "DPXa1JzfzT7CXz2"

@pytest.fixture
def meme_headers(auth_token):
    obj = CreateMeme()
    obj.set_token(auth_token)
    return obj


@allure.feature("Meme API")
@allure.story("Check token is alive")
def test_check_token_alive(auth_token):
    auth = Authorize()
    response = auth.check_token(auth_token)
    assert response.status_code == 200
    print(f"Token {auth_token} is alive and valid")


@allure.feature("Meme API")
@allure.story("Create and delete meme")
def test_create_and_delete_meme(meme_headers):
    body = {
        "text": "real life",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["cat", "gape", "tongue"],
        "info": {"color": ["white", "grey"]}
    }
    meme_headers.create_new_meme(body)
    meme_headers.check_statuscode_is_200()
    meme_id = meme_headers.json["id"]

    DeleteMeme().delete_meme(meme_id)
    print(f"Meme with id {meme_id} created and deleted successfully")


@allure.feature("Meme API")
@allure.story("Get meme by ID")
def test_get_meme(meme_headers):
    meme_id = 5847
    get_meme = GetMeme()
    get_meme.set_token(meme_headers.headers["Authorization"])
    get_meme.get_meme(meme_id)
    get_meme.check_statuscode_is_200()
    assert get_meme.json["id"] == meme_id
    assert get_meme.json["text"] == "real life"


@allure.feature("Meme API")
@allure.story("Update meme with PUT")
def test_put_meme(meme_headers):
    meme_id = 5847
    body = {
        "id": meme_id,
        "text": "updated text",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["cat", "fun"],
        "info": {"color": ["black"]}
    }
    put_meme = PutMeme()
    put_meme.set_token(meme_headers.headers["Authorization"])
    put_meme.put_meme(body, meme_id)
    put_meme.check_statuscode_is_200()
    assert put_meme.json["text"] == "updated text"


@allure.feature("Meme API")
@allure.story("Delete meme")
def test_delete_meme(meme_headers):
    body = {
        "text": "temporary meme",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["temp"],
        "info": {"color": ["yellow"]}
    }
    meme_headers.create_new_meme(body)
    meme_id = meme_headers.json["id"]

    delete_meme = DeleteMeme()
    delete_meme.set_token(meme_headers.headers["Authorization"])
    delete_meme.delete_meme(meme_id)
    delete_meme.check_statuscode_is_200()

    get_meme = GetMeme()
    get_meme.set_token(meme_headers.headers["Authorization"])
    get_meme.get_meme(meme_id)
    get_meme.check_statuscode_is_404()

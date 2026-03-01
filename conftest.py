import pytest


from methods.authorize import Authorize
from methods.create_meme import CreateMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme
from methods.get_meme import GetMeme


@pytest.fixture(scope="session")
def auth_token():
    auth = Authorize()
    auth.get_token("Uliana")
    auth.check_status_code(200)
    return auth.json["token"]


@pytest.fixture()
def create_meme(auth_token):
    api = CreateMeme()
    api.set_token(auth_token)
    return api


@pytest.fixture()
def update_meme(auth_token):
    api = PutMeme()
    api.set_token(auth_token)
    return api


@pytest.fixture()
def delete_meme(auth_token):
    api = DeleteMeme()
    api.set_token(auth_token)
    return api


@pytest.fixture()
def get_meme(auth_token):
    api = GetMeme()
    api.set_token(auth_token)
    return api


@pytest.fixture()
def created_meme(create_meme, delete_meme):
    body = {
        "text": "Test meme",
        "url": "https://example.com/image.png",
        "tags": ["test"],
        "info": {"color": "red"}
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code(200)
    create_meme.check_id_exists()
    meme = create_meme.json
    yield meme

    delete_meme.delete_meme(meme["id"])

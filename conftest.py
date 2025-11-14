import pytest


from methods.create_meme import CreateMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme
from methods.get_meme import GetMeme


@pytest.fixture()
def create_new_meme_up():
    return CreateMeme()


@pytest.fixture()
def test_meme(create_new_meme_up):
    body = {
        "text": "Test meme",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["test", "meme"],
        "info": {"color": ["red", "blue"]}
    }
    create_new_meme_up.create_new_meme(body)
    meme_id = create_new_meme_up.json["id"]
    yield create_new_meme_up.json
    DeleteMeme().delete_meme(meme_id)


@pytest.fixture()
def updated_meme_up():
    return PutMeme()


@pytest.fixture()
def delete_meme_up():
    return DeleteMeme()


@pytest.fixture()
def get_meme_up():
    return GetMeme()

import pytest


from methods.create_meme import CreateMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme
from methods.get_meme import GetMeme


@pytest.fixture()
def create_meme():
    return CreateMeme()


@pytest.fixture()
def update_meme():
    return PutMeme()


@pytest.fixture()
def delete_meme():
    return DeleteMeme()


@pytest.fixture()
def get_meme():
    return GetMeme()


@pytest.fixture()
def created_meme(create_meme, delete_meme):
    body = {
        "text": "Test meme",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["test", "meme"],
        "info": {"color": ["red", "blue"]},
    }

    create_meme.create_new_meme(body)
    meme_id = create_meme.json["id"]

    yield create_meme.json

    delete_meme.delete_meme(meme_id)

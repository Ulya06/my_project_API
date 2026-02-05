import allure
import pytest


@allure.feature("Meme API")
@allure.story("Check token is alive")
def test_check_token_alive(auth_token):
    from methods.authorize import Authorize

    auth = Authorize()
    response = auth.check_token(auth_token)
    assert response.status_code == 200


@allure.feature("Meme API")
@allure.story("Create meme saves correct data")
def test_create_meme_saves_correct_data(create_meme, get_meme, delete_meme):
    body = {
        "text": "life",
        "url": "https://example.com/img.png",
        "tags": ["cat"],
        "info": {"color": ["black"]},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    meme_id = create_meme.json["id"]

    get_meme.get_meme(meme_id)
    get_meme.check_status_code_200()

    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code_200()


@pytest.mark.parametrize(
    "text",
    ["a", "test", "123", "long text for meme"]
)
def test_create_meme_with_different_text_values(create_meme, delete_meme, text):
    body = {
        "text": text,
        "url": "https://example.com/img.png",
        "tags": ["tag"],
        "info": {},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])


@pytest.mark.parametrize(
    "tags",
    [["a"], ["one", "two"], []]
)
def test_create_meme_with_different_tags(create_meme, delete_meme, tags):
    body = {
        "text": "tags test",
        "url": "https://example.com/img.png",
        "tags": tags,
        "info": {},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])


def test_get_created_meme(created_meme, get_meme):
    get_meme.get_meme(created_meme["id"])
    get_meme.check_status_code_200()


def test_update_meme_text_only(created_meme, update_meme, get_meme):
    meme_id = created_meme["id"]
    body = {"text": "updated"}

    update_meme.put_meme(body, meme_id)
    update_meme.check_status_code_200()

    get_meme.get_meme(meme_id)
    get_meme.check_status_code_200()


def test_update_meme_url_only(created_meme, update_meme):
    body = {"url": "https://example.com/new.png"}
    update_meme.put_meme(body, created_meme["id"])
    update_meme.check_status_code_200()


def test_update_meme_tags_only(created_meme, update_meme):
    body = {"tags": ["new"]}
    update_meme.put_meme(body, created_meme["id"])
    update_meme.check_status_code_200()


def test_update_meme_info_only(created_meme, update_meme):
    body = {"info": {"size": "big"}}
    update_meme.put_meme(body, created_meme["id"])
    update_meme.check_status_code_200()


def test_delete_meme(created_meme, delete_meme):
    delete_meme.delete_meme(created_meme["id"])
    delete_meme.check_status_code_200()


def test_deleted_meme_not_available(created_meme, delete_meme, get_meme):
    meme_id = created_meme["id"]
    delete_meme.delete_meme(meme_id)
    get_meme.get_meme(meme_id)
    get_meme.check_status_code_404()


def test_multiple_memes_creation(create_meme, delete_meme):
    ids = []
    for i in range(3):
        create_meme.create_new_meme({
            "text": f"meme {i}",
            "url": "https://example.com/img.png",
            "tags": ["tag"],
            "info": {},
        })
        ids.append(create_meme.json["id"])

    for meme_id in ids:
        delete_meme.delete_meme(meme_id)
        delete_meme.check_status_code_200()


def test_get_meme_twice(created_meme, get_meme):
    get_meme.get_meme(created_meme["id"])
    get_meme.check_status_code_200()
    get_meme.get_meme(created_meme["id"])
    get_meme.check_status_code_200()


def test_update_meme_twice(created_meme, update_meme):
    update_meme.put_meme({"text": "1"}, created_meme["id"])
    update_meme.check_status_code_200()
    update_meme.put_meme({"text": "2"}, created_meme["id"])
    update_meme.check_status_code_200()


def test_create_and_delete_immediately(create_meme, delete_meme):
    create_meme.create_new_meme({
        "text": "temp",
        "url": "https://example.com/img.png",
        "tags": [],
        "info": {},
    })
    delete_meme.delete_meme(create_meme.json["id"])
    delete_meme.check_status_code_200()


def test_create_meme_with_empty_tags(create_meme, delete_meme):
    body = {
        "text": "empty tags",
        "url": "https://example.com/img.png",
        "tags": [],
        "info": {},
    }
    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])


def test_create_meme_with_empty_info(create_meme, delete_meme):
    body = {
        "text": "empty info",
        "url": "https://example.com/img.png",
        "tags": ["tag"],
        "info": {},
    }
    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])


def test_create_meme_with_long_text(create_meme, delete_meme):
    body = {
        "text": "a" * 200,
        "url": "https://example.com/img.png",
        "tags": ["tag"],
        "info": {},
    }
    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    delete_meme.delete_meme(create_meme.json["id"])

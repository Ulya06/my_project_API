import pytest
import allure


@allure.story("Create meme invalid types")
@pytest.mark.parametrize("body", [
    {"text": 123, "url": "url", "tags": [], "info": {}},
    {"text": "text", "url": 123, "tags": [], "info": {}},
    {"text": "text", "url": "url", "tags": "wrong", "info": {}},
    {"text": "text", "url": "url", "tags": [], "info": "wrong"},
])
def test_create_invalid_types(create_meme, body):
    create_meme.create_new_meme(body)
    create_meme.check_status_code(400)


@allure.story("Create meme missing fields")
@pytest.mark.parametrize("body", [
    {"url": "url", "tags": [], "info": {}},
    {"text": "text", "tags": [], "info": {}},
    {"text": "text", "url": "url", "info": {}},
    {"text": "text", "url": "url", "tags": []},
])
def test_create_missing_fields(create_meme, body):
    create_meme.create_new_meme(body)
    create_meme.check_status_code(400)


@allure.story("Create meme empty body")
def test_create_empty_body(create_meme):
    create_meme.create_new_meme({})
    create_meme.check_status_code(400)


@allure.story("Get nonexistent meme")
def test_get_nonexistent(get_meme):
    get_meme.get_meme(999999)
    get_meme.check_status_code(404)


@allure.story("Delete nonexistent meme")
def test_delete_nonexistent(delete_meme):
    delete_meme.delete_meme(999999)
    delete_meme.check_status_code(404)


@allure.story("Update nonexistent meme")
def test_update_nonexistent(update_meme):
    body = {
        "text": "test",
        "url": "url",
        "tags": [],
        "info": {}
    }

    update_meme.put_meme(body, 999999)
    update_meme.check_status_code(404)


@allure.story("Update invalid types")
@pytest.mark.parametrize("body", [
    {"text": 123, "url": "url", "tags": [], "info": {}},
    {"text": "text", "url": 123, "tags": [], "info": {}},
])
def test_update_invalid_types(created_meme, update_meme, body):
    update_meme.put_meme(body, created_meme["id"])
    update_meme.check_status_code(400)

import allure


@allure.story("Create meme")
def test_create_meme(create_meme, delete_meme):
    body = {
        "text": "hello",
        "url": "https://example.com/img.png",
        "tags": ["fun"],
        "info": {"size": "large"}
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code(200)
    create_meme.check_id_exists()
    create_meme.check_meme_equals(body)
    delete_meme.delete_meme(create_meme.json["id"])


@allure.story("Get meme")
def test_get_meme(created_meme, get_meme):
    get_meme.get_meme(created_meme["id"])
    get_meme.check_status_code(200)
    get_meme.check_meme_equals(created_meme)


@allure.story("Update meme")
def test_update_meme(created_meme, update_meme, get_meme):
    meme_id = created_meme["id"]
    new_body = {
        "text": "updated",
        "url": created_meme["url"],
        "tags": created_meme["tags"],
        "info": created_meme["info"]
    }

    update_meme.put_meme(new_body, meme_id)
    update_meme.check_status_code(200)
    get_meme.get_meme(meme_id)
    get_meme.check_meme_equals(new_body)


@allure.story("Delete meme")
def test_delete_meme(created_meme, delete_meme, get_meme):
    meme_id = created_meme["id"]
    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code(200)
    get_meme.get_meme(meme_id)
    get_meme.check_status_code(404)

import allure


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
        "text": "real life",
        "url": "https://www.care.com/c/wp-content/uploads/sites/2/2021/04/maressab-202115020615567399.jpg",
        "tags": ["cat", "gape", "tongue"],
        "info": {"color": ["white", "grey"]},
    }

    create_meme.create_new_meme(body)
    create_meme.check_status_code_200()
    meme_id = create_meme.json["id"]

    get_meme.get_meme(meme_id)
    get_meme.check_status_code_200()


    assert get_meme.json["text"] == body["text"]
    assert get_meme.json["url"] == body["url"]
    assert get_meme.json["tags"] == body["tags"]
    assert get_meme.json["info"] == body["info"]


    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code_200()


@allure.feature("Meme API")
@allure.story("Update meme updates all fields")
def test_update_meme_updates_all_fields(created_meme, update_meme, get_meme):
    meme_id = created_meme["id"]

    updated_body = {
        "id": meme_id,
        "text": "updated text",
        "url": "https://example.com/new.png",
        "tags": ["updated", "fun"],
        "info": {"color": ["black"]},
    }

    update_meme.put_meme(updated_body, meme_id)
    update_meme.check_status_code_200()

    get_meme.get_meme(meme_id)
    get_meme.check_status_code_200()


    assert get_meme.json["text"] == updated_body["text"]
    assert get_meme.json["url"] == updated_body["url"]
    assert get_meme.json["tags"] == updated_body["tags"]
    assert get_meme.json["info"] == updated_body["info"]


@allure.feature("Meme API")
@allure.story("Delete meme removes meme from system")
def test_delete_meme_removes_meme(created_meme, delete_meme, get_meme):
    meme_id = created_meme["id"]

    delete_meme.delete_meme(meme_id)
    delete_meme.check_status_code_200()

    get_meme.get_meme(meme_id)
    get_meme.check_status_code_404()

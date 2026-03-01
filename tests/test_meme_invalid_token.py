import allure
import pytest


from methods.create_meme import CreateMeme
from methods.get_meme import GetMeme
from methods.put_meme import PutMeme
from methods.delete_meme import DeleteMeme


@allure.story("Operations with invalid token")
@pytest.mark.parametrize("endpoint_class, method_name, body_or_id",
    [
        (CreateMeme, "create_new_meme", {"text": "test", "url": "url", "tags": [], "info": {}}),
        (GetMeme, "get_meme", 1),
        (PutMeme, "put_meme", ({"text": "updated", "url": "url", "tags": [], "info": {}}, 1)),
        (DeleteMeme, "delete_meme", 1),
    ]
)
def test_operations_with_invalid_token(endpoint_class, method_name, body_or_id):
    instance = endpoint_class()
    instance.headers = {"Authorization": "invalid"}


    if isinstance(body_or_id, tuple):
        getattr(instance, method_name)(*body_or_id)
    else:
        getattr(instance, method_name)(body_or_id)

    instance.check_status_code(401)

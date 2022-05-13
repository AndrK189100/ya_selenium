import pytest
from main import user_name as un, user_password as up
from main import yandex_authorization

def test_yandex_authorization():

    result = yandex_authorization(un, up)
    title = result.title
    result.quit()
    assert  title == 'Яндекс ID'



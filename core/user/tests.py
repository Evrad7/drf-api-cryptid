import pytest
from .models import User



@pytest.mark.django_db
def test_create_user(user_data):
    user=User.objects.create_user(**user_data)
    assert user.username==user_data["username"]
    assert user.email==user_data["email"]
    assert user.first_name==user_data["first_name"]
    assert user.last_name==user_data["last_name"]


@pytest.mark.django_db
def test_create_super_user(user_data):
    user=User.objects.create_superuser(**user_data)
    assert user.username==user_data["username"]
    assert user.email==user_data["email"]
    assert user.first_name==user_data["first_name"]
    assert user.last_name==user_data["last_name"]
    assert user.is_superuser
    assert user.is_staff


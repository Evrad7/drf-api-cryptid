import pytest
from rest_framework.test import APIClient

from .comment.models import Comment

from .post.models import Post

from .user.models import User

@pytest.fixture()
def client():
    return APIClient()

@pytest.fixture(scope="function")
def user_data():
    return {
        "username":"User test 0",
        "email":"usertest@gmail.com",
        "password":"dfsdfsdfsdfq454564",
        "first_name":"First name user",
        "last_name":"Last name user",
        
    }


@pytest.fixture()
def simple_user(user_data):
    return User.objects.create_user(**user_data)

@pytest.fixture
def post(simple_user):
    return Post.objects.create(author=simple_user, body="Post fixture")


@pytest.fixture
def comment(simple_user, post):
    return Comment.objects.create(author=simple_user, post=post, body="Simple comment")
import pytest

from core.post.models import Post


@pytest.mark.django_db
def test_create_post(simple_user):
    data={
        "author":simple_user,
        "body":"Body post"
    }
    post=Post.objects.create(**data)
    assert post.author==data["author"]
    assert post.body==data["body"]
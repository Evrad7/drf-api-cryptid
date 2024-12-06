import pytest

from core.comment.models import Comment


@pytest.mark.django_db
def test_create_comment(post, simple_user):
    data={
        "author":simple_user,
        "post":post,
        "body":"Comment 1",
    }
    comment=Comment.objects.create(**data)
    assert comment.author==data["author"]
    assert comment.post==data["post"]
    assert comment.body==data["body"]

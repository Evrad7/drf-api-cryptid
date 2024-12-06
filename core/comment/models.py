from django.db import models

from ..abstract.models import AbstractManager, AbstractModel


class CommentManger(AbstractManager):
    pass

class Comment(AbstractModel):
    author=models.ForeignKey(to="core_user.User", on_delete=models.PROTECT)
    post=models.ForeignKey(to="core_post.Post", on_delete=models.CASCADE)
    body=models.TextField()
    edited=models.BooleanField(default=False)

    objects=CommentManger()

    def __str__(self) -> str:
        return self.author.name

import pytest
from rest_framework import status
from rest_framework.test import APIClient


class TestCommentViewSet:
    endpoint="/post/"

    @pytest.mark.django_db
    def test_list(self, client, simple_user, post, comment):
        client.force_authenticate(simple_user)
        response=client.get(self.endpoint+str(post.public_id)+"/comment/")
        assert response.status_code==status.HTTP_200_OK
        assert response.data["count"]==1
    
    @pytest.mark.django_db
    def test_retrieve(self, client, simple_user, post, comment):
        client.force_authenticate(simple_user)
        response=client.get(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/")
        assert response.status_code==status.HTTP_200_OK
        assert response.data["id"]==comment.public_id.hex
        assert response.data["body"]==comment.body


    @pytest.mark.django_db
    def test_create(self, client, simple_user, post):
        client.force_authenticate(simple_user)
        data={
            "author_id":simple_user.public_id.hex,
            "post":post.public_id.hex,
            "body":"Comment post",
        }
        response=client.post(self.endpoint+str(post.public_id)+"/comment/", data)
        assert response.status_code==status.HTTP_201_CREATED
        assert response.data["body"]==data["body"]


    @pytest.mark.django_db
    def test_update(self, client, simple_user, post, comment):
        client.force_authenticate(simple_user)
        data={
            "author_id":simple_user.public_id.hex,
            "post":post.public_id.hex,
            "body":"Comment post updated",
        }
        response=client.put(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/", data)
        assert response.status_code==status.HTTP_200_OK
        assert response.data["body"]==data["body"]

    
    @pytest.mark.django_db
    def test_destroy(self, client, simple_user, post, comment):
        client.force_authenticate(simple_user)
        response=client.delete(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/")
        assert response.status_code==status.HTTP_204_NO_CONTENT



    @pytest.mark.django_db
    def test_list_anonymous(self, client, post, comment):
        response=client.get(self.endpoint+str(post.public_id)+"/comment/")
        assert response.status_code==status.HTTP_200_OK
        assert response.data["count"]==1
    
    @pytest.mark.django_db
    def test_retrieve_anonymous(self, client, post, comment):
        response=client.get(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/")
        assert response.status_code==status.HTTP_200_OK
        assert response.data["id"]==comment.public_id.hex
        assert response.data["body"]==comment.body


    @pytest.mark.django_db
    def test_create_anonymous(self, client, simple_user, post):
        data={
            "author_id":simple_user.public_id.hex,
            "post":post.public_id.hex,
            "body":"Comment post",
        }
        response=client.post(self.endpoint+str(post.public_id)+"/comment/", data)
        assert response.status_code==status.HTTP_401_UNAUTHORIZED


    @pytest.mark.django_db
    def test_update_anonymous(self, client, simple_user, post, comment):
        data={
            "author_id":simple_user.public_id.hex,
            "post":post.public_id.hex,
            "body":"Comment post updated",
        }
        response=client.put(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/", data)
        assert response.status_code==status.HTTP_401_UNAUTHORIZED

    
    # @pytest.mark.django_db
    # def test_destroy(self, client: APIClient, post, comment):
    #     response=client.delete(self.endpoint+str(post.public_id)+"/comment/"+str(comment.public_id)+"/")
    #     assert response.status_code==status.HTTP_401_UNAUTHORIZED


        
        
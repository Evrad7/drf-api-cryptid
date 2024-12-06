
from urllib import response
import pytest
from rest_framework import status

class TestAuthenticationViewSet:
    endpoint="/auth/"

    @pytest.mark.django_db
    def test_login(self, client, simple_user, user_data):
        data={
            "email":simple_user.email,
            "password":user_data["password"],   
        }
        response=client.post(self.endpoint+"login/", data)
        assert response.status_code==status.HTTP_200_OK
        assert response.data["access"]
        assert response.data["user"]["username"]==simple_user.username
        assert response.data["user"]["email"]==simple_user.email
        assert response.data["user"]["id"]==simple_user.public_id.hex


    @pytest.mark.django_db
    def test_register(self, client):
        data={
            "username":"User test 7",
            "first_name":"First name user test 7",
            "last_name":"Last name user test 7",
            "email":"userbig@gmail.com",
            "password":"dfsdfsJHJ5564",

        }
        response=client.post(self.endpoint+"register/", data)
        assert response.status_code==status.HTTP_201_CREATED
        assert response.data["access"]
        assert response.data["refresh"]
        assert response.data["user"]["username"]==data["username"]
        assert response.data["user"]["email"]==data["email"]

    @pytest.mark.django_db
    def test_refresh(self, client, simple_user, user_data):
        data = {
            "email": simple_user.email,
            "password": user_data["password"]
        }
        response = client.post(self.endpoint + "login/",data)
        assert response.status_code == status.HTTP_200_OK
        data_refresh = {"refresh":  response.data['refresh']}
        response = client.post(self.endpoint + "refresh/",
                              data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['access']
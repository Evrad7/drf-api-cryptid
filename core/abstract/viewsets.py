
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class AbstractViewSet(viewsets.ModelViewSet):
    filter_backends=[filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields=["updated", "created"]
    ordering=["-updated"]



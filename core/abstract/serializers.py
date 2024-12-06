
from rest_framework import serializers

class AbstractSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(source="public_id", format="hex", read_only=True)


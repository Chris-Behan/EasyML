from rest_framework import serializers


class FileSerializer(serializers.Serializer):

    features = serializers.CharField(max_length=500)
    label = serializers.CharField(max_length=200)

    def create(self, validated_data):

        return "received file info"

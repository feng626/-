from rest_framework import serializers


class ModelSerializer(serializers.ModelSerializer):

    def pre_create(self, validated_data):
        username = self._get_user_name()
        validated_data['update_by'] = username
        validated_data['create_by'] = username

    def pre_update(self, instance, validated_data):
        username = self._get_user_name()
        validated_data['update_by'] = username

    def create(self, validated_data):
        self.pre_create(validated_data)
        return super(ModelSerializer, self).create(validated_data)

    def _get_user_name(self):
        user = self.context['request'].user
        username = None
        if user.is_anonymous:
            username = 'anonymous'
        else:
            username = user.username
        return username

    def update(self, instance, validated_data):
        self.pre_update(instance, validated_data)
        return super(ModelSerializer, self).update(instance, validated_data)

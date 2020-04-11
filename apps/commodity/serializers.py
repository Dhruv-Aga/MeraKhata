from rest_framework import serializers
from commodity.models import Item
from django.contrib.auth.models import User



class ItemPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return 'Item: %d: %s' % (instance.id, instance.name)


class ItemSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Item.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    def to_representation(self, instance):
        response = super().to_representation(instance)
        if instance.owner is not None:
            print(instance.owner)
            response['owner'] = UserSerializer(instance.owner).data
        return response

    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # items = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username']
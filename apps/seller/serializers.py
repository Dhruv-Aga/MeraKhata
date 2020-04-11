from rest_framework import serializers
from seller.models import Seller
from commodity.models import Item
from commodity.serializers import ItemPrimaryKeyRelatedField, ItemSerializer
from django.contrib.auth.models import User



class SellerSerializer(serializers.ModelSerializer):
    
    def update(self, instance, validated_data):
        items = set([item.id for item in validated_data.pop('items')])
        instance.items.set(items)
        connections = set([connection.id for connection in validated_data.pop('connections')])
        instance.connections.set(connections)
        instance.save()
        return instance

    def create(self, validated_data):
        items = set([item.id for item in validated_data.pop('items')])
        connections = set([connection.id for connection in validated_data.pop('connections')])
        instance = Seller.objects.create(**validated_data)
        instance.items.set(items)
        instance.connections.set(connections)
        return instance

    def retrieve(self, instance):
        response = super().to_representation(instance)
        details = instance.items.all()
        response['items'] = []
        if details is not None:
            response['items'] = list([ItemSerializer(x).id for x in details])
        details = instance.connections.all()
        response['connections'] = []
        if details is not None:
            response['connections'] = list([SellerSerializer(x).data for x in details])
        return response

    def to_representation(self, instance):
        response = super().to_representation(instance)
        details = instance.items.all()
        response['items'] = []
        if details is not None:
            response['items'] = list([ItemSerializer(x).data for x in details])
        details = instance.connections.all()
        response['connections'] = []
        if details is not None:
            response['connections'] = list([SellerSerializer(x).data for x in details])
        
        return response

    class Meta:
        model = Seller
        fields = '__all__'
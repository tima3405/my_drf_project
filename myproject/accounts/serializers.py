from rest_framework import serializers
from .models import Car, Comments, User


class CommentsListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comments
        fields = ('id', 'comment', 'user')
        read_only_fields = ['user', ]


class CarSerializer(serializers.ModelSerializer):
    car_comment = CommentsListSerializer(many=True, read_only=True)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Car
        fields = ['id', 'vin', 'color', 'brand', 'car_type', 'user', 'car_comment', ]


class CarsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'vin', 'user', 'comment',)


class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

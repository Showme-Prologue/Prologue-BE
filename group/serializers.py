from rest_framework import serializers

from .models import Group, GroupUserList

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class GroupUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupUserList
        fields = '__all__'

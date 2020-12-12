from rest_framework import serializers
from .models import Member, Principle

class MemberSerializer(serializers.ModelSerializer):
    # feeling = serializers.ReadOnlyField(
    #     source='principle.username',
    #     read_only=True
    # )

    class Meta: 
        model = Member
        fields = ('id', 'username', 'name', 'department', 'team')

class PrincipleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Principle
        fields = ('id', 'username', 'feeling', 'date')
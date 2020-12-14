from rest_framework import serializers
from .models import Member, Principle
from users.serializers import UserSerializer

class MemberSerializer(serializers.ModelSerializer):
    # feeling = serializers.ReadOnlyField(
    #     source='Principle.username',
    #     read_only=True
    # )

    class Meta: 
        model = Member
        fields = ('id', 'user_pk', 'name', 'department', 'team')

class PrincipleSerializer(serializers.ModelSerializer):
    user = UserSerializer(
        many=True,
        read_only=True,
        source='auth.User'
    )
    class Meta: 
        model = Principle
        fields = ('id', 'user', 'username', 'date', 'questionnaire_type', 'question_one', 'question_two', 'question_three', 'question_four', 'question_five', 'question_six', 'question_seven')

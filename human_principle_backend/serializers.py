from rest_framework import serializers
from .models import Member, Principle

class MemberSerializer(serializers.ModelSerializer):
    # feeling = serializers.ReadOnlyField(
    #     source='principle.username',
    #     read_only=True
    # )

    class Meta: 
        model = Member
        fields = ('id', 'user_pk', 'name', 'department', 'team')

class PrincipleSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Principle
        fields = ('id', 'name', 'date', 'questionnaire_type', 'question_one', 'question_two', 'question_three', 'question_four', 'question_five', 'question_six', 'question_seven')

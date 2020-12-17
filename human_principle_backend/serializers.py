from rest_framework import serializers
from .models import Principle
from users.models import User

class PrincipleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(
        source='user.email',
        read_only=True
    )
    class Meta:
        model = Principle
        fields = ('id', 'user', 'date', 'questionnaire_type', 'question_one', 'question_two', 'question_three', 'question_four', 'question_five', 'question_six', 'question_seven')

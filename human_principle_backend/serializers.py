from rest_framework import serializers
from .models import Principle
from users.models import User

class PrincipleSerializer(serializers.ModelSerializer):
    email = serializers.SlugRelatedField(
        slug_field='email',
        queryset=User.objects.all()
    )
    class Meta: 
        model = Principle
        fields = ('id', 'email', 'date', 'questionnaire_type', 'question_one', 'question_two', 'question_three', 'question_four', 'question_five', 'question_six', 'question_seven')


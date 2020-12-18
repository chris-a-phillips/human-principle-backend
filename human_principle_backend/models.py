from django.db import models
from users.models import User

# Create your models here.
# app name then model class name

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='goals', blank=False)
    set_date = models.DateField(auto_now=True)
    due_date = models.DateField(auto_now=False, auto_now_add=False)
    title = models.CharField(max_length = 255, blank=False)
    description = models.CharField(max_length = 255, blank=False)
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    PRIORITY_OPTIONS = [
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    ]
    priority_level = models.CharField(
        max_length=10,
        choices=PRIORITY_OPTIONS,
        default=LOW,
    )

class Principle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='principles', blank=False)
    date = models.DateField(auto_now=True)

    MENTAL = 'Mental'
    PHYSICAL = 'Physical'
    EMOTIONAL = 'Emotional'
    QUESTIONNAIRE_TYPE = [
        (MENTAL, 'Mental'),
        (PHYSICAL, 'Physical'),
        (EMOTIONAL, 'Emotional'),
    ]
    questionnaire_type = models.CharField(
        max_length=10,
        choices=QUESTIONNAIRE_TYPE,
        default=MENTAL,
    )

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    RESPONSE_CHOICES = [
        (ONE, 1),
        (TWO, 2),
        (THREE, 3),
        (FOUR, 4),
        (FIVE, 5),
        (SIX, 6),
        (SEVEN, 7),
        (EIGHT, 8),
        (NINE, 9),
        (TEN, 10),
    ]
    question_one = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=0,
    )
    question_two = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )
    question_three = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )
    question_four = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )
    question_five = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )
    question_six = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )
    question_seven = models.CharField(
        max_length=2,
        choices=RESPONSE_CHOICES,
        default=ONE,
    )

    def __str__(self):
        return self.email
from django.db import models

# Create your models here.
# app name then model class name
class Member(models.Model):
    user_pk = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='member', blank=False)
    name = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Principle(models.Model):
    username = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='principle', blank=False)
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

    STRONGLY_DISAGREE = '1'
    DISAGREE = '2'
    SLIGHTLY_DISAGREE = '3'
    SLIGHTLY_AGREE = '4'
    AGREE = '5'
    STRONGLY_AGREE = '6'
    RESPONSE_CHOICES = [
        (STRONGLY_DISAGREE, '1'),
        (DISAGREE, '2'),
        (SLIGHTLY_DISAGREE, '3'),
        (SLIGHTLY_AGREE, '4'),
        (AGREE, '5'),
        (STRONGLY_AGREE, '6'),
    ]
    question_one = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_two = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_three = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_four = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_five = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_six = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )
    question_seven = models.CharField(
        max_length=1,
        choices=RESPONSE_CHOICES,
        default=SLIGHTLY_AGREE,
    )

    def __str__(self):
        return self.username
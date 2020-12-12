from django.db import models

# Create your models here.

class Member(models.Model):
    username = models.ForeignKey('users.user', on_delete=models.CASCADE, related_name='member', blank=False)
    name = models.CharField(max_length=100, blank=False)
    department = models.CharField(max_length=100, blank=False)
    team = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name

class Principle(models.Model):
    username = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='principle', blank=False)
    date = models.DateField(auto_now=True)
    HAPPY = 'H'
    SAD = 'S'
    MAD = 'M'
    CHILL = 'C'
    DONT_KNOW = 'SF'
    EMOTION_CHOICES = [
        (HAPPY, 'Happy'),
        (SAD, 'Sad'),
        (MAD, 'Mad'),
        (CHILL, 'Chill'),
        (DONT_KNOW, 'Don\'t Know'),
    ]
    feeling = models.CharField(
        max_length=2,
        choices=EMOTION_CHOICES,
        default=CHILL,
    )

    def __str__(self):
        return self.feeling
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.
    optionOne = models.
    optionTwo = models.
    optionThree = models.

class gameStats(models.Model):
    user = models.ForeignKey(User,)
    score = models.

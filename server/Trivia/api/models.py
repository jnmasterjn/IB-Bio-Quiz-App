from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length=30)
    optionOne = models.CharField(max_length=30)
    optionTwo = models.CharField(max_length=30)
    optionThree = models.CharField(max_length=30)
    
    def __str__(self):
        return self.question

class gameStats(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    score = models.IntegerField()

def __str__(self):
        return self
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    optionOne = models.CharField(max_length=300)
    optionTwo = models.CharField(max_length=300)
    optionThree = models.CharField(max_length=300)

    def __str__(self):
        return f"Question: {self.question} | Options: {self.optionOne}, {self.optionTwo}, {self.optionThree}"

class GameStats(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return f"Username: {self.user.username} | Score: {self.score}"
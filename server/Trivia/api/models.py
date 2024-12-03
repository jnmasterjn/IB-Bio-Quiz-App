from django.db import models
from django.contrib.auth.models import User #import built-in User model

#model for quiz questions and answers
class Quiz(models.Model): 
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=300)
    optionOne = models.CharField(max_length=300)
    optionTwo = models.CharField(max_length=300)
    optionThree = models.CharField(max_length=300)

    def __str__(self):
        #string representation of the Quiz object
        return f"Question: {self.question} | Options: {self.optionOne}, {self.optionTwo}, {self.optionThree}"

# model to track game stats for each user
class GameStats(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)  #link to User model (ForeignKey)
    score = models.IntegerField(default=0)

    def __str__(self):
        #string representation of the GameStats object
        return f"Username: {self.user.username} | Score: {self.score}"




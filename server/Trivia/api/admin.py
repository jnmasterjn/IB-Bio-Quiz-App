from django.contrib import admin

#register models from models.py, make them accessible in the admin interface
from api.models import Quiz, GameStats

admin.site.register(Quiz)   #register the Quiz model
admin.site.register(GameStats)  # register the GameStats model
from django.contrib import admin

#put our models (databases) created in models.py into the admin page
from api.models import Quiz, gameStats

admin.site.register(Quiz)
admin.site.register(gameStats)
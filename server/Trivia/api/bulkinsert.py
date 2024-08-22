from .models import Quiz
from django.db import transaction

quizzes = [
    Quiz(
        question="Which planet in our solar system is known for having a ring system?",
        answer="Saturn",
        optionOne="Saturn",
        optionTwo="Jupiter",
        optionThree="Uranus"
    )
]

# Insert data using bulk_create
with transaction.atomic():
    Quiz.objects.bulk_create(quizzes)


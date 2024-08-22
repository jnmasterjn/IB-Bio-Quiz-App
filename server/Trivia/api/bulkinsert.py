from .models import Quiz
from django.db import transaction

quizzes = [
    Quiz(
        question="Which planet in our solar system is known for having a ring system?",
        answer="Saturn",
        optionOne="Saturn",
        optionTwo="Jupiter",
        optionThree="Uranus"
    ),
    Quiz(
        question="In which year did the Berlin Wall fall?",
        answer="1989",
        optionOne="1989",
        optionTwo="1991",
        optionThree="1987"
    ),
    Quiz(
        question="What is the smallest unit of life that can replicate independently?",
        answer="Cell",
        optionOne="Cell",
        optionTwo="Gene",
        optionThree="Atom"
    ),
    Quiz(
        question="What is the hardest natural substance on Earth?",
        answer="Diamond",
        optionOne="Diamond",
        optionTwo="Gold",
        optionThree="Iron"
    ),
    Quiz(
        question="Who was the first woman to win a Nobel Prize?",
        answer="Marie Curie",
        optionOne="Marie Curie",
        optionTwo="Rosalind Franklin",
        optionThree="Ada Lovelace"
    ),
    Quiz(
        question="Which country is the largest by land area?",
        answer="Russia",
        optionOne="Russia",
        optionTwo="Canada",
        optionThree="China"
    ),
    Quiz(
        question="Who developed the theory of relativity?",
        answer="Albert Einstein",
        optionOne="Albert Einstein",
        optionTwo="Isaac Newton",
        optionThree="Galileo Galilei"
    ),
    Quiz(
        question="What is the capital of Japan?",
        answer="Tokyo",
        optionOne="Tokyo",
        optionTwo="Osaka",
        optionThree="Kyoto"
    ),
    Quiz(
        question="Which element is known as the building block of life?",
        answer="Carbon",
        optionOne="Carbon",
        optionTwo="Oxygen",
        optionThree="Hydrogen"
    ),
    Quiz(
        question="What is the most abundant gas in Earth's atmosphere?",
        answer="Nitrogen",
        optionOne="Nitrogen",
        optionTwo="Oxygen",
        optionThree="Carbon Dioxide"
    )
]

# Insert data using bulk_create
with transaction.atomic():
    Quiz.objects.bulk_create(quizzes)


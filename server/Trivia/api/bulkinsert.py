from .models import Quiz
from django.db import transaction

Quizzes = [
    # Energy Transfer
    Quiz(
        question="What happens to energy as it moves up trophic levels in a food chain?",
        answer="Energy decreases because most is lost as heat.",
        optionOne="Energy decreases because most is lost as heat.",
        optionTwo="Energy increases as more organisms consume producers.",
        optionThree="Energy stays constant throughout the food chain."
    ),
    Quiz(
        question="What is the primary source of energy for almost all ecosystems?",
        answer="The Sun.",
        optionOne="The Sun.",
        optionTwo="Decomposers.",
        optionThree="Consumers."
    ),
    Quiz(
        question="Why is only about 10 percent of energy transferred between trophic levels?",
        answer="Energy is lost as heat and used for metabolic processes.",
        optionOne="Energy is lost as heat and used for metabolic processes.",
        optionTwo="Producers do not provide enough energy.",
        optionThree="Energy is stored in decomposers."
    ),
    Quiz(
        question="Which trophic level has the highest biomass?",
        answer="Producers.",
        optionOne="Producers.",
        optionTwo="Primary consumers.",
        optionThree="Tertiary consumers."
    ),
    # Biogeochemical Cycles
    Quiz(
        question="What is the primary process that removes carbon dioxide from the atmosphere?",
        answer="Photosynthesis.",
        optionOne="Photosynthesis.",
        optionTwo="Respiration.",
        optionThree="Decomposition."
    ),
    Quiz(
        question="Which process releases carbon dioxide into the atmosphere?",
        answer="Respiration.",
        optionOne="Respiration.",
        optionTwo="Nitrogen fixation.",
        optionThree="Photosynthesis."
    ),
    Quiz(
        question="What is the main way nitrogen is made available to plants?",
        answer="Nitrogen fixation by bacteria.",
        optionOne="Nitrogen fixation by bacteria.",
        optionTwo="Absorption of nitrogen gas directly from the atmosphere.",
        optionThree="Nitrogen released during photosynthesis."
    ),
    Quiz(
        question="Which human activity contributes most to increased levels of carbon dioxide in the atmosphere?",
        answer="Burning fossil fuels.",
        optionOne="Burning fossil fuels.",
        optionTwo="Deforestation.",
        optionThree="Planting crops."
    ),
    # Ecology and Population Dynamics
    Quiz(
        question="What is the term for the maximum population size an environment can sustain?",
        answer="Carrying capacity.",
        optionOne="Carrying capacity.",
        optionTwo="Population density.",
        optionThree="Reproductive potential."
    ),
    Quiz(
        question="What happens to prey populations when predator populations increase?",
        answer="Prey populations decrease due to increased predation.",
        optionOne="Prey populations decrease due to increased predation.",
        optionTwo="Prey populations increase as predators provide protection.",
        optionThree="Prey populations remain constant regardless of predator numbers."
    ),
    Quiz(
        question="What is an example of density-dependent population control?",
        answer="Increased competition for resources as population grows.",
        optionOne="Increased competition for resources as population grows.",
        optionTwo="A natural disaster reducing the population.",
        optionThree="Seasonal temperature changes limiting survival."
    ),
    Quiz(
        question="What happens in ecosystems when invasive species are introduced?",
        answer="They outcompete native species, reducing biodiversity.",
        optionOne="They outcompete native species, reducing biodiversity.",
        optionTwo="They increase biodiversity by adding new species.",
        optionThree="They adapt to the environment without affecting other species."
    ),
    # Greenhouse Effect and Climate Change
    Quiz(
        question="Which gas contributes most to the enhanced greenhouse effect?",
        answer="Carbon dioxide.",
        optionOne="Carbon dioxide.",
        optionTwo="Nitrogen.",
        optionThree="Oxygen."
    ),
    Quiz(
        question="What happens to oceans as atmospheric CO2 levels rise?",
        answer="Oceans become more acidic due to carbonic acid formation.",
        optionOne="Oceans become more acidic due to carbonic acid formation.",
        optionTwo="Oceans become more alkaline.",
        optionThree="Oceans release more CO2 into the atmosphere."
    ),
    Quiz(
        question="Which human activity directly increases methane levels in the atmosphere?",
        answer="Cattle farming.",
        optionOne="Cattle farming.",
        optionTwo="Deforestation.",
        optionThree="Burning fossil fuels."
    ),
    Quiz(
        question="What is the primary cause of coral bleaching?",
        answer="Rising ocean temperatures.",
        optionOne="Rising ocean temperatures.",
        optionTwo="Excess nitrogen in the water.",
        optionThree="Increased salinity of ocean water."
    ),
    # Succession and Ecosystems
    Quiz(
        question="What type of succession occurs on newly exposed volcanic rock?",
        answer="Primary succession.",
        optionOne="Primary succession.",
        optionTwo="Secondary succession.",
        optionThree="Climax succession."
    ),
    Quiz(
        question="What is the role of pioneer species in ecological succession?",
        answer="They modify the environment, making it suitable for other species.",
        optionOne="They modify the environment, making it suitable for other species.",
        optionTwo="They dominate the ecosystem permanently.",
        optionThree="They consume all resources, preventing other species from colonizing."
    ),
    Quiz(
        question="What is the final stable community called in ecological succession?",
        answer="Climax community.",
        optionOne="Climax community.",
        optionTwo="Pioneer community.",
        optionThree="Tertiary community."
    )
]

# Save these to the database within a transaction
with transaction.atomic():
    Quiz.objects.bulk_create(Quizzes)

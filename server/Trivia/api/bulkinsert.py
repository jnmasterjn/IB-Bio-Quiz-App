from .models import Quiz
from django.db import transaction

quizzes = [
    Quiz(
        question="What is the powerhouse of the cell?",
        answer="Mitochondria",
        optionOne="Mitochondria",
        optionTwo="Nucleus",
        optionThree="Ribosome"
    ),
    Quiz(
        question="Which organ is responsible for pumping blood through the body?",
        answer="Heart",
        optionOne="Heart",
        optionTwo="Lungs",
        optionThree="Liver"
    ),
    Quiz(
        question="What is the basic unit of life?",
        answer="Cell",
        optionOne="Cell",
        optionTwo="Tissue",
        optionThree="Organ"
    ),
    Quiz(
        question="Which part of the cell contains genetic material?",
        answer="Nucleus",
        optionOne="Nucleus",
        optionTwo="Mitochondria",
        optionThree="Cell Membrane"
    ),
    Quiz(
        question="What molecule carries oxygen in red blood cells?",
        answer="Hemoglobin",
        optionOne="Hemoglobin",
        optionTwo="Myoglobin",
        optionThree="Collagen"
    ),
    Quiz(
        question="Which process do plants use to make their food?",
        answer="Photosynthesis",
        optionOne="Photosynthesis",
        optionTwo="Respiration",
        optionThree="Fermentation"
    ),
    Quiz(
        question="What is the term for an organism that can make its own food?",
        answer="Autotroph",
        optionOne="Autotroph",
        optionTwo="Heterotroph",
        optionThree="Saprotroph"
    ),
    Quiz(
        question="Which gas do plants absorb from the atmosphere for photosynthesis?",
        answer="Carbon Dioxide",
        optionOne="Carbon Dioxide",
        optionTwo="Oxygen",
        optionThree="Nitrogen"
    ),
    Quiz(
        question="What is the name of the process by which cells divide to form new cells?",
        answer="Mitosis",
        optionOne="Mitosis",
        optionTwo="Meiosis",
        optionThree="Fission"
    ),
    Quiz(
        question="Which molecule serves as the main energy currency in cells?",
        answer="ATP",
        optionOne="ATP",
        optionTwo="DNA",
        optionThree="RNA"
    ),
    Quiz(
        question="What is the chemical symbol for water?",
        answer="H2O",
        optionOne="H2O",
        optionTwo="CO2",
        optionThree="O2"
    ),
    Quiz(
        question="What is the largest organ in the human body?",
        answer="Skin",
        optionOne="Skin",
        optionTwo="Liver",
        optionThree="Brain"
    ),
    Quiz(
        question="What is the primary function of the roots in plants?",
        answer="Absorb Water",
        optionOne="Absorb Water",
        optionTwo="Perform Photosynthesis",
        optionThree="Store Energy"
    ),
    Quiz(
        question="Which blood cells are responsible for fighting infections?",
        answer="White Blood Cells",
        optionOne="White Blood Cells",
        optionTwo="Red Blood Cells",
        optionThree="Platelets"
    ),
    Quiz(
        question="What is the most abundant gas in the Earth's atmosphere?",
        answer="Nitrogen",
        optionOne="Nitrogen",
        optionTwo="Oxygen",
        optionThree="Carbon Dioxide"
    ),
    Quiz(
        question="Which type of blood vessel carries blood away from the heart?",
        answer="Arteries",
        optionOne="Arteries",
        optionTwo="Veins",
        optionThree="Capillaries"
    ),
    Quiz(
        question="What part of the brain is responsible for memory and learning?",
        answer="Hippocampus",
        optionOne="Hippocampus",
        optionTwo="Cerebellum",
        optionThree="Medulla"
    ),
    Quiz(
        question="What is the term for animals that eat both plants and meat?",
        answer="Omnivores",
        optionOne="Omnivores",
        optionTwo="Herbivores",
        optionThree="Carnivores"
    ),
    Quiz(
        question="Which organ is responsible for filtering waste from the blood?",
        answer="Kidneys",
        optionOne="Kidneys",
        optionTwo="Liver",
        optionThree="Spleen"
    ),
    Quiz(
        question="What type of organisms break down dead material in an ecosystem?",
        answer="Decomposers",
        optionOne="Decomposers",
        optionTwo="Producers",
        optionThree="Consumers"
    ),
    Quiz(
        question="Which hormone regulates blood sugar levels?",
        answer="Insulin",
        optionOne="Insulin",
        optionTwo="Adrenaline",
        optionThree="Thyroxine"
    ),
    Quiz(
        question="What is the name of the process by which plants lose water through their leaves?",
        answer="Transpiration",
        optionOne="Transpiration",
        optionTwo="Photosynthesis",
        optionThree="Osmosis"
    ),
    Quiz(
        question="What is the genetic material that carries traits from parents to offspring?",
        answer="DNA",
        optionOne="DNA",
        optionTwo="RNA",
        optionThree="Proteins"
    ),
    Quiz(
        question="What is the main structural component of the plant cell wall?",
        answer="Cellulose",
        optionOne="Cellulose",
        optionTwo="Starch",
        optionThree="Chitin"
    ),
    Quiz(
        question="Which kingdom do mushrooms belong to?",
        answer="Fungi",
        optionOne="Fungi",
        optionTwo="Plantae",
        optionThree="Protista"
    ),
    Quiz(
        question="What organelle is known as the control center of the cell?",
        answer="Nucleus",
        optionOne="Nucleus",
        optionTwo="Ribosome",
        optionThree="Golgi Apparatus"
    ),
    Quiz(
        question="Which blood type is known as the universal donor?",
        answer="O Negative",
        optionOne="O Negative",
        optionTwo="AB Positive",
        optionThree="A Positive"
    ),
    Quiz(
        question="What part of the plant conducts water and nutrients from the roots to the leaves?",
        answer="Xylem",
        optionOne="Xylem",
        optionTwo="Phloem",
        optionThree="Cambium"
    ),
    Quiz(
        question="What is the term for the variety of different species in an ecosystem?",
        answer="Biodiversity",
        optionOne="Biodiversity",
        optionTwo="Population",
        optionThree="Symbiosis"
    ),
    Quiz(
        question="Which gas is produced during photosynthesis?",
        answer="Oxygen",
        optionOne="Oxygen",
        optionTwo="Carbon Dioxide",
        optionThree="Nitrogen"
    ),
    Quiz(
        question="What is the name of the protein that carries oxygen in the blood?",
        answer="Hemoglobin",
        optionOne="Hemoglobin",
        optionTwo="Myoglobin",
        optionThree="Collagen"
    ),
    Quiz(
        question="Which human body system is responsible for transporting nutrients and oxygen to cells?",
        answer="Circulatory System",
        optionOne="Circulatory System",
        optionTwo="Respiratory System",
        optionThree="Digestive System"
    ),
    Quiz(
        question="Which part of the brain controls balance and coordination?",
        answer="Cerebellum",
        optionOne="Cerebellum",
        optionTwo="Medulla",
        optionThree="Cerebrum"
    ),
    Quiz(
        question="What is the process by which plants convert light energy into chemical energy?",
        answer="Photosynthesis",
        optionOne="Photosynthesis",
        optionTwo="Chemosynthesis",
        optionThree="Respiration"
    ),
    Quiz(
        question="What is the primary pigment used by plants to absorb sunlight?",
        answer="Chlorophyll",
        optionOne="Chlorophyll",
        optionTwo="Carotene",
        optionThree="Anthocyanin"
    ),
    Quiz(
        question="What is the process by which organisms maintain a stable internal environment?",
        answer="Homeostasis",
        optionOne="Homeostasis",
        optionTwo="Metabolism",
        optionThree="Adaptation"
    ),
    Quiz(
        question="Which type of reproduction involves only one parent organism?",
        answer="Asexual Reproduction",
        optionOne="Asexual Reproduction",
        optionTwo="Sexual Reproduction",
        optionThree="Hermaphroditism"
    ),
    Quiz(
        question="What are the small structures in cells that produce proteins?",
        answer="Ribosomes",
        optionOne="Ribosomes",
        optionTwo="Mitochondria",
        optionThree="Nuclei"
    ),
    Quiz(
        question="Which part of a flower contains the ovules?",
        answer="Ovary",
        optionOne="Ovary",
        optionTwo="Anther",
        optionThree="Petal"
    ),
    Quiz(
        question="What type of biomolecule are enzymes?",
        answer="Proteins",
        optionOne="Proteins",
        optionTwo="Lipids",
        optionThree="Carbohydrates"
    ),
    Quiz(
        question="Which human body system breaks down food into nutrients?",
        answer="Digestive System",
        optionOne="Digestive System",
        optionTwo="Excretory System",
        optionThree="Circulatory System"
    )
]

# Insert data using bulk_create
with transaction.atomic():
    Quiz.objects.bulk_create(quizzes)


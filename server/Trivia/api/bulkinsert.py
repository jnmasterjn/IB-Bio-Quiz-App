from .models import Quiz
from django.db import transaction

quizzes = [
    Quiz(
        question="What is the role of helicase in DNA replication?",
        answer="Helicase unwinds the DNA double helix by breaking hydrogen bonds between the base pairs.",
        optionOne="Helicase unwinds the DNA double helix by breaking hydrogen bonds between the base pairs.",
        optionTwo="Helicase synthesizes the new DNA strand.",
        optionThree="Helicase joins Okazaki fragments together."
    ),
    Quiz(
        question="Which enzyme is responsible for adding nucleotides to the growing DNA strand during replication?",
        answer="DNA polymerase.",
        optionOne="DNA polymerase.",
        optionTwo="DNA ligase.",
        optionThree="RNA polymerase."
    ),
    Quiz(
        question="In which direction does DNA polymerase synthesize the new DNA strand?",
        answer="In the 5' to 3' direction.",
        optionOne="In the 5' to 3' direction.",
        optionTwo="In the 3' to 5' direction.",
        optionThree="In both directions."
    ),
    Quiz(
        question="What is the function of primase during DNA replication?",
        answer="Primase synthesizes a short RNA primer to provide a starting point for DNA synthesis.",
        optionOne="Primase synthesizes a short RNA primer to provide a starting point for DNA synthesis.",
        optionTwo="Primase synthesizes the Okazaki fragments.",
        optionThree="Primase removes RNA primers after replication."
    ),
    # Protein Synthesis
    Quiz(
        question="What is the first step of protein synthesis called?",
        answer="Transcription.",
        optionOne="Transcription.",
        optionTwo="Translation.",
        optionThree="Replication."
    ),
    Quiz(
        question="Which molecule carries amino acids to the ribosome during translation?",
        answer="tRNA.",
        optionOne="tRNA.",
        optionTwo="mRNA.",
        optionThree="rRNA."
    ),
    Quiz(
        question="Where does transcription occur in eukaryotic cells?",
        answer="In the nucleus.",
        optionOne="In the nucleus.",
        optionTwo="In the cytoplasm.",
        optionThree="In the ribosome."
    ),
    Quiz(
        question="What is the role of mRNA during protein synthesis?",
        answer="It carries the genetic information from DNA to the ribosome.",
        optionOne="It carries the genetic information from DNA to the ribosome.",
        optionTwo="It transports amino acids to the ribosome.",
        optionThree="It forms the core structure of the ribosome."
    ),
    # Cell Cycle and Division
    Quiz(
        question="What happens during the G1 phase of the cell cycle?",
        answer="The cell grows and carries out normal functions.",
        optionOne="The cell grows and carries out normal functions.",
        optionTwo="The cell divides into two daughter cells.",
        optionThree="The DNA is replicated."
    ),
    Quiz(
        question="During which phase of mitosis do sister chromatids separate?",
        answer="Anaphase.",
        optionOne="Anaphase.",
        optionTwo="Prophase.",
        optionThree="Metaphase."
    ),
    Quiz(
        question="What is the main purpose of mitosis?",
        answer="To produce two genetically identical daughter cells.",
        optionOne="To produce two genetically identical daughter cells.",
        optionTwo="To produce four genetically diverse daughter cells.",
        optionThree="To replicate the cell’s DNA."
    ),
    Quiz(
        question="Which phase of the cell cycle involves the replication of DNA?",
        answer="S phase.",
        optionOne="S phase.",
        optionTwo="G2 phase.",
        optionThree="M phase."
    ),
    # Nucleic Acids
    Quiz(
        question="What are the building blocks of nucleic acids?",
        answer="Nucleotides.",
        optionOne="Nucleotides.",
        optionTwo="Amino acids.",
        optionThree="Fatty acids."
    ),
    Quiz(
        question="Which nitrogenous base is found in RNA but not DNA?",
        answer="Uracil.",
        optionOne="Uracil.",
        optionTwo="Thymine.",
        optionThree="Adenine."
    ),
    Quiz(
        question="Which sugar is present in the structure of DNA?",
        answer="Deoxyribose.",
        optionOne="Deoxyribose.",
        optionTwo="Ribose.",
        optionThree="Glucose."
    ),
    Quiz(
        question="What type of bond holds the two strands of a DNA molecule together?",
        answer="Hydrogen bonds.",
        optionOne="Hydrogen bonds.",
        optionTwo="Phosphodiester bonds.",
        optionThree="Covalent bonds."
    )
]

from .models import Quiz
from django.db import transaction

quizzes = [
Quiz(
        question="In rabbits, the allele for grey fur (G) is dominant over white fur (g). Cross a heterozygous grey rabbit (Gg) with a homozygous white rabbit (gg). What are the genotypic and phenotypic ratios of the offspring?",
        answer="50% grey (Gg), 50% white (gg).",
        optionOne="50% grey (Gg), 50% white (gg).",
        optionTwo="100% grey (GG).",
        optionThree="25% grey (GG), 75% white (gg)."
    ),

    # Sex-Linked Traits (X-Linked Recessive)
    Quiz(
        question="In humans, red-green color blindness is a recessive X-linked trait. A carrier woman (X^N X^n) is crossed with a normal man (X^N Y). What percentage of their sons would be color blind?",
        answer="50% of the sons will be color blind.",
        optionOne="50% of the sons will be color blind.",
        optionTwo="100% of the sons will be color blind.",
        optionThree="0% of the sons will be color blind."
    ),

    # Blood Type (Multiple Alleles and Codominance)
    Quiz(
        question="If a woman with blood type A (I^A i) has a child with a man who has blood type B (I^B i), what are the possible blood types of their child?",
        answer="The child could have blood type A, B, AB, or O.",
        optionOne="The child could have blood type A, B, AB, or O.",
        optionTwo="The child could only have blood type AB.",
        optionThree="The child could only have blood type A or B."
    ),

    # Linked Genes
    Quiz(
        question="Two genes, A and B, are linked on the same chromosome. A heterozygous individual (AaBb) is crossed with an individual that is homozygous recessive for both traits (aabb). If there is no crossing over, what will the phenotypic ratio of the offspring be?",
        answer="1:1 ratio of AaBb to aabb.",
        optionOne="1:1 ratio of AaBb to aabb.",
        optionTwo="3:1 ratio of AaBb to aabb.",
        optionThree="9:3:3:1 ratio."
    ),

    # Dihybrid Cross (Unlinked Genes)
    Quiz(
        question="In peas, yellow seeds (Y) are dominant to green seeds (y), and round seeds (R) are dominant to wrinkled seeds (r). Cross two plants that are heterozygous for both traits (YyRr x YyRr). What is the phenotypic ratio of the offspring?",
        answer="9:3:3:1 (yellow round: yellow wrinkled: green round: green wrinkled).",
        optionOne="9:3:3:1 (yellow round: yellow wrinkled: green round: green wrinkled).",
        optionTwo="1:2:1.",
        optionThree="3:1."
    )
]

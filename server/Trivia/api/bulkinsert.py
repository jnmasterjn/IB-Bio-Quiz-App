from .models import Quiz
from django.db import transaction

quizzes = [
    Quiz(
        question="What leads to allopatric speciation?",
        answer="Geographical isolation, causing populations to diverge genetically and eventually become reproductively isolated.",
        optionOne="Geographical isolation, causing populations to diverge genetically and eventually become reproductively isolated.",
        optionTwo="Behavioural isolation, preventing individuals from recognising each other’s mating rituals.",
        optionThree="Differences in timing of reproductive cycles within the same area."
    ),
    
    # Sympatric Speciation
    Quiz(
        question="What is an example of sympatric speciation in progress?",
        answer="Apple maggot flies, where flies are diverging based on host plant preferences within the same geographical area.",
        optionOne="Apple maggot flies, where flies are diverging based on host plant preferences within the same geographical area.",
        optionTwo="Galapagos finches, which diverged due to isolation on different islands.",
        optionThree="Kaibab squirrels, which were isolated by the formation of the Grand Canyon."
    ),
    
    # Mechanisms of Reproductive Isolation
    Quiz(
        question="Which type of reproductive isolation occurs due to differences in mating rituals or courtship behaviors?",
        answer="Behavioural isolation.",
        optionOne="Behavioural isolation.",
        optionTwo="Geographical isolation.",
        optionThree="Temporal isolation."
    ),
    
    # Geographical Isolation Example
    Quiz(
        question="Which species is an example of allopatric speciation due to a geographical barrier?",
        answer="Kaibab squirrels and Abert squirrels, which were separated by the Grand Canyon.",
        optionOne="Kaibab squirrels and Abert squirrels, which were separated by the Grand Canyon.",
        optionTwo="Apple maggot flies, which diverged based on their choice of host plant.",
        optionThree="Fireflies, which evolved different light patterns."
    ),
    
    # Temporal Isolation
    Quiz(
        question="What is an example of temporal isolation leading to reproductive isolation?",
        answer="Two species of cicadas with different life cycles, maturing at different times.",
        optionOne="Two species of cicadas with different life cycles, maturing at different times.",
        optionTwo="Male fireflies of different species using different light patterns.",
        optionThree="Kaibab squirrels separated by the Grand Canyon."
    ),
    
    # Sympatric Speciation Mechanism
    Quiz(
        question="What is a key factor in sympatric speciation?",
        answer="Isolation mechanisms such as behavioural or temporal isolation occurring within the same geographical area.",
        optionOne="Isolation mechanisms such as behavioural or temporal isolation occurring within the same geographical area.",
        optionTwo="Physical barriers that prevent gene flow between populations.",
        optionThree="The introduction of a geographical barrier, like a mountain range."
    ),
    # Adaptive Radiation
    Quiz(
        question="What is adaptive radiation?",
        answer="The rapid evolution of an ancestral species into multiple species that exploit different ecological niches.",
        optionOne="The rapid evolution of an ancestral species into multiple species that exploit different ecological niches.",
        optionTwo="The gradual evolution of species without divergence into separate ecological niches.",
        optionThree="The extinction of species due to competition for resources."
    ),
    
    # Example of Adaptive Radiation
    Quiz(
        question="Which of the following is an example of adaptive radiation?",
        answer="Darwin’s finches on the Galapagos Islands.",
        optionOne="Darwin’s finches on the Galapagos Islands.",
        optionTwo="The hybridisation of a mule from a horse and a donkey.",
        optionThree="The crossing of wheat and rye plants to form hybrid offspring."
    ),
    
    # Importance of Adaptive Radiation
    Quiz(
        question="How does adaptive radiation contribute to biodiversity?",
        answer="It allows closely related species to exploit different ecological niches, reducing competition and increasing species diversity.",
        optionOne="It allows closely related species to exploit different ecological niches, reducing competition and increasing species diversity.",
        optionTwo="It forces species to compete for the same resources, leading to the survival of only the fittest species.",
        optionThree="It results in the extinction of species that fail to adapt to the same ecological niche."
    ),
    
    # Barriers to Hybridisation
    Quiz(
        question="What are prezygotic barriers in hybridisation?",
        answer="Mechanisms that prevent fertilisation, such as behavioural isolation or differences in courtship behaviour.",
        optionOne="Mechanisms that prevent fertilisation, such as behavioural isolation or differences in courtship behaviour.",
        optionTwo="Mechanisms that occur after fertilisation, such as hybrid sterility.",
        optionThree="Mechanisms that increase the fertility of hybrids."
    ),
    
    # Sterility of Interspecific Hybrids
    Quiz(
        question="Why are mules, the offspring of a donkey and a horse, sterile?",
        answer="Mules have an uneven number of chromosomes (63), preventing proper homologous chromosome pairing during meiosis.",
        optionOne="Mules have an uneven number of chromosomes (63), preventing proper homologous chromosome pairing during meiosis.",
        optionTwo="Mules are genetically incompatible with both parent species due to a lack of shared genes.",
        optionThree="Mules are produced by postzygotic barriers that prevent the formation of reproductive organs."
    ),
    
    # Example of Postzygotic Barrier
    Quiz(
        question="Which of the following is a postzygotic barrier to hybridisation?",
        answer="Reduced fertility of the hybrid, such as in the case of a mule.",
        optionOne="Reduced fertility of the hybrid, such as in the case of a mule.",
        optionTwo="Differences in courtship behavior that prevent mating between species.",
        optionThree="Differences in the timing of reproductive cycles that prevent species from mating."
    ),
    # Polyploidy Definition
    Quiz(
        question="What is polyploidy?",
        answer="A condition where a cell or organism acquires one or more additional sets of chromosomes.",
        optionOne="A condition where a cell or organism acquires one or more additional sets of chromosomes.",
        optionTwo="A condition where a cell loses chromosomes during mitosis.",
        optionThree="A mutation in the DNA sequence of a gene, causing genetic variation."
    ),
    
    # Example of Polyploidy
    Quiz(
        question="Which of the following is an example of a polyploid organism?",
        answer="A plant with 42 chromosomes (n=7) is hexaploid (6n).",
        optionOne="A plant with 42 chromosomes (n=7) is hexaploid (6n).",
        optionTwo="A plant with 14 chromosomes (n=7) is diploid (2n).",
        optionThree="A plant with 21 chromosomes (n=7) is triploid (3n)."
    ),
    
    # Even vs Odd Polyploids
    Quiz(
        question="Why are polyploids with odd numbers of chromosomes typically sterile?",
        answer="Odd chromosome numbers cause problems during meiosis as chromosomes cannot pair up correctly.",
        optionOne="Odd chromosome numbers cause problems during meiosis as chromosomes cannot pair up correctly.",
        optionTwo="Odd chromosome numbers lead to excessive DNA replication, causing sterility.",
        optionThree="Odd chromosome numbers prevent fertilisation by other species."
    ),
    
    # Allopolyploidy Definition
    Quiz(
        question="What is allopolyploidy?",
        answer="A form of polyploidy where multiple chromosome sets come from different parental species.",
        optionOne="A form of polyploidy where multiple chromosome sets come from different parental species.",
        optionTwo="A mutation that occurs due to chromosome deletions during meiosis.",
        optionThree="A condition where chromosome numbers are halved during reproduction."
    ),
    
    # Allopolyploidy Example
    Quiz(
        question="Which of the following crops is an example of an allopolyploid?",
        answer="Tobacco and wheat are examples of allopolyploid crops.",
        optionOne="Tobacco and wheat are examples of allopolyploid crops.",
        optionTwo="Bananas and strawberries are examples of allopolyploid crops.",
        optionThree="Rice and corn are examples of allopolyploid crops."
    ),
    
    # Role of Polyploidy in Speciation
    Quiz(
        question="How does polyploidy contribute to speciation in plants?",
        answer="Polyploidy can result in new species that cannot interbreed with the original parent species, leading to reproductive isolation.",
        optionOne="Polyploidy can result in new species that cannot interbreed with the original parent species, leading to reproductive isolation.",
        optionTwo="Polyploidy leads to identical offspring without any genetic variation.",
        optionThree="Polyploidy causes mutations that make the offspring more susceptible to diseases."
    )
]

from .models import Quiz
from django.db import transaction

quizzes = [
# Speciation
    Quiz(
        question="What defines a species in terms of reproductive compatibility?",
        answer="A species consists of organisms that can interbreed and produce viable, fertile offspring.",
        optionOne="A species consists of organisms that can interbreed and produce viable, fertile offspring.",
        optionTwo="A species consists of organisms that live in the same habitat and have similar appearances.",
        optionThree="A species consists of organisms that can interbreed, but their offspring are always sterile."
    ),
    Quiz(
        question="What is the process by which new species arise called?",
        answer="Speciation",
        optionOne="Speciation",
        optionTwo="Mutation",
        optionThree="Genetic drift"
    ),
    
    # Reproductive Isolation and Differential Selection
    Quiz(
        question="What is reproductive isolation?",
        answer="Reproductive isolation refers to barriers that prevent populations from interbreeding and producing fertile offspring.",
        optionOne="Reproductive isolation refers to barriers that prevent populations from interbreeding and producing fertile offspring.",
        optionTwo="Reproductive isolation refers to the inability of populations to survive in the same environment.",
        optionThree="Reproductive isolation refers to genetic differences that prevent individuals from mating."
    ),
    Quiz(
        question="Which of the following is an example of a geographical barrier that could lead to speciation?",
        answer="The formation of a mountain range dividing two populations.",
        optionOne="The formation of a mountain range dividing two populations.",
        optionTwo="The extinction of predators in a habitat.",
        optionThree="A change in climate conditions across a habitat."
    ),
    Quiz(
        question="What is differential selection?",
        answer="Differential selection is when different environmental pressures lead to the selection of different traits in separate populations.",
        optionOne="Differential selection is when different environmental pressures lead to the selection of different traits in separate populations.",
        optionTwo="Differential selection refers to the competition between species for the same resources.",
        optionThree="Differential selection is when populations evolve identical traits despite different environmental pressures."
    ),
    
    # Case Study: Chimpanzees and Bonobos
    Quiz(
        question="What led to the divergence of bonobos and chimpanzees?",
        answer="The formation of the Congo River, which geographically isolated the populations.",
        optionOne="The formation of the Congo River, which geographically isolated the populations.",
        optionTwo="Different feeding habits and competition for resources between the two populations.",
        optionThree="Climate change that affected the food supply of the populations."
    ),
    Quiz(
        question="How did differential selection lead to speciation in chimpanzees and bonobos?",
        answer="Chimpanzees evolved aggressive behaviors due to competition for resources, while bonobos evolved cooperative behaviors in an abundant resource environment.",
        optionOne="Chimpanzees evolved aggressive behaviors due to competition for resources, while bonobos evolved cooperative behaviors in an abundant resource environment.",
        optionTwo="Chimpanzees evolved larger bodies to adapt to their environment, while bonobos remained the same size.",
        optionThree="Bonobos evolved to live in a female-dominated society, while chimpanzees evolved to be solitary."
    ),
        # Evidence from Base and Amino Acid Sequences
    Quiz(
        question="What does a high degree of similarity in the amino acid sequences between two species suggest?",
        answer="It suggests a recent common ancestor between the two species.",
        optionOne="It suggests a recent common ancestor between the two species.",
        optionTwo="It indicates that the species do not share any evolutionary relationship.",
        optionThree="It shows that the species have adapted to similar environmental conditions, but are unrelated."
    ),
    Quiz(
        question="How does molecular phylogeny provide evidence for evolution?",
        answer="It compares DNA or RNA base sequences and amino acid sequences to infer evolutionary relationships.",
        optionOne="It compares DNA or RNA base sequences and amino acid sequences to infer evolutionary relationships.",
        optionTwo="It examines only the physical characteristics of organisms to determine evolutionary history.",
        optionThree="It studies only fossil records to understand the ancestry of species."
    ),
    
    # Evidence from Selective Breeding
    Quiz(
        question="What is selective breeding and how does it serve as evidence for evolution?",
        answer="Selective breeding is when humans select organisms with desirable traits for reproduction, leading to rapid genetic changes in the population.",
        optionOne="Selective breeding is when humans select organisms with desirable traits for reproduction, leading to rapid genetic changes in the population.",
        optionTwo="Selective breeding is when organisms naturally adapt to their environment without human intervention.",
        optionThree="Selective breeding is when traits are randomly passed down through generations, leading to unpredictable outcomes."
    ),
    Quiz(
        question="How did Darwin use pigeon breeding to support his theory of natural selection?",
        answer="Darwin observed that pigeon breeds descended from a common ancestor, the wild rock pigeon, after years of selective breeding.",
        optionOne="Darwin observed that pigeon breeds descended from a common ancestor, the wild rock pigeon, after years of selective breeding.",
        optionTwo="Darwin concluded that pigeon breeds evolved due to random mutations, unrelated to selective breeding.",
        optionThree="Darwin used pigeons to show that animals can only evolve in the wild and not under human influence."
    ),
    
    # Evidence from Homologous Structures
    Quiz(
        question="What is a homologous structure and how does it provide evidence for evolution?",
        answer="A homologous structure is a body part with a similar structure but different functions in different species, indicating common ancestry.",
        optionOne="A homologous structure is a body part with a similar structure but different functions in different species, indicating common ancestry.",
        optionTwo="A homologous structure is a body part that performs the same function in all organisms, regardless of structure.",
        optionThree="A homologous structure is a body part unique to one species and does not indicate evolutionary relationships."
    ),
    Quiz(
        question="Which of the following is an example of a homologous structure?",
        answer="The pentadactyl limb found in mammals like humans, whales, and bats.",
        optionOne="The pentadactyl limb found in mammals like humans, whales, and bats.",
        optionTwo="The wings of birds and insects, both used for flight.",
        optionThree="The gills of fish and lungs of mammals."
    ),
    
    # Convergent Evolution and Analogous Structures
    Quiz(
        question="What is convergent evolution?",
        answer="Convergent evolution occurs when distantly related organisms develop similar adaptations due to similar environmental pressures.",
        optionOne="Convergent evolution occurs when distantly related organisms develop similar adaptations due to similar environmental pressures.",
        optionTwo="Convergent evolution happens when organisms that share a common ancestor evolve similar traits in different environments.",
        optionThree="Convergent evolution occurs when closely related species develop unique adaptations to their environments."
    ),
    Quiz(
        question="Which of the following is an example of analogous structures?",
        answer="The wings of birds and insects, which evolved independently but perform the same function.",
        optionOne="The wings of birds and insects, which evolved independently but perform the same function.",
        optionTwo="The limbs of humans and whales, which have similar structures but different functions.",
        optionThree="The bones in the forelimbs of different mammals, which have a common evolutionary origin."
    ),
        # Evolution Definition
    Quiz(
        question="How is evolution defined in biological terms?",
        answer="A change in the heritable characteristics of a population over time.",
        optionOne="A change in the heritable characteristics of a population over time.",
        optionTwo="The physical adaptations that organisms acquire during their lifetime.",
        optionThree="The process by which organisms acquire traits from their environment."
    ),
    # Darwinian Evolution
    Quiz(
        question="According to Darwin's theory of evolution, what is the key mechanism for how species evolve over time?",
        answer="Natural selection.",
        optionOne="Natural selection.",
        optionTwo="Genetic engineering.",
        optionThree="Acquired traits from the environment."
    ),
    # Lamarckian Evolution
    Quiz(
        question="What was the main idea of Lamarckian evolution?",
        answer="Organisms acquire traits during their lifetime and pass these traits to their offspring.",
        optionOne="Organisms acquire traits during their lifetime and pass these traits to their offspring.",
        optionTwo="Traits are passed down genetically based on survival and reproduction.",
        optionThree="Species evolve randomly without a specific mechanism."
    ),
    # Difference between Darwinian and Lamarckian Evolution
    Quiz(
        question="Which of the following best distinguishes Darwinian evolution from Lamarckian evolution?",
        answer="Darwinian evolution is based on natural selection, while Lamarckian evolution involves acquired traits being passed on to offspring.",
        optionOne="Darwinian evolution is based on natural selection, while Lamarckian evolution involves acquired traits being passed on to offspring.",
        optionTwo="Darwinian evolution involves acquired traits, while Lamarckian evolution is based on natural selection.",
        optionThree="Both Darwinian and Lamarckian evolution theories are based on acquired traits being passed on to offspring."
    ),
    # Overproduction in Darwinian Evolution
    Quiz(
        question="According to Darwin, why does overproduction of offspring lead to natural selection?",
        answer="Overproduction leads to competition for resources, and individuals with favorable traits are more likely to survive.",
        optionOne="Overproduction leads to competition for resources, and individuals with favorable traits are more likely to survive.",
        optionTwo="Overproduction ensures that all offspring survive and reproduce.",
        optionThree="Overproduction helps species adapt by acquiring new traits from their environment."
    ),
    # Natural Selection and Population Adaptation
    Quiz(
        question="How does natural selection affect the proportion of individuals with favorable traits in a population over time?",
        answer="Individuals with favorable traits are more likely to survive and reproduce, increasing the proportion of these traits in the population.",
        optionOne="Individuals with favorable traits are more likely to survive and reproduce, increasing the proportion of these traits in the population.",
        optionTwo="Individuals without favorable traits reproduce more, which maintains diversity in the population.",
        optionThree="Natural selection eliminates all individuals with less favorable traits in one generation."
    ),
    # Barriers to Reproduction and Speciation
    Quiz(
        question="What role do barriers to reproduction or reproductive isolation play in evolution according to Darwin?",
        answer="They can lead to the formation of new species by preventing gene flow between populations.",
        optionOne="They can lead to the formation of new species by preventing gene flow between populations.",
        optionTwo="They increase the genetic diversity within a single species.",
        optionThree="They prevent any further evolution by separating populations permanently."
    ),
    # Evidence for Evolution
    Quiz(
        question="What are some sources of evidence for Darwinian evolution?",
        answer="Fossils, selective breeding, comparative anatomy, and geographical distribution.",
        optionOne="Fossils, selective breeding, comparative anatomy, and geographical distribution.",
        optionTwo="Acquired traits, rapid environmental changes, and genetic mutations.",
        optionThree="Environmental changes, random gene flow, and population fluctuations."
    )
]

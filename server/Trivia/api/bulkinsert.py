from .models import Quiz
from django.db import transaction

quizzes = [
    # Gene Mutations
    Quiz(
        question="What is a gene mutation?",
        answer="A structural change to a gene at the molecular level.",
        optionOne="A structural change to a gene at the molecular level.",
        optionTwo="A complete removal of a gene from the genome.",
        optionThree="A functional enhancement of a gene's activity."
    ),
    
    # Consequences of Base Substitutions
    Quiz(
        question="What is the difference between a synonymous and a non-synonymous substitution?",
        answer="A synonymous substitution does not change the amino acid sequence, while a non-synonymous substitution alters the amino acid sequence.",
        optionOne="A synonymous substitution does not change the amino acid sequence, while a non-synonymous substitution alters the amino acid sequence.",
        optionTwo="A synonymous substitution always leads to protein malfunction, while a non-synonymous substitution has no effect on proteins.",
        optionThree="A synonymous substitution changes the genetic code, while a non-synonymous substitution removes nucleotides from the sequence."
    ),
    
    # Consequences of Insertions and Deletions
    Quiz(
        question="What is a frameshift mutation?",
        answer="A mutation caused by insertions or deletions that shift the reading frame of codons, altering the resulting amino acid sequence.",
        optionOne="A mutation caused by insertions or deletions that shift the reading frame of codons, altering the resulting amino acid sequence.",
        optionTwo="A mutation caused by the substitution of a single base without affecting the reading frame.",
        optionThree="A mutation that results from the replacement of a codon with a stop codon."
    ),
    
    Quiz(
        question="What is the potential consequence of an insertion mutation?",
        answer="It can cause a frameshift mutation, leading to significant changes in the protein's amino acid sequence and possibly disrupting its function.",
        optionOne="It can cause a frameshift mutation, leading to significant changes in the protein's amino acid sequence and possibly disrupting its function.",
        optionTwo="It replaces one amino acid with another but does not impact the protein's function.",
        optionThree="It deletes part of the gene sequence, resulting in no protein being produced."
    ),
    
    Quiz(
        question="What effect can a deletion mutation have on a DNA sequence?",
        answer="It can cause a frameshift, resulting in a completely altered amino acid sequence and potentially a nonfunctional protein.",
        optionOne="It can cause a frameshift, resulting in a completely altered amino acid sequence and potentially a nonfunctional protein.",
        optionTwo="It changes the structure of the protein but does not affect its function.",
        optionThree="It inserts a new gene in place of the deleted sequence."
    ),
    
    # Base Substitutions and Their Effects
    Quiz(
        question="What is a single-nucleotide polymorphism (SNP)?",
        answer="A base substitution mutation where one nucleotide is replaced by another.",
        optionOne="A base substitution mutation where one nucleotide is replaced by another.",
        optionTwo="An insertion of a single nucleotide in a gene.",
        optionThree="A deletion of multiple nucleotides in a gene."
    ),
    
    Quiz(
        question="How can non-synonymous base substitutions affect protein function?",
        answer="They alter the amino acid sequence of the protein, which may lead to protein malfunction.",
        optionOne="They alter the amino acid sequence of the protein, which may lead to protein malfunction.",
        optionTwo="They do not affect the amino acid sequence of the protein.",
        optionThree="They cause the protein to become more efficient in its function."
    ),
       Quiz(
        question="What are the two primary causes of gene mutations?",
        answer="Errors in DNA replication/repair and mutagens such as chemicals or radiation.",
        optionOne="Errors in DNA replication/repair and mutagens such as chemicals or radiation.",
        optionTwo="Natural aging and diet.",
        optionThree="Environmental changes and protein deficiency."
    ),
    
    # Randomness in Mutation
    Quiz(
        question="What makes mutations random?",
        answer="Mutations can occur anywhere in the base sequences of a genome without deliberate selection.",
        optionOne="Mutations can occur anywhere in the base sequences of a genome without deliberate selection.",
        optionTwo="Mutations are always caused by radiation exposure.",
        optionThree="Mutations can only occur in certain gene sequences."
    ),
    
    # Consequences of Mutation in Germ and Somatic Cells
    Quiz(
        question="What is the main difference between mutations in somatic cells and germ cells?",
        answer="Mutations in somatic cells cannot be passed to offspring, while mutations in germ cells can be inherited.",
        optionOne="Mutations in somatic cells cannot be passed to offspring, while mutations in germ cells can be inherited.",
        optionTwo="Mutations in somatic cells always result in cancer, while mutations in germ cells have no effect.",
        optionThree="Mutations in somatic cells are harmless, while mutations in germ cells always cause genetic disorders."
    ),
    
    # Mutation as a Source of Genetic Variation
    Quiz(
        question="Why is gene mutation considered the original source of genetic variation?",
        answer="Gene mutations introduce new alleles into a population, contributing to diversity.",
        optionOne="Gene mutations introduce new alleles into a population, contributing to diversity.",
        optionTwo="Gene mutations always lead to harmful traits that reduce variation.",
        optionThree="Gene mutations only affect non-coding regions and do not contribute to variation."
    ),
    
    # Effects of Different Mutations
    Quiz(
        question="Which type of mutation results in the most significant changes to the protein structure?",
        answer="Frameshift mutations caused by insertions or deletions.",
        optionOne="Frameshift mutations caused by insertions or deletions.",
        optionTwo="Silent mutations caused by base substitutions.",
        optionThree="Synonymous mutations with no effect on protein structure."
    ),
    
    # Example of a Harmful Mutation
    Quiz(
        question="What is a potential consequence of a harmful mutation in a somatic cell?",
        answer="It can lead to diseases such as cancer by disrupting normal cell growth and division.",
        optionOne="It can lead to diseases such as cancer by disrupting normal cell growth and division.",
        optionTwo="It improves the fitness of the organism.",
        optionThree="It has no effect on the organism."
    ),
    
    # Beneficial Mutations
    Quiz(
        question="How can beneficial mutations affect an organism's fitness?",
        answer="Beneficial mutations can improve an organism's ability to adapt to its environment and increase reproductive success.",
        optionOne="Beneficial mutations can improve an organism's ability to adapt to its environment and increase reproductive success.",
        optionTwo="Beneficial mutations always reduce the organism's chances of survival.",
        optionThree="Beneficial mutations have no effect on an organism's fitness."
    ),
        # Gene Knockout
    Quiz(
        question="What is the purpose of gene knockout studies?",
        answer="To investigate the function of a gene by making it inoperative.",
        optionOne="To investigate the function of a gene by making it inoperative.",
        optionTwo="To add new genes to organisms.",
        optionThree="To replicate the function of genes in different species."
    ),
    
    # CRISPR and Cas9
    Quiz(
        question="What is the role of Cas9 in the CRISPR-Cas9 system?",
        answer="Cas9 is an enzyme that cuts DNA at specific target sites guided by RNA.",
        optionOne="Cas9 is an enzyme that cuts DNA at specific target sites guided by RNA.",
        optionTwo="Cas9 repairs damaged DNA sequences.",
        optionThree="Cas9 helps transcribe genes into mRNA."
    ),
    
    # CRISPR and Gene Editing
    Quiz(
        question="How is the CRISPR system adapted by scientists for gene editing?",
        answer="Scientists design single guide RNAs (sgRNA) to target specific genes for modification or deletion.",
        optionOne="Scientists design single guide RNAs (sgRNA) to target specific genes for modification or deletion.",
        optionTwo="Scientists use CRISPR to randomly mutate genes.",
        optionThree="CRISPR is used to repair DNA in all organisms without RNA involvement."
    ),
    
    # Ethical Considerations in CRISPR
    Quiz(
        question="What are some ethical concerns regarding the use of CRISPR technology?",
        answer="Concerns include off-target effects and potential use for genetic enhancement or selection.",
        optionOne="Concerns include off-target effects and potential use for genetic enhancement or selection.",
        optionTwo="It can only be used in microorganisms, limiting its scope.",
        optionThree="CRISPR may cause random mutations in all organisms without regulation."
    ),
    
    # Conserved Sequences
    Quiz(
        question="What is the significance of highly conserved sequences in genes?",
        answer="Highly conserved sequences are critical for essential cellular processes and remain unchanged due to functional constraints.",
        optionOne="Highly conserved sequences are critical for essential cellular processes and remain unchanged due to functional constraints.",
        optionTwo="Highly conserved sequences allow for rapid mutations to adapt to environmental changes.",
        optionThree="Highly conserved sequences have no role in evolution."
    ),
    
    # CRISPR Applications
    Quiz(
        question="How can CRISPR-Cas9 technology be applied in agriculture?",
        answer="CRISPR can introduce genetic modifications to enhance crop yield, nutritional content, and disease resistance.",
        optionOne="CRISPR can introduce genetic modifications to enhance crop yield, nutritional content, and disease resistance.",
        optionTwo="CRISPR can be used to delete harmful genes in crops.",
        optionThree="CRISPR only works in animal models and cannot be applied to plants."
    )
]

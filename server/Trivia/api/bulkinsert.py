from .models import Quiz
from django.db import transaction

quizzes = [
    # D3.1 Reproduction
    Quiz(
        question="How does the structure of the placenta facilitate the exchange of materials between mother and fetus?",
        answer="The placenta has villi that increase surface area for diffusion of gases, nutrients, and waste between mother and fetus.",
        optionOne="The placenta has villi that increase surface area for diffusion of gases, nutrients, and waste between mother and fetus.",
        optionTwo="The placenta has smooth membranes that actively pump nutrients into the fetus.",
        optionThree="The placenta filters harmful substances from the mother's blood but does not exchange gases."
    ),
    Quiz(
        question="What role does progesterone play in preventing uterine contractions during pregnancy?",
        answer="Progesterone inhibits uterine contractions by maintaining the uterine lining and preventing the release of prostaglandins.",
        optionOne="Progesterone inhibits uterine contractions by maintaining the uterine lining and preventing the release of prostaglandins.",
        optionTwo="Progesterone stimulates uterine muscles to relax during contractions.",
        optionThree="Progesterone promotes the release of oxytocin to suppress uterine contractions."
    ),

    # D3.2 Inheritance
    Quiz(
        question="How does the law of segregation relate to the inheritance of alleles in gametes?",
        answer="The law of segregation states that each gamete receives only one allele for each gene during meiosis.",
        optionOne="The law of segregation states that each gamete receives only one allele for each gene during meiosis.",
        optionTwo="The law of segregation states that dominant alleles are separated from recessive alleles during fertilization.",
        optionThree="The law of segregation explains that only dominant alleles are passed on to offspring."
    ),
    Quiz(
        question="What is pleiotropy, and how does it affect multiple traits in an organism?",
        answer="Pleiotropy occurs when one gene influences multiple traits, such as the gene responsible for sickle cell anemia affecting both red blood cell shape and malaria resistance.",
        optionOne="Pleiotropy occurs when one gene influences multiple traits, such as the gene responsible for sickle cell anemia affecting both red blood cell shape and malaria resistance.",
        optionTwo="Pleiotropy occurs when multiple genes influence a single trait, as seen in skin color.",
        optionThree="Pleiotropy is the inheritance of two dominant alleles that produce a blended phenotype."
    ),

    # D1.3 Mutation and Gene Editing
    Quiz(
        question="What is a missense mutation, and how does it differ from a silent mutation?",
        answer="A missense mutation changes the amino acid sequence of a protein, while a silent mutation does not affect the protein’s function.",
        optionOne="A missense mutation changes the amino acid sequence of a protein, while a silent mutation does not affect the protein’s function.",
        optionTwo="Both missense and silent mutations result in shortened proteins.",
        optionThree="A missense mutation introduces a stop codon, whereas a silent mutation changes the protein sequence without affecting its function."
    ),
    Quiz(
        question="How do insertions and deletions (indels) cause frameshift mutations, and why are these mutations often more harmful?",
        answer="Indels cause frameshift mutations by altering the reading frame, leading to widespread changes in the amino acid sequence and often resulting in a non-functional protein.",
        optionOne="Indels cause frameshift mutations by altering the reading frame, leading to widespread changes in the amino acid sequence and often resulting in a non-functional protein.",
        optionTwo="Indels cause point mutations by altering only one amino acid, which can sometimes be repaired.",
        optionThree="Indels are typically harmless since they occur in non-coding regions of DNA."
    ),

    # D2.2 Gene Expression (HL only)
    Quiz(
        question="How do transcription factors regulate gene expression in response to environmental signals?",
        answer="Transcription factors bind to specific DNA sequences, either promoting or inhibiting the transcription of genes in response to environmental cues.",
        optionOne="Transcription factors bind to specific DNA sequences, either promoting or inhibiting the transcription of genes in response to environmental cues.",
        optionTwo="Transcription factors degrade mRNA molecules after they are transcribed, controlling gene expression.",
        optionThree="Transcription factors activate RNA polymerase directly to control transcription rates."
    ),
    Quiz(
        question="How does RNA interference (RNAi) regulate gene expression at the post-transcriptional level?",
        answer="RNA interference involves small RNAs binding to mRNA, leading to its degradation or the prevention of its translation into proteins.",
        optionOne="RNA interference involves small RNAs binding to mRNA, leading to its degradation or the prevention of its translation into proteins.",
        optionTwo="RNA interference promotes faster translation of mRNA into proteins, enhancing gene expression.",
        optionThree="RNA interference prevents the splicing of mRNA, thus increasing gene expression."
    ),

    # A4.1 Evolution and Speciation
    Quiz(
        question="What is the founder effect, and how does it contribute to genetic drift?",
        answer="The founder effect occurs when a small group of individuals becomes isolated from a larger population, leading to reduced genetic diversity and increased genetic drift.",
        optionOne="The founder effect occurs when a small group of individuals becomes isolated from a larger population, leading to reduced genetic diversity and increased genetic drift.",
        optionTwo="The founder effect happens when a population grows rapidly, reducing genetic variation.",
        optionThree="The founder effect leads to hybrid species through crossbreeding between isolated groups."
    ),
    Quiz(
        question="How do homologous structures provide evidence for common ancestry among species?",
        answer="Homologous structures are anatomical features that share a common origin but may have different functions, indicating a shared ancestor.",
        optionOne="Homologous structures are anatomical features that share a common origin but may have different functions, indicating a shared ancestor.",
        optionTwo="Homologous structures are features that develop independently in unrelated species as a result of similar environmental pressures.",
        optionThree="Homologous structures are features that serve the same function in different species but do not have a common evolutionary origin."
    ),

    # A1.2 Nucleic Acid
    Quiz(
        question="How do phosphodiester bonds contribute to the structure of the DNA double helix?",
        answer="Phosphodiester bonds connect the sugar-phosphate backbone of DNA, providing structural stability to the double helix.",
        optionOne="Phosphodiester bonds connect the sugar-phosphate backbone of DNA, providing structural stability to the double helix.",
        optionTwo="Phosphodiester bonds link nitrogenous bases together to form the rungs of the double helix.",
        optionThree="Phosphodiester bonds attach the double helix to the cell membrane during cell division."
    ),
    Quiz(
        question="What is the significance of the antiparallel orientation of the two strands of DNA?",
        answer="The antiparallel orientation ensures that the two DNA strands can form complementary base pairs and be efficiently replicated.",
        optionOne="The antiparallel orientation ensures that the two DNA strands can form complementary base pairs and be efficiently replicated.",
        optionTwo="The antiparallel orientation prevents the strands from unwinding during replication.",
        optionThree="The antiparallel orientation is only required during transcription and has no effect on replication."
    ),

    # D1.1 DNA Replication
    Quiz(
        question="Describe the role of single-strand binding proteins (SSBs) in DNA replication.",
        answer="Single-strand binding proteins stabilize the unwound DNA strands to prevent them from re-annealing during replication.",
        optionOne="Single-strand binding proteins stabilize the unwound DNA strands to prevent them from re-annealing during replication.",
        optionTwo="Single-strand binding proteins catalyze the addition of nucleotides during replication.",
        optionThree="Single-strand binding proteins cut the DNA to allow replication to proceed."
    ),
    Quiz(
        question="What is the significance of the replication origin in DNA replication?",
        answer="The replication origin is the site where replication begins, allowing the formation of replication forks and the initiation of DNA synthesis.",
        optionOne="The replication origin is the site where replication begins, allowing the formation of replication forks and the initiation of DNA synthesis.",
        optionTwo="The replication origin is where DNA ligase binds to begin sealing Okazaki fragments.",
        optionThree="The replication origin is the site where ribosomes attach to DNA for protein synthesis."
    ),

    # D1.2 Protein Synthesis
    Quiz(
        question="How does the poly-A tail added to mRNA molecules affect their stability and function?",
        answer="The poly-A tail protects mRNA from degradation and aids in the export of mRNA from the nucleus to the cytoplasm.",
        optionOne="The poly-A tail protects mRNA from degradation and aids in the export of mRNA from the nucleus to the cytoplasm.",
        optionTwo="The poly-A tail prevents the mRNA from being translated until it is removed.",
        optionThree="The poly-A tail directs mRNA to the endoplasmic reticulum for translation."
    ),
    Quiz(
        question="What is the role of elongation factors in the process of translation?",
        answer="Elongation factors assist in the binding of tRNA to the ribosome and the translocation of the ribosome along the mRNA strand during translation.",
        optionOne="Elongation factors assist in the binding of tRNA to the ribosome and the translocation of the ribosome along the mRNA strand during translation.",
        optionTwo="Elongation factors terminate translation by releasing the newly synthesized polypeptide from the ribosome.",
        optionThree="Elongation factors are involved in the modification of tRNA after translation is completed."
    ),

    # D2.1 Cell and Nuclear Division
    Quiz(
        question="How does cytokinesis differ between animal and plant cells?",
        answer="In animal cells, cytokinesis occurs through cleavage furrow formation, while in plant cells, a cell plate forms to divide the cell.",
        optionOne="In animal cells, cytokinesis occurs through cleavage furrow formation, while in plant cells, a cell plate forms to divide the cell.",
        optionTwo="In animal cells, cytokinesis requires the cell wall to split, while in plant cells, the membrane pinches inward.",
        optionThree="In both plant and animal cells, cytokinesis occurs by the same process of forming a cell plate."
    ),
    Quiz(
        question="What is the role of the G1 checkpoint in the cell cycle, and how does it prevent uncontrolled cell division?",
        answer="The G1 checkpoint assesses cell size, nutrients, and DNA integrity, ensuring that conditions are favorable before DNA replication begins.",
        optionOne="The G1 checkpoint assesses cell size, nutrients, and DNA integrity, ensuring that conditions are favorable before DNA replication begins.",
        optionTwo="The G1 checkpoint allows cells to skip the S phase and go directly to mitosis if needed.",
        optionThree="The G1 checkpoint repairs DNA mutations before the cell can proceed to DNA replication."
    ),
]
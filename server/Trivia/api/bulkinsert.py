from .models import Quiz
from django.db import transaction

quizzes = [
Quiz(
        question="What is gene expression?",
        answer="Gene expression is the process by which genetic information is used to produce RNA and proteins.",
        optionOne="Gene expression is the process by which genetic information is used to produce RNA and proteins.",
        optionTwo="Gene expression is the mutation of genes over time.",
        optionThree="Gene expression is the process by which DNA is replicated during cell division."
    ),
    Quiz(
        question="How does gene expression affect phenotype?",
        answer="Gene expression controls the production of proteins, which in turn determine the structure and function of cells, influencing the organism's phenotype.",
        optionOne="Gene expression controls the production of proteins, which in turn determine the structure and function of cells, influencing the organism's phenotype.",
        optionTwo="Gene expression causes mutations that change the organism's physical characteristics.",
        optionThree="Gene expression only affects the genotype and has no impact on phenotype."
    ),
    
    # Regulation of Transcription
    Quiz(
        question="How can transcription be regulated by proteins?",
        answer="Transcription can be regulated by transcription factors that either activate or repress the binding of RNA polymerase to DNA.",
        optionOne="Transcription can be regulated by transcription factors that either activate or repress the binding of RNA polymerase to DNA.",
        optionTwo="Transcription is only regulated by mutations in the gene sequence.",
        optionThree="Transcription is regulated through the translation of proteins."
    ),
    Quiz(
        question="What is the role of enhancers in transcription?",
        answer="Enhancers are regions of DNA that can bind activator proteins to facilitate RNA polymerase binding to the promoter, enhancing gene transcription.",
        optionOne="Enhancers are regions of DNA that can bind activator proteins to facilitate RNA polymerase binding to the promoter, enhancing gene transcription.",
        optionTwo="Enhancers prevent transcription by blocking RNA polymerase from binding to DNA.",
        optionThree="Enhancers are non-coding regions that only degrade mRNA."
    ),
    
    # Regulation of Translation
    Quiz(
        question="How can the persistence of mRNA regulate gene expression?",
        answer="The longer an mRNA molecule persists, the more it can be translated into protein, thus increasing gene expression.",
        optionOne="The longer an mRNA molecule persists, the more it can be translated into protein, thus increasing gene expression.",
        optionTwo="The persistence of mRNA has no effect on gene expression.",
        optionThree="The persistence of mRNA only determines whether or not the gene is transcribed."
    ),
    Quiz(
        question="Which modifications to mRNA increase its stability?",
        answer="The addition of a guanine cap at the 5' end and a poly-A tail at the 3' end increases the stability of mRNA.",
        optionOne="The addition of a guanine cap at the 5' end and a poly-A tail at the 3' end increases the stability of mRNA.",
        optionTwo="Only the addition of a poly-A tail increases the stability of mRNA.",
        optionThree="mRNA is only stabilised by protein binding, not by chemical modifications."
    ),
        # Epigenesis
    Quiz(
        question="What is epigenesis?",
        answer="Epigenesis is the process by which cells and organisms develop from an undifferentiated zygote through interactions between DNA and environmental factors.",
        optionOne="Epigenesis is the process by which cells and organisms develop from an undifferentiated zygote through interactions between DNA and environmental factors.",
        optionTwo="Epigenesis is the permanent alteration of the DNA sequence in response to environmental changes.",
        optionThree="Epigenesis is the random mutation of genes in response to environmental stress."
    ),
    
    # Genome, Transcriptome, and Proteome
    Quiz(
        question="How are the genome, transcriptome, and proteome different in individual cells?",
        answer="The genome is the complete set of DNA, the transcriptome is the set of RNA transcripts, and the proteome is the entire set of proteins expressed in a cell.",
        optionOne="The genome is the complete set of DNA, the transcriptome is the set of RNA transcripts, and the proteome is the entire set of proteins expressed in a cell.",
        optionTwo="The transcriptome is the complete set of DNA, the proteome is the set of RNA transcripts, and the genome is the entire set of proteins expressed in a cell.",
        optionThree="The genome is the set of proteins, the transcriptome is the complete set of DNA, and the proteome is the set of RNA transcripts in a cell."
    ),
    
    # Methylation and Gene Expression
    Quiz(
        question="How does DNA methylation affect gene expression?",
        answer="Methylation of cytosine in promoter regions represses transcription by preventing transcription factors from binding, thereby decreasing gene expression.",
        optionOne="Methylation of cytosine in promoter regions represses transcription by preventing transcription factors from binding, thereby decreasing gene expression.",
        optionTwo="Methylation of cytosine activates transcription by facilitating the binding of transcription factors.",
        optionThree="Methylation has no effect on gene expression and only alters the DNA sequence."
    ),
    
    # Histone Acetylation and Methylation
    Quiz(
        question="What is the effect of histone acetylation on gene expression?",
        answer="Histone acetylation reduces the positive charge on histone tails, loosening DNA-histone interactions and increasing gene expression.",
        optionOne="Histone acetylation reduces the positive charge on histone tails, loosening DNA-histone interactions and increasing gene expression.",
        optionTwo="Histone acetylation increases the positive charge on histone tails, tightening DNA-histone interactions and decreasing gene expression.",
        optionThree="Histone acetylation has no effect on gene expression."
    ),
    Quiz(
        question="How does histone methylation affect gene expression?",
        answer="Histone methylation can either activate or repress gene expression, depending on the amino acid methylated and the number of methyl groups added.",
        optionOne="Histone methylation can either activate or repress gene expression, depending on the amino acid methylated and the number of methyl groups added.",
        optionTwo="Histone methylation always represses gene expression by preventing the binding of RNA polymerase.",
        optionThree="Histone methylation always activates gene expression by enhancing RNA polymerase activity."
    ),
    
    # Epigenetic Inheritance
    Quiz(
        question="What is epigenetic inheritance?",
        answer="Epigenetic inheritance refers to the transmission of non-genetic information, such as DNA methylation or histone modifications, that can influence gene expression in offspring.",
        optionOne="Epigenetic inheritance refers to the transmission of non-genetic information, such as DNA methylation or histone modifications, that can influence gene expression in offspring.",
        optionTwo="Epigenetic inheritance refers to the inheritance of genetic mutations that occur during development.",
        optionThree="Epigenetic inheritance only occurs during environmental adaptation in somatic cells."
    ),
    Quiz(
        question="How does air pollution affect gene expression?",
        answer="Air pollution affects DNA methylation patterns, leading to increased inflammation, oxidative stress, and immune response disruption.",
        optionOne="Air pollution affects DNA methylation patterns, leading to increased inflammation, oxidative stress, and immune response disruption.",
        optionTwo="Air pollution causes genetic mutations directly in the DNA sequence.",
        optionThree="Air pollution has no impact on gene expression."
    ),
    
    # Removal of epigenetic tags
    Quiz(
        question="What happens to most epigenetic tags during fertilization?",
        answer="Most epigenetic tags are removed, allowing for the reset of gene expression and the development of new epigenetic modifications.",
        optionOne="Most epigenetic tags are removed, allowing for the reset of gene expression and the development of new epigenetic modifications.",
        optionTwo="All epigenetic tags are removed entirely from the genome.",
        optionThree="No epigenetic tags are removed, and all are passed on to offspring."
    ),
    
    # Monozygotic twins studies
    Quiz(
        question="Why are monozygotic twins useful for studying gene expression?",
        answer="Monozygotic twins have identical genomes, so any differences in their traits are due to environmental or epigenetic factors.",
        optionOne="Monozygotic twins have identical genomes, so any differences in their traits are due to environmental or epigenetic factors.",
        optionTwo="Monozygotic twins have identical environments, so any differences in traits are genetic.",
        optionThree="Monozygotic twins have completely different genomes, making them ideal for studying genetic disorders."
    ),
    
    # External factors impacting gene expression
    Quiz(
        question="How does the presence of lactose impact the expression of the lac operon in bacteria?",
        answer="When lactose is present, it binds to the repressor, allowing RNA polymerase to bind to the promoter and express the genes in the lac operon.",
        optionOne="When lactose is present, it binds to the repressor, allowing RNA polymerase to bind to the promoter and express the genes in the lac operon.",
        optionTwo="When lactose is present, it prevents RNA polymerase from binding to the promoter, inhibiting gene expression.",
        optionThree="Lactose presence has no effect on gene expression in bacteria."
    ),
    
    Quiz(
        question="What effect does oestradiol have on gene expression?",
        answer="Oestradiol binds to intracellular receptors, forming a complex that can enter the nucleus and promote the transcription of target genes.",
        optionOne="Oestradiol binds to intracellular receptors, forming a complex that can enter the nucleus and promote the transcription of target genes.",
        optionTwo="Oestradiol binds directly to DNA to inhibit transcription of certain genes.",
        optionThree="Oestradiol has no impact on gene expression in cells."
    ),
    
    Quiz(
        question="What happens to gene expression when the tryptophan operon is exposed to high levels of tryptophan?",
        answer="High levels of tryptophan bind to the repressor, causing it to inhibit the operon by preventing RNA polymerase from transcribing the genes.",
        optionOne="High levels of tryptophan bind to the repressor, causing it to inhibit the operon by preventing RNA polymerase from transcribing the genes.",
        optionTwo="High levels of tryptophan activate RNA polymerase, increasing gene transcription.",
        optionThree="Tryptophan presence does not affect gene expression in the operon."
    ),
    
    # Methylation and gene expression
    Quiz(
        question="How does methylation of cytosine in DNA affect gene expression?",
        answer="Methylation of cytosine in promoter regions prevents transcription factors from binding, reducing gene expression.",
        optionOne="Methylation of cytosine in promoter regions prevents transcription factors from binding, reducing gene expression.",
        optionTwo="Methylation of cytosine in promoter regions enhances the binding of transcription factors, increasing gene expression.",
        optionThree="Methylation of cytosine has no effect on gene expression."
    )
]

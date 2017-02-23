# A new CNV calling method
  A memo for the development of novel CNV calling tools. To detect novel copy number variation events in plasma samples, here we develop a novel tool called ctCNV to help find such events.

## Basical idea
  Based on the read depth coverage of capture seqencing data, significance testing (EWT) algorithm will be used to found signicicantly altered CNV envents in case samples compared to a pool of normal control samples. The main python script is based on the improvement and application of CNVkit library (Thanks Eric Talevich! [CNVkit on Github](https://github.com/etal/cnvkit)). 

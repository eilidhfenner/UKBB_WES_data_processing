# UK Biobank WES data processing

The majority of the processing of this large scale WES dataset was achieved using Hail – an open source python library designed for the exploration and analysis of large scale genomic datasets. Hail is built for an Apache Spark environment, enabling scalability and parallelisation of processing. Within this library are numbered scripts for the processing of the dataset using Hail, PLINK and R. 

# 0: Running scripts in a bash environment
`00_Array_bash.sh` - A bash script to run Hail, and other scripts through. 

The SBATCH commands set up the job as required, setting memory, tasks, and the array. Required modules are then loaded, and temporary directories are set. The python script is then run. Most scripts were run one chromosome at a time, as working with a table containing data from all chromosomes was hard computationally. This array bash script runs the python script on each chromosome individually. 

# 1: Building matrix tables and genotype QC 
`01_build_mt_genotype_QC.py` - A Hail python script to process the pVCFs and build matrix tables (one per chromosome) from them. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). Orignal counts of variants are calculated before removal 'monoallelic' sites and those with >6 alleles. Multi-allelic sites are then split and genotype QC was performed. This script also generates and exports sample and variant QC metrics both before and after genotype QC. The resulting matrix table is filtered for only genotype entries to save space, and then saved. 

## Matrix tables 
Initially, almost 1000 block pVCFs were downloaded from UK Biobank. These blocks contained slightly different sample IDs due to samples requesting removal from the dataset. Samples were matched up and those requesting removal were removed. Following this, pVCFs were rewritten before VCFs from all blocks for each chromosome were read into one Hail matrix table. Matrix tables are Hail specific data structures combining features of matrices and data frames. Matrix tables split data into hundreds or thousands of partitions, allowing for the parallelisation of processing across the dataset – as tasks can be run on multiple partitions at one time. 
## Filtering variants
Following matrix tables being built for each chromosome, original variant counts were calculated. Sites labelled in the VCFs by GLNexus as ‘mono-allelic’ were removed. These are defined as sites representing an alternate allele region with multiple variants that ‘could not be unified into non-overlapping multiallelic sites’. These typically make up less than 1 percent of sites. Sites with more than 6 alleles were removed and multi-allelic sites were split. 
## Genotype QC 
Next, genotypes were filtered based on the following criteria:
- Unusual allele balance. Removed genotypes listed as: homozygous reference with >10% alternate allele reads; homozygous alternate with >10% reference allele reads; heterozygous without a reference alternate allele balance of around 1:1 ; removed genotypes with alternate allele proportion of less than 25% or over 75%. 
- Depth of less than 10.
- Genotype quality of less than 30. 

Subsequently, sites with no variants remaining were removed.Entries within the matrix table were then filtered to keep only the genotype (removing metrics such as depth and genotype quality), making the size of the matrix tables much more manageable. 

# 2-4: Visualising and filtering on variant and sample QC metrics
## Visualising variant QC metrics 
`02_Variant_QC.R` - An R script used to visualise post genotype QC variant QC metrics from all chromosomes. A table of metrics from across all chromosomes is saved.

As with the sample QC, the tables of variant QC metrics are for each chromosome. To effectively visualise these metrics, plots of them across all chromosomes were created. From these plots, cut-off values were set and variants outside of these cut-offs were removed in `04_sample_variant_QC.py`. 
## Visualising sample QC metrics
`03_Sample_QC.R` - An R script used to calculate post genotype QC sample QC metrics from all chromosomes, plot these metrics, and apply a call rate cut-off. Sample QC metrics were then saved, as was a table of samples passing sample QC to be read back into hail in `04_sample_variant_QC.py`. 

Within Hail, each chromosome was processed individually, therefore sample QC metrics calculated by hail are for each individual chromosome. The above script is therefore used reformat per chromosome sample QC metrics, and then to calculate sample QC metrics across all chromosomes. These metrics are then plotted and based on the plots, a call rate filter is applied. Samples with a mean call rate of less than 0.8 are removed, and the list of samples passing this filter is exported. A table of sample QC metrics across all chromosomes is also written. 
## Filtering on sample and variant QC cut-offs
`04_sample_variant_QC.py` - A Hail python script to perform sample and variant QC and save out a matrix table of high quality variants and samples. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). 
### Variant QC 
Script 04 filters variants, removing those with:
- Genotype quality (GQ) of less than or equal to 40.
- Call rate of less than or equal to 0.9.
- Variants lying within low complexity regions. 
### Sample QC 
Script 04 reads in a list of samples to keep based on the removal of samples with a mean call rate of less than 0.8.

# 5 - 8 : Selecting high quality, common variants for ancestry annotations
Following genotype, sample and variant QC, high quality, common variants were selected using the following criteria: 
- Variant frequency – selected variants with a minor allele frequency of >1%
- Call rate – selected variants with a call rate of >.98. 
- Hardy Weinberg equilibrium p-value  >0.00000001

These common, high quality variants from each chromosome were then exported to plink format and pruned to pseudo-independent SNPs. These pruned SNPs were read back into Hail as matrix tables (one per chromosome) before being merged into one matrix table consisting of pruned variants from all chromsomes. These common,high quality, LD pruned variants were then used in:

`05_Common_var_PLINK.py` - A Hail python script to filter variants based on Hardy Weinberg equilibrium p-value and allele frequency, then write the passing variants as PLINK files. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). 

`06_prune_variants.sh` - A bash script using PLINK to perform LD pruning of the high quality common variants (R^2 = 0.5). This is an array script and is run on each chromosome. 

`07_pruned_var_matrix_tables.py` - A Hail python script to build and write matrix tables (one per chromosome) from the lists of LD pruned variants from PLINK. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). 

`08_merge_pruned_variants.py` - A Hail python script to read each pruned variant matrix table and merge into one table of high quality, common, LD pruned variants from across all chromosomes. Two versions of this table are then saved - one with the sex chromosomes included, and one of only the autosomes. 

# 9: Defining genetic ancestries
`09_PCAs.py` - A Hail python script which reads in the matrix table of pruned autosomes from all chromosomes, performs a prinicipal component analysis on the Hardy-Weinberg normalised genotype calls, and then exports a table of 10 principal components. This table was then read into R and annotated to phenotypes. Genetic ancestries were then defined using the first two principal components alongside self-reported ethnic background.


# 10: Highlighting related samples 
Relatedness of participants was calcuated using the kinship matrix available from UK Biobank.
`10_relatedness.R` - An R script to select samples to remove based on relatedness. These samples are then filtered out in `15_annotate_variants.py`.

# 11 - 12: Imputing sex 
`11_impute_sex.py` - A hail python script to filter the X chromosome matrix table for call rate and MAF, and use these filtered variants to impute sex. The results of this are then written as a hail table and exported for further investigation in R (`12_Impute_sex.R`). 
## Variant filtering 
Variants on the x chromosome were filtered and were removed if they had: 
- A call rate of less than .97
- A minor allele frequency of less than 1%
## Imputing sex
The filtered variants were then used to impute sex. This is acheived in Hail by calculating the inbreeding co-efficient (f_stat) on the X chromosome. The f_stat was then used to assign sex: 
- Less than 0.6 - female
- Over 0.6 - male
## Visualising and filtering samples on imputed sex
Samples whose imputed sex and self reported sex did not match were identified.

`12_Impute_sex.R` - An R script used to merge self reported sex, y chromosome depth, and imputed sex data. Plots are made to visualise the imputed sex f-statistic and y depth and their relationship with self-reported sex. Finally, samples with mismatching self reported and imputed sex are highlighted and removed from the dataset - a list of samples to keep is written and is used to filter samples in `15_annotate_variants.py`.

# 13 - 14 : Setting up annotation files 
To annotate variants with functional consequences, pathogenicity metrics, and frequency in other datasets, annotation files first had to be prepared. 

## Ensembl VEP 
`13_vep-config_loftee.json` - VEP annotations can be run in Hail using a .json script.

## dbNSFP 
`14_build_dbNSFP.py` - A script preparing dbNSFP for use in Hail. 

# 15 - 16: Final filtering and annotating variants with functional consequence 
`15_annotate_variants.py` - A Hail python script to filter samples and variants as above, and then annotate variants with frequencies in other datasets and scores of missense pathogenicity. These annotations were formatted for use here in `13_vep-config_loftee.json` and `14_build_dbNSFP.py`. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). 

## Final filtering
Following pruning, relatedness and ancestry investigation, variants and samples were filtered to remove:
- Related individuals, based on a kinship cut-off set to remove 1st, 2nd and 3rd degree relatives. See `10_Relatedness.R` to see how samples to remove based on relatedness were selected.
- Samples whose imputed sex and self reported sex did not match. These were identified in `12_impute_sex.R`. 

## Annotations
All variants were then annotated with: 
- Ensembl's VEP with a LOFTEE plug-in
- Frequencies in other datasets: TopMED and GnomAD.
- Scores of missense pathogenicity: MPC scores, CADD scores, and REVEL scores. 

`16_VEP_annotations.py` - A Hail python script to add further annotations to variants, including most severe consequence and LOFTEE annotations. VEP annotations run in Hail using a .json script (`13_vep-config_loftee.json`). Following this, sets of annotations are formed and variants are then annotated with their worst consequence. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). 

# 17: Preparing gene sets for counts of qualifying variants 
`17_gene_sets.py` - A script to read in lists of Ensembl IDs from different gene sets and write out as a hail table for use in counting variants in gene sets. 


# 18: Counting qualifying variants 
## Count
`18_count_qualifying_variants.py` -  A script to count the number of qualifying variants in specific gene sets and write out these counts for use in regression analyses. This script is run on one chromosome at a time using a bash array script (`00_Array_bash.sh`). This is rerun for each gene set, and the script is an example for the LoFi set of genes. 

Once all variants were annotated, sets of qualifying variants could be counted per individual and per gene. 

# 19: Merge qualifying variant counts from across chromosomes
`19_merge_qualifying_variants.R` - Read in counts of variants from each chromosome and totals these across chromosomes, then write out a final total count table. This is rerun for each gene set, and the script is an example for the LoFi set of genes. 

# 20: Regress counts against phenotypes 
`20_regression.R` - This script reads in the counts of variants for the gene set, annotates it to a file containing phenotypic data and then runs a linear regression. This is rerun for each gene set, and the script is an example for the LoFi set of genes. 

# SET UP HAIL
## Read in argument from bash script - this argument is the chromosome number.
import sys
print(sys.argv[0])
print('This is the 1st argument (chromosome): ' + sys.argv[1])

import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.
so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})
from hail import *
import hail.expr.functions

# Read in matrix table
mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd_rmsexmismatch_rmrelated_annotated.mt')

# Filter to gene set of interest
# e.g. for constrained genes based on pLI score 
gene_set='LoFi_pli'
mt=mt.key_rows_by(mt.gene_id_worstCsq)
c=hl.read_table('/scratch/c.c1928239/annotations/gnomad_LoF_annotations.ht')
mt=mt.annotate_rows(LoF_gene_pLI =c[mt.gene_id_worstCsq].pli_9)
mt=mt.key_rows_by(mt.locus, mt.alleles)
mt=mt.filter_rows(mt.LoF_gene_pLI==True)
print(mt.count())


# To run counts on other sets, just switch out the constrained set for another set: 

## e.g. for LOEUF decile 1 
#gene_set='LOEUF_decile_1'
#dec=hl.read_table('/scratch/c.c1928239/annotations/gene_sets/obs_exp_deciles.ht')                                                                                                  
#mt=mt.key_rows_by(mt.gene_id_worstCsq) 
#mt=mt.annotate_rows(Obs_exp_decile=dec[mt.gene_id_worstCsq].decile) 
#mt=mt.key_rows_by(mt.locus, mt.alleles)
##Filter to one decile
#mt=mt.filter_rows(mt.Obs_exp_decile==1)

## e.g. for SCHEMA FDR set: 
#gene_set='SCHEMA_FDR_5'
#s=hl.read_table('/scratch/c.c1928239/annotations/gene_sets/Schema_annotations.ht')
#mt=mt.annotate_rows(schema_FDR_5_gene=s[mt.gene_id_worstCsq].Schema_FDR_5)
#mt=mt.key_rows_by(mt.locus, mt.alleles)
#mt=mt.filter_rows(mt.schema_FDR_5_gene==True)

## e.g. for CNV loci:
#gene_set='schizophrenia_enriched_CNVs'
#cnv=hl.import_locus_intervals('/scratch/c.c1928239/annotations/gene_sets/SZ_enriched_CNV_loci.bed', reference_genome='GRCh38')  
#mt=mt.annotate_rows(SZ_enriched_CNV_set=hl.is_defined(cnv[mt.locus])) 
#mt=mt.filter_rows(mt.SZ_enriched_CNV_set==True)



# COUNT QUALIFYING VARIANTS for each sample

# Variant frequencies, all annotations
mt = mt.annotate_cols(n_AC1 = hl.agg.filter((mt.variant_qc.AC[1]==1),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC2 = hl.agg.filter((mt.variant_qc.AC[1]==2),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC3 = hl.agg.filter((mt.variant_qc.AC[1]==3),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC4=hl.agg.filter((mt.variant_qc.AC[1]==4),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC5=hl.agg.filter((mt.variant_qc.AC[1]==5),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC6to10=hl.agg.filter((mt.variant_qc.AC[1]<=10)&(mt.variant_qc.AC[1]>=6),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC11to20=hl.agg.filter((mt.variant_qc.AC[1]<=20)&(mt.variant_qc.AC[1]>=11),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC21to50=hl.agg.filter((mt.variant_qc.AC[1]<=50)&(mt.variant_qc.AC[1]>=21),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC51to100=hl.agg.filter((mt.variant_qc.AC[1]<=100)&(mt.variant_qc.AC[1]>=51),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_AC101to200=hl.agg.filter((mt.variant_qc.AC[1]<=200)&(mt.variant_qc.AC[1]>=101),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC1 = hl.agg.filter((mt.variant_qc.AC[1]==1)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC2 = hl.agg.filter((mt.variant_qc.AC[1]==2)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC3 = hl.agg.filter((mt.variant_qc.AC[1]==3)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC4=hl.agg.filter((mt.variant_qc.AC[1]==4)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC5=hl.agg.filter((mt.variant_qc.AC[1]==5)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC6to10=hl.agg.filter((mt.variant_qc.AC[1]<=10)&(mt.variant_qc.AC[1]>=6)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC11to20=hl.agg.filter((mt.variant_qc.AC[1]<=20)&(mt.variant_qc.AC[1]>=11)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC21to50=hl.agg.filter((mt.variant_qc.AC[1]<=50)&(mt.variant_qc.AC[1]>=21)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC51to100=hl.agg.filter((mt.variant_qc.AC[1]<=100)&(mt.variant_qc.AC[1]>=51)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_HC_LoF_AC101to200=hl.agg.filter((mt.variant_qc.AC[1]<=200)&(mt.variant_qc.AC[1]>=101)&(mt.LoF_worstCsq==True)&(mt.vep.transcript_consequences.lof.contains("HC")),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC1 = hl.agg.filter((mt.variant_qc.AC[1]==1)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC2 = hl.agg.filter((mt.variant_qc.AC[1]==2)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC3 = hl.agg.filter((mt.variant_qc.AC[1]==3)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC4=hl.agg.filter((mt.variant_qc.AC[1]==4)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC5=hl.agg.filter((mt.variant_qc.AC[1]==5)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC6to10=hl.agg.filter((mt.variant_qc.AC[1]<=10)&(mt.variant_qc.AC[1]>=6)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC11to20=hl.agg.filter((mt.variant_qc.AC[1]<=20)&(mt.variant_qc.AC[1]>=11)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC21to50=hl.agg.filter((mt.variant_qc.AC[1]<=50)&(mt.variant_qc.AC[1]>=21)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC51to100=hl.agg.filter((mt.variant_qc.AC[1]<=100)&(mt.variant_qc.AC[1]>=51)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_REVEL75_Miss_AC101to200=hl.agg.filter((mt.variant_qc.AC[1]<=200)&(mt.variant_qc.AC[1]>=101)&(mt.Revel_score>0.75)&(mt.Miss_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC1 = hl.agg.filter((mt.variant_qc.AC[1]==1)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC2 = hl.agg.filter((mt.variant_qc.AC[1]==2)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC3 = hl.agg.filter((mt.variant_qc.AC[1]==3)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC4=hl.agg.filter((mt.variant_qc.AC[1]==4)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC5=hl.agg.filter((mt.variant_qc.AC[1]==5)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC6to10=hl.agg.filter((mt.variant_qc.AC[1]<=10)&(mt.variant_qc.AC[1]>=6)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC11to20=hl.agg.filter((mt.variant_qc.AC[1]<=20)&(mt.variant_qc.AC[1]>=11)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC21to50=hl.agg.filter((mt.variant_qc.AC[1]<=50)&(mt.variant_qc.AC[1]>=21)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC51to100=hl.agg.filter((mt.variant_qc.AC[1]<=100)&(mt.variant_qc.AC[1]>=51)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())),
                        n_Syn_AC101to200=hl.agg.filter((mt.variant_qc.AC[1]<=200)&(mt.variant_qc.AC[1]>=101)&(mt.Syn_worstCsq==True),hl.agg.sum(mt.GT.n_alt_alleles())))


counts = mt.cols()
counts=counts.drop(counts.sample_qc)
counts.export('new/chr_'+sys.argv[1]'_'+gene_set+'_counts.tsv')
# SET UP HAIL
## Read in argument from bash script - this argument is the chromosome number.
import sys
print(sys.argv[0])
print('This is the 1st argument (chromosome): ' + sys.argv[1])

import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})
from hail import *
import hail.expr.functions

# READ IN GENOTYPE, SAMPLE AND VARIANT QCd MT
mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd.mt')
# Remove all samples removed from QC steps 
print(mt.count())
# Sex mismatching samples 
samples_to_keep=hl.import_table('/scratch/c.c1928239/new_builds/sex_imputation_ids_to_keep.tsv')
samples_to_keep=samples_to_keep.rename({'"to_keep_imputed_sex"':"s"})
samples_to_keep=samples_to_keep.key_by(samples_to_keep.s)
mt = mt.filter_cols((hl.is_defined(samples_to_keep[mt.s])))
print(mt.count())
# Samples removed through relatedness filtering 
to_rm=hl.import_table('/scratch/c.c1928239/new_builds/3rd_degree_rel_ids.tsv')  
to_rm=to_rm.rename({'"eid"':"s"})
to_rm=to_rm.key_by(to_rm.s)
mt = mt.filter_cols((hl.is_defined(to_rm[mt.s])), keep=False)
print(mt.count())




# ANNOTATE VARIANTS
## TopMed AC 
tm=hl.import_vcf('/scratch/c.c1928239/annotations/topmed/chr'+sys.argv[1]+'.TOPMed_freeze_8.all.vcf.gz', force_bgz=True, reference_genome='GRCh38')
tm=tm.select_rows(tm.info.AC)
tm=tm.rows()
mt=mt.annotate_rows(TopMed_AC=tm[mt.locus, mt.alleles].AC)   
mt=mt.annotate_rows(TopMed_count=hl.coalesce(mt.TopMed_AC, [0]))   
## MPC score 
mpc=hl.read_table('/scratch/c.c1928239/annotations/mpc.ht')
s=mt.alleles[1]
mt=mt.annotate_rows(alt=s)
mt=mt.key_rows_by(mt.locus, mt.alt)
a_mt=mt.annotate_rows(MPC_score=mpc[mt.locus, mt.alt].MPC_sc)
## GnomAD AC 
gn=hl.read_table('/scratch/c.c1928239/annotations/gnomad_exomes_controls_AC.ht/')
a_mt=a_mt.annotate_rows(gnomAD_exomes_controls_AC=gn[a_mt.locus, a_mt.alt].gnomAD_control_AC) 
a_mt=a_mt.annotate_rows(GnomAD_control_allele_count=hl.coalesce(a_mt.gnomAD_exomes_controls_AC, 0))  
## CADD score 
cadd=hl.read_table('/scratch/c.c1928239/annotations/CADD_phred_scores.ht/')    
a_mt=a_mt.annotate_rows(CADD_phred_score=cadd[a_mt.locus, a_mt.alt].CADD_phred) 
## Revel score
revel=hl.read_table('/scratch/c.c1928239/annotations/Revel_scores.ht')
a_mt=a_mt.annotate_rows(Revel_score=revel[a_mt.locus, a_mt.alt].REVEL_score)  
##Rekey
a_mt=a_mt.key_rows_by(a_mt.locus, a_mt.alleles)
mt=a_mt



#Recalculate variant QC metrics following removal of some samples
mt=hl.variant_qc(mt)
mt.checkpoint('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd_rmsexmismatch_rmrelated.mt', overwrite=True)
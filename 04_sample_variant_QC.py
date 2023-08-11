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

mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC.mt')

# VARIANT QC -- because here we work with each chromosome individually, variant QC metrics were exported to R where plots of variant QC metrics across all chromosomes could be viewed (see R_scripts/variant_QC.R ). Viewing these plots allowed for the selection of QC filters to apply.
mt=mt.filter_rows(mt.variant_qc.gq_stats.mean>40) 
print(mt.count())
mt=mt.filter_rows(mt.variant_qc.call_rate>0.9)
print(mt.count())
# For hail to read intervals, read in and write out as tsv
LCR=hl.import_table('intervals_LCRFromHengHg38.bed') 
LCR.export('LCR_intervals.tsv')   
intervals=hl.import_locus_intervals('/scratch/c.c1928239/annotations/LCR_intervals.tsv', reference_genome='GRCh38', skip_invalid_intervals=True)
mt=mt.annotate_rows(LCR=hl.is_defined(intervals[mt.locus]))  
mt=mt.filter_rows(mt.LCR==False)    
print(mt.count())



# SAMPLE QC -- because here we work with each chromosome individually, sample qc metrics had to be calculated across all chromosomes before selecting and applying cutoffs (see R_scripts/sample_QC.R ). This was done in R and a table of sample IDs to remove were written, which is read in here to filter out low quality samples. 
print(mt.count())
samples_to_keep=hl.import_table('/scratch/c.c1928239/new_builds/QC/sample_qc_keep.tsv')
samples_to_keep=samples_to_keep.rename({'"x"':"s"})
samples_to_keep=samples_to_keep.key_by(samples_to_keep.s)
mt = mt.filter_cols((hl.is_defined(samples_to_keep[mt.s])))
print(mt.count())

# Save out 
mt.checkpoint('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd.mt', overwrite=True)
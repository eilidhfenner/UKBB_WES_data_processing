import hail as hl 
# Set a different temp working directory with plenty of space 
hl.init(tmp_dir='/scratch/c.c1928239/tmp', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})
from hail import *
import hail.expr.functions


import sys
print(sys.argv[0])
print('This is the 1st argument (chromosome): ' + sys.argv[1])


# Before this script, put vcfs into 3 groups as shown below.
#mkdir b0
#mv *_b0_v1.vcf.bgz b0/
#mkdir b1_9
#mv *_b1_v1.vcf.gz b1_9/
#mv *_b2_v1.vcf.gz b1_9/
#mv *_b3_v1.vcf.gz b1_9/
#mv *_b4_v1.vcf.gz b1_9/
#mv *_b5_v1.vcf.gz b1_9/
#mv *_b6_v1.vcf.gz b1_9/
#mv *_b7_v1.vcf.gz b1_9/
#mv *_b8_v1.vcf.gz b1_9/
#mv *_b9_v1.vcf.gz b1_9/




# BUILD MATRIX TABLE
## Build matrix table from block pVCFs downloaded from UKBB. These blocks contain slightly different sample IDs due to samples requesting removal from the dataset. The mismatching samples are removed, vcfs rewritten, and then the vcfs from all blocks are read in to one matrix table.
b0=hl.import_vcf('b0/ukb23156*', force_bgz=True, reference_genome='GRCh38', array_elements_required=False)
b0_samples_to_remove = {'-000001', '-000002', '-000003', '-000004', '-000005', '-000006', '-000007', '-000008', '-000009', '-000010','-000011','-000012', '5538663', '5769145', '2181875', '2200627', '5028934', '5193618'}
b0_set_to_remove = hl.literal(b0_samples_to_remove)
b0_filtered=b0.filter_cols(~b0_set_to_remove.contains(b0['s']))
hl.export_vcf(b0_filtered, 'b0_filtered.vcf.bgz')

b1=hl.import_vcf('b1_9/ukb23156*', force_bgz=True, reference_genome='GRCh38', array_elements_required=False)
b1_samples_to_remove = {'-000001', '-000002', '-000003', '-000004', '-000005', '-000006', '-000007', '-000008', '-000009', '-000010','-000011','-000012', '-000013', '-000014', '-000015', '5538663', '5769145', '2200627'}
b1_set_to_remove = hl.literal(b1_samples_to_remove)
b1_filtered=b1.filter_cols(~b1_set_to_remove.contains(b1['s']))
hl.export_vcf(b1_filtered, 'b1_filtered.vcf.bgz')

b10=hl.import_vcf('ukb23156*', force_bgz=True, reference_genome='GRCh38', array_elements_required=False)
b10_samples_to_remove = {'-000001', '-000002', '-000003', '-000004', '-000005', '-000006', '-000007', '-000008', '-000009', '-000010','-000011','-000012', '-000013', '-000014', '-000015', '-000016', '-000017','-000018'}
b10_set_to_remove = hl.literal(b10_samples_to_remove)
b10_filtered=b10.filter_cols(~b10_set_to_remove.contains(b10['s']))
hl.export_vcf(b10_filtered, 'b10_filtered.vcf.bgz')

# Import three vcfs (now with all the same sample IDs) into one matrix table. 
mt=hl.import_vcf(['b0_filtered.vcf.bgz','b1_filtered.vcf.bgz', 'b10_filtered.vcf.bgz'],force_bgz=True, reference_genome='GRCh38', array_elements_required=False)
print(mt.describe())
print(mt.count())
# Can save at this stage using the below line, but this requires lots of space. 
# mt.checkpoint('whole_chr_'+sys.argv[1]+'.mt')




# SPLITTING MULTI-ALLELIC SITES
# Count original n of sites.
print('n original variants:')
print(mt.count_rows())
# Remove sites labelled as 'monoallelic'. This is defined as
mt = mt.filter_rows(hl.is_missing(mt.filters))
print('n variants following removal of those labelled as monoallelic:')
print(mt.count_rows())
# Before splitting multi-allelic sites, remove sites with >6 alleles
mt = mt.filter_rows(mt.alleles.length() <= 6)
print('n variants following removal of those with more than 6 alleles:')
print(mt.count_rows())
# Split multi-allelic sites
mt = hl.split_multi_hts(mt)
print('n variants following splitting of multiallelic sites:')
print(mt.count_rows())
# Can save at this stage using the below line, but this requires lots of space. 
#mt.checkpoint('whole_chr_'+sys.argv[1]+'.mt', overwrite=True)



# GENOTYPE QC
# Calculate original sample and variant QC metrics and write out for visualisation in R
mt=hl.sample_qc(mt)
mt=hl.variant_qc(mt)
sample_qc=mt.cols()
sample_qc.export('pre_sample_qc.csv', delimiter=',')
var_qc=mt.rows()
var_qc=var_qc.select(var_qc.variant_qc)
var_qc.export('pre_var_qc.csv', delimiter=',')

# Run genotype quality control
# Create allele balance variable
ab=mt.AD[1]/hl.sum(mt.AD)
# Below removing: genotypes listed as homozygous reference but with >10 alternate allele reads | genotypes listed as homozgyous without a reference:alternate of ~1:1 | and genotypes listed as homozygous alternate with over 10% reference reads
filter_condition_ab=((mt.GT.is_hom_ref() & (ab <= 0.1)) | (mt.GT.is_het() & (ab >= 0.25) & (ab <= 0.75)) | (mt.GT.is_hom_var() & (ab >= 0.9)))
mt=mt.filter_entries(filter_condition_ab)
# Remove entries with depth < 10
mt=mt.filter_entries(mt.DP > 10)
# Remove entries with a GQ < 30
mt=mt.filter_entries(mt.GQ > 30)

# Remove any variants with no alleles left following genotype QC
mt = hl.variant_qc(mt)
mt = mt.filter_rows((mt.variant_qc.AF[0] == 0.0) | (mt.variant_qc.AF[0] == 1.0), keep = False)
print('n variants following genotype QC and removal of non-variant rows')
print(mt.count_rows())


# Recalculate sample and variant QC metrics
# As each matrix table is just for one chromosome (due to size requirements), sample QC is currently just for this chromosome - have to read in from all chromosomes and calculate overall sample QC 
mt=hl.sample_qc(mt)
sample_qc=mt.cols()
sample_qc.export('postgeno_sample_qc.csv', delimiter=",")
mt=hl.variant_qc(mt)
var_qc=mt.variant_qc
var_qc.export('postgeno_var_qc.csv', delimiter=",")

# Drop non-genotype entries and save out
mt= mt.select_entries(mt.GT)
# Saving here and not above means less storage is required, as not all entries are in this matrix table. 
mt.checkpoint('chr_'+sys.argv[1]+'split_genoQC.mt', overwrite=True) 
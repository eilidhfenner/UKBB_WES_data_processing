# SET UP HAIL
## Read in argument from bash script - this argument is the chromosome number.
import sys
print(sys.argv[0])
print('This is the 1st argument (chromosome): ' + sys.argv[1])

import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp/', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})


from hail import *
import hail.expr.functions

# Read in QCd matrix table 
mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd.mt')


## import high quality pruned variants
ht_pruned_variants = hl.import_table('PLINK_FILES_chr_'+sys.argv[1]+'_pruned.prune.in', no_header=True)
ht_pruned_variants = ht_pruned_variants.annotate(**hl.parse_variant(ht_pruned_variants.f0, reference_genome='GRCh38'))
ht_pruned_variants = ht_pruned_variants.key_by(ht_pruned_variants.locus, ht_pruned_variants.alleles)

## keep pruned ht_pruned_variants
mt = mt.filter_rows(hl.is_defined(ht_pruned_variants[mt.row_key]))
print(mt.count())

# Save pruned variant table 
mt.write('chr_'+sys.argv[1]+'pruned_variants.mt', overwrite=True)


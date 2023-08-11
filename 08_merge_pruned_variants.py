import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp/', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})


from hail import *
import hail.expr.functions

chr1=hl.read_matrix_table('chr_1/chr_1pruned_variants.mt/')
chr2=hl.read_matrix_table('chr_2/chr_2pruned_variants.mt/')
chr3=hl.read_matrix_table('chr_3/chr_3pruned_variants.mt/')
chr4=hl.read_matrix_table('chr_4/chr_4pruned_variants.mt/')
chr5=hl.read_matrix_table('chr_5/chr_5pruned_variants.mt/')
chr6=hl.read_matrix_table('chr_6/chr_6pruned_variants.mt/')
chr7=hl.read_matrix_table('chr_7/chr_7pruned_variants.mt/')
chr8=hl.read_matrix_table('chr_8/chr_8pruned_variants.mt/')
chr9=hl.read_matrix_table('chr_9/chr_9pruned_variants.mt/')
chr10=hl.read_matrix_table('chr_10/chr_10pruned_variants.mt/')
chr11=hl.read_matrix_table('chr_11/chr_11pruned_variants.mt/')
chr12=hl.read_matrix_table('chr_12/chr_12pruned_variants.mt/')
chr13=hl.read_matrix_table('chr_13/chr_13pruned_variants.mt/')
chr14=hl.read_matrix_table('chr_14/chr_14pruned_variants.mt/')
chr15=hl.read_matrix_table('chr_15/chr_15pruned_variants.mt/')
chr16=hl.read_matrix_table('chr_16/chr_16pruned_variants.mt/')
chr17=hl.read_matrix_table('chr_17/chr_17pruned_variants.mt/')
chr18=hl.read_matrix_table('chr_18/chr_18pruned_variants.mt/')
chr19=hl.read_matrix_table('chr_19/chr_19pruned_variants.mt/')
chr20=hl.read_matrix_table('chr_20/chr_20pruned_variants.mt')
chr21=hl.read_matrix_table('chr_21/chr_21pruned_variants.mt')
chr22=hl.read_matrix_table('chr_22/chr_22pruned_variants.mt')
chr23=hl.read_matrix_table('chr_23/chr_23pruned_variants.mt')
chr24=hl.read_matrix_table('chr_24/chr_24pruned_variants.mt')

pruned_autosomes = chr1.union_rows(chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10, chr11, chr12, chr13, chr14, chr15, chr16, chr17, chr18, chr19, chr20, chr21, chr22)
pruned_autosomes.repartition(200)
pruned_autosomes.checkpoint('pruned_autosomes.mt')

pruned_all_chr = pruned_autosomes.union_rows(chr23, chr24)
pruned_all_chr.repartition(200)
pruned_all_chr.checkpoint('pruned_all_chr.mt')

## Rewrite merged pruned autosomes to plink 
hl.export_plink(pruned_autosomes, 'pruned_PLINK_')

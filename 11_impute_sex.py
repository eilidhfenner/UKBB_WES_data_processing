# SET UP HAIL
import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp/', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})


from hail import *
import hail.expr.functions

# Read in X chromosome and filter to high quality, common variants
mt=hl.read_matrix_table('chr_23/chr_23split_genoQC.mt/') 
# Filter out all variants with a call rate below .97
mt=mt.filter_rows(mt.variant_qc.call_rate>=.97)    
print(mt.count())
# Filter out any variants with a MAF of <.01
mt=mt.filter_rows((mt.variant_qc.AF[1]>.01) & (mt.variant_qc.AF[1]<.99))
print(mt.count())

# Impute sex and write imputed table as a hail table and tsv. The tsv is further analysed in `06_imputed_sex.R`
imputed=hl.impute_sex(mt.GT)
imputed.write('imputed_sex.ht', overwrite=True)
imputed.export('imputed_sex.tsv')

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
import bokeh
from bokeh.io import show, output_notebook
from bokeh.layouts import gridplot
from bokeh.io import export_png
from bokeh.plotting import figure, output_file, save

# READ IN GENOTYPE, SAMPLE AND VARIANT QCd MT
mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd.mt')

# EXPORT COMMON, HIGH QUALITY VARIANTS TO PLINK 
mt=mt.filter_rows(mt.variant_qc.p_value_hwe > 0.00000001)

# Select common variants
common_vars = (mt.filter_rows((mt.variant_qc.AF[0] > 0.01) &
                              (mt.variant_qc.AF[0] < 0.99) &
                              ((mt.variant_qc.call_rate > 0.98))
                              ).persist()
              )

print(common_vars.count())

hl.export_plink(common_vars, 'PLINK_FILES_chr_'+sys.argv[1])


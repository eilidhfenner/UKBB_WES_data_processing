import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp/', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})


from hail import *
import hail.expr.functions

# Read in pruned, high quality variants from autosomes and then run Hardy Weinberg normalised PCA. 
mt=hl.read_matrix_table('pruned_autosomes.mt')
print(mt.count())
eigenvalues, pcs, _ = hl.hwe_normalized_pca(mt.GT)

# Format table and then write out PCAs
pcs = pcs.annotate(PC1 = pcs.scores[0],
        PC2 = pcs.scores[1], PC3 = pcs.scores[2],
        PC4 = pcs.scores[3], PC5 = pcs.scores[4],
        PC6 = pcs.scores[5], PC7 = pcs.scores[6],
        PC8 = pcs.scores[7], PC9 = pcs.scores[8],
        PC10 = pcs.scores[9])
pcs.flatten().export('PCAs.tsv',delimiter = "\t")
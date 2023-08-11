## Read in argument from bash script - this argument is the chromosome number.
import sys
print(sys.argv[0])
print('This is the 1st argument (chromosome): ' + sys.argv[1])


import hail as hl
hl.init(tmp_dir='/scratch/c.c1928239/tmp/', spark_conf={
    "spark.executor.extraClassPath": "/usr/lib64/libblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/liblapack.so:/usr/lib64/libgslcblas.so:/usr/lib64/atlas/libsatlas.so.3"})

# Annotate with VEP 
mt=hl.read_matrix_table('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd_rmsexmismatch_rmrelated.mt')
mt = hl.vep(mt, "/scratch/c.c1928239/annotations/vep-config_loftee.json")


# Set up annotations
PTV_annotations = hl.set(["splice_acceptor_variant", "splice_donor_variant", "stop_gained", "frameshift_variant"])
NS_annotations = hl.set(["splice_acceptor_variant", "splice_donor_variant", "stop_gained", "inframe_insertion", "inframe_deletion", "inframe_insertion", "missense_variant", "stop_lost", "start_lost", "frameshift_variant"])
Miss_annotations = hl.set(["missense_variant"])
S_annotations = hl.set(["synonymous_variant"])
# Annotate
mt = mt.annotate_rows(LoF_worstCsq = (PTV_annotations.contains(mt.vep.most_severe_consequence)),
                          NS_worstCsq = (NS_annotations.contains(mt.vep.most_severe_consequence)),
                          Miss_worstCsq = (Miss_annotations.contains(mt.vep.most_severe_consequence)),
                          Syn_worstCsq = (S_annotations.contains(mt.vep.most_severe_consequence)),
                          gene_symbol_worstCsq = (mt.vep.transcript_consequences.find(lambda x : x.consequence_terms.contains(mt.vep.most_severe_consequence)).gene_symbol),
                          gene_id_worstCsq = (mt.vep.transcript_consequences.find(lambda x : x.consequence_terms.contains(mt.vep.most_severe_consequence)).gene_id)
                         )

mt.checkpoint('chr_'+sys.argv[1]+'split_genoQC_sample_var_QCd_rmsexmismatch_rmrelated_annotated.mt', overwrite=True)
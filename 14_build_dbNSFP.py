import hail as hl
hl.init()

# Read dbNSFP table (downloaded from dbNSFP site) into hail
db=hl.import_table('/scratch/c.c1928239/ref/dbNSFP4.1a_grch38.gz', force_bgz=True)
# Rename some columns
db=db.rename({'pos(1-based)':'pos'})
db=db.rename({'#chr':'chr'})
# Make a 'locus' column in the correct format for annotation with mt
db=db.annotate(locus='chr'+db.chr+':'+db.pos)
db=db.annotate(alt=db.alt)
# Select the columns you want (choose your annotations)
db=db.select(db.locus, db.alleles, db.alt, db.CADD_phred, db.CADD_raw, db.CADD_raw_rankscore, \
db.MPC_rankscore, db.MPC_score, db.REVEL_rankscore, db.REVEL_score, db.gnomAD_exomes_flag, \
db.gnomAD_exomes_AC, db.gnomAD_exomes_AN, db.gnomAD_exomes_AF, db.gnomAD_exomes_nhomalt, \
db.gnomAD_exomes_controls_AC, db.gnomAD_exomes_controls_AN, db.gnomAD_exomes_controls_AF, \
db.gnomAD_exomes_controls_nhomalt, db.clinvar_id, db.clinvar_clnsig, db.clinvar_trait, \
db.clinvar_review, db.clinvar_hgvs, db.clinvar_var_source, db.clinvar_MedGen_id, \
db.clinvar_OMIM_id, db.clinvar_Orphanet_id)
# Replace '.' in db with NaN so hail will be able to read and check it has worked
dba=db.annotate(REVEL_rankscore=db.REVEL_rankscore.replace("(?<!\d)\.", "NaN"))
dba=dba.annotate(CADD_phred=dba.CADD_phred.replace("(?<!\d)\.", "NaN"))
dba=dba.annotate(CADD_raw=dba.CADD_raw.replace("(?<!\d)\.", "NaN"))
dba=dba.annotate(CADD_raw_rankscore=dba.CADD_raw_rankscore.replace("(?<!\d)\.", "NaN"))
dba=dba.annotate(REVEL_score=dba.REVEL_score.replace("(?<!\d)\.", "NaN"))
dba.show(10)
# Save out this table, and then read back in, specifying correct schema for each column (schema for dbNSFP can be found here )
dba.export('narray_dbNSFP.tsv')
db=hl.import_table('narray_dbNSFP.tsv', types={'CADD_phred': hl.tfloat64,'CADD_raw':hl.tfloat64,'CADD_raw_rankscore':hl.tfloat64, 'MPC_rankscore': hl.tstr,'MPC_score': hhl.tstr,'REVEL_rankscore':hl.tfloat64,'REVEL_score': hl.tfloat64,'locus':hl.expr.types.tlocus(reference_genome='GRCh38'), 'alleles':hl.dtype('array<str>')})
# Key your db by locus and allele
db=db.key_by(db.locus, db.alt)
# Save as hail table
db.checkpoint('dbNSFP_annotations.ht')
print('dbNSFP table written')

# MPC score 
ht=db
s=ht.select(ht.MPC_score)
s=s.annotate(new=s.MPC_score.replace("(?<!\d)\.|\.(?!\d)",""))
s=s.annotate(MPC=s.new.replace(";",""))
s1=s.filter(s.MPC!="")
s2=s1.annotate(MPC_sc=s1.MPC.replace("^(.{7}).+", "$1"))
s2=s2.drop(s2.MPC_score)
s2=s2.drop(s2.new)
s2=s2.drop(s2.MPC)
s2.export('MPC.tsv')
mpc=hl.import_table('MPC.tsv', types={'MPC_sc': hl.tfloat64, 'locus':hl.expr.types.tlocus(reference_genome='GRCh38'), 'alleles':hl.dtype('array<str>')})
mpc=mpc.key_by(mpc.locus, mpc.alt)
mpc.write('mpc.ht')

# Gnomad AC 
s=ht.select(ht.gnomAD_exomes_controls_AC) 
s=s.annotate(gnomAD_control_AC=s.gnomAD_exomes_controls_AC.replace("(?<!\d)\.|\.(?!\d)",""))
s=s.filter(s.gnomAD_control_AC!="")
s=s.drop(s.gnomAD_exomes_controls_AC)
s.export('gnomad_controls_AC.tsv')
gn=hl.import_table('gnomad_controls_AC.tsv', types={'gnomAD_control_AC':hl.tfloat64, 'locus':hl.expr.types.tlocus(reference_genome='GRCh38'), 'alleles':hl.dtype('array<str>')}) 
gn=gn.key_by(gn.locus, gn.alt)  
gn.write('gnomad_exomes_controls_AC.ht')

# CADD score 
s=ht.select(ht.CADD_phred) 
s.write('CADD_phred_scores.ht')

# Revel score 
s=ht.select(ht.REVEL_score)
s.write('Revel_scores.ht')


# Constraint
const=hl.import_table('/scratch/c.c1928239/annotations/gnomad.v2.1.1.lof_metrics.tsv')                                    
c=const.select(const.gene_id, const.pLI, const.oe_lof, const.oe_lof_upper)   
c.export('gnomad_constraint_metrics.tsv')    
c=hl.import_table('gnomad_constraint_metrics.tsv', types={'pLI': hl.tfloat64, 'oe_lof':hl.tfloat64, 'oe_lof_upper':hl.tfloat64})
c=c.annotate(pli_9=hl.if_else(c.pLI>=0.9, True, False)) 
c=c.annotate(loeuf_35=hl.if_else(c.oe_lof_upper<0.35, True, False))    
c=c.key_by(c.gene_id)
c.write('gnomad_LoF_annotations.ht')    




# Constrained genes
## pLI 
const=hl.import_table('/scratch/c.c1928239/annotations/gnomad.v2.1.1.lof_metrics.tsv')                                    
c=const.select(const.gene_id, const.pLI, const.oe_lof, const.oe_lof_upper)   
c.export('gnomad_constraint_metrics.tsv')    
c=hl.import_table('gnomad_constraint_metrics.tsv', types={'pLI': hl.tfloat64, 'oe_lof':hl.tfloat64, 'oe_lof_upper':hl.tfloat64})
c=c.annotate(pli_9=hl.if_else(c.pLI>=0.9, True, False)) 
c=c.annotate(loeuf_35=hl.if_else(c.oe_lof_upper<0.35, True, False))    
c=c.key_by(c.gene_id)
c.write('gnomad_LoF_annotations.ht')  

## LOEUF score 
mt=hl.import_table('obs_exp_lof_deciles.csv', delimiter=',', types={'decile':hl.tfloat64})   
mt=mt.key_by(mt.gene_id)   
mt.write('obs_exp_deciles.ht')  

# Common allele loci
## All prioritised 
pgc3=hl.import_table('/scratch/c.c1928239/annotations/gene_sets/PGC3/PGC3_all.csv')                                                    
pgc3=pgc3.annotate(GWAS_all=True)
pgc3=pgc3.key_by(pgc3.id)
pgc3.write('/scratch/c.c1928239/annotations/gene_sets/PGC3_all.ht')

## Closest to index SNP 
pgc3=hl.import_table('/scratch/c.c1928239/annotations/gene_sets/PGC3/PGC3_closest.csv')                                                    
pgc3=pgc3.annotate(GWAS_closest=True)
pgc3=pgc3.key_by(pgc3.id)
pgc3.write('/scratch/c.c1928239/annotations/gene_sets/PGC3_closest.ht')

## All prioritised 
pgc3=hl.import_table('/scratch/c.c1928239/annotations/gene_sets/PGC3/PGC3_all_prioritised.csv')                                                    
pgc3=pgc3.annotate(prioritised_all=True)
pgc3=pgc3.key_by(pgc3.id)
pgc3.write('/scratch/c.c1928239/annotations/gene_sets/PGC3_all_prioritised.ht')

## Finemap prioritised 
pgc3=hl.import_table('/scratch/c.c1928239/annotations/gene_sets/PGC3/PGC3_finemap_prioritised.csv')
pgc3=pgc3.rename({'\ufeffid':'id'})                                                                  
pgc3=pgc3.annotate(prioritised_finemap=True)
pgc3=pgc3.key_by(pgc3.id)
pgc3.write('/scratch/c.c1928239/annotations/gene_sets/PGC3_finemap_prioritised.ht')

## SMR prioritised
pgc3=hl.import_table('/scratch/c.c1928239/annotations/gene_sets/PGC3/PGC3_SMR_prioritised.csv') 
pgc3=pgc3.rename({'\ufeffid':'id'})                                                                  
pgc3=pgc3.annotate(prioritised_SMR=True)
pgc3=pgc3.key_by(pgc3.id)
pgc3.write('/scratch/c.c1928239/annotations/gene_sets/PGC3_SMR_prioritised.ht')

# Brain expressed genes 
br=hl.import_table('brain_expressed.csv', delimiter=',', types={' fpkm':hl.tfloat64})    
br=br.annotate(Brain_expressed=True)
br=br.key_by(br.ID)
br.write('Brain_expressed_annotations.ht')

# RCV enriched (SCHEMA) genes
s=hl.import_table('SCHEMA_gene_results.tsv.bgz', types={'P meta': hl.tfloat64})
s=s.rename({'P meta':'p_meta'}) 
s=s.annotate(Schema_FDR_5=hl.if_else(s.p_meta<=8.23e-05, True, False))
s=s.annotate(Schema_GWS=hl.if_else(s.p_meta<=2.2e-06, True, False))
s=s.select(s.gene_id, s.Schema_FDR_5, s.Schema_GWS)
s=s.key_by(s.gene_id) 
s.write('Schema_annotations.ht') 


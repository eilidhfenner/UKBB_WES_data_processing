library(ukbtools)

# Read in tables 
## Kinshp matrix 
array_rel=read.delim('Relatedness.dat')
## Samples with WES data that passed QC 
samples=read.csv("IDs_post_sample_qc.tsv", header=T)

# Filter link file to my samples 
sample=merge(samples, array_rel, by.x='s',by.y='eid')

# Randomly remove up to third degree relations
to_rm=ukb_gen_samples_to_remove(array_rel,s, cutoff = 0.0442)
rm3rd <- as.data.table(to_rm)
rm=merge(rm3rd, link_ids, by.x='to_rm',by.y='app14421')
rm=rm[,c('eid_13310')]
write.table(rm, '3rd_degree_rel_ids.tsv', row.names=F)
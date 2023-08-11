#Set up libraries and working directory 
## Load in libraries
library(dplyr)
library(ggplot2)
library(reshape2)
library(janitor)
library(tibble)
library(tidyverse)
library(ggplot2)
library(ggpubr)
library(vioplot)
setwd("path/to/QC_metrics/")

# Read in post genotype QC sample QC metrics and reformat. Repeat the below script for each chromosome and save as 'chr...'
## Chr 1 
s <- read.csv("chr_1/postgeno_sample_qc.csv", header=FALSE)
#Remove row 1
s <- s[-1,]
#Select cols you want
s = s %>% select(V1, V2, V6, V10, V25:V27)
# Reformat columns so just numbers remain
s$V1 <- sub("^.*:", "", s$V1, perl=TRUE)
s$V2 <- sub("^.*:", "", s$V2, perl=TRUE)
s$V6 <- sub("^.*:", "", s$V6, perl=TRUE)
s$V10 <- sub("^.*:", "", s$V10, perl=TRUE)
s$V25 <- sub("^.*:", "", s$V25, perl=TRUE)
s$V26 <- sub("^.*:", "", s$V26, perl=TRUE)
s$V27 <- sub("^.*:", "", s$V27, perl=TRUE)
s$V27 = substr(s$V27,1,nchar(s$V27)-1)
# Rename cols
names(s)[names(s) == "V1"] <- "sample_id"
names(s)[names(s) == "V2"] <- "Dp_stats_mean_1"
names(s)[names(s) == "V6"] <- "GQ_stats_mean_1"
names(s)[names(s) == "V10"] <- "Call_rate_1"
names(s)[names(s) == "V25"] <- "Ti_Tv_1"
names(s)[names(s) == "V26"] <- "Het_Hom_1"
names(s)[names(s) == "V27"] <- "Ins_Del_1"
#Write as chr1
chr1 <- s

# Once sample QC metrics are reformatted for each chromosome, merge into one dataframe and reformat all values to be numeric
## Merge
s <- merge(chr1, chr2, by = 'sample_id')
s<- merge(s, chr3, by = 'sample_id')
s<- merge(s, chr4, by = 'sample_id')          
s<- merge(s, chr5, by = 'sample_id')  
s<- merge(s, chr6, by = 'sample_id')  
s<- merge(s, chr7, by = 'sample_id')  
s<- merge(s, chr8, by = 'sample_id') 
s<- merge(s, chr9, by = 'sample_id')  
s<- merge(s, chr10, by = 'sample_id')  
s<- merge(s, chr11, by = 'sample_id')  
s<- merge(s, chr12, by = 'sample_id')  
s<- merge(s, chr13, by = 'sample_id')  
s<- merge(s, chr14, by = 'sample_id')  
s<- merge(s, chr15, by = 'sample_id')  
s<- merge(s, chr16, by = 'sample_id')  
s<- merge(s, chr17, by = 'sample_id')  
s<- merge(s, chr18, by = 'sample_id')  
s<- merge(s, chr19, by = 'sample_id')  
s<- merge(s, chr20, by = 'sample_id')  
s<- merge(s, chr21, by = 'sample_id')  
s<- merge(s, chr22, by = 'sample_id')  
s<- merge(s, chrx, by = 'sample_id')  
s<- merge(s, chry, by = 'sample_id')  
s = s %>% mutate_if(is.character,as.numeric)

# Calculate QC metrics per sample across all chromosomes. Do this by multiplying each mean by the number of variants it represents, then divide by total variants to get an overall mean per sample across all chromosomes. This can also be repeated for other metrics such as Ti:Tv, Het:Hom and Insertion:Deletion ratios. 
## Mean depth per sample
s$dp_total_1 <- (s$Dp_stats_mean_1*1641404)
s$dp_total_2 <- (s$Dp_stats_mean_2*1191444)
s$dp_total_3 <- (s$Dp_stats_mean_3*950743)
s$dp_total_4 <- (s$Dp_stats_mean_4*646847)
s$dp_total_5 <- (s$Dp_stats_mean_5*719514)
s$dp_total_6 <- (s$Dp_stats_mean_6*808581)
s$dp_total_7 <- (s$Dp_stats_mean_7*783576)
s$dp_total_8 <- (s$Dp_stats_mean_8*598025)
s$dp_total_9 <- (s$Dp_stats_mean_9*709200)
s$dp_total_10 <- (s$Dp_stats_mean_10*666445)
s$dp_total_11<- (s$Dp_stats_mean_11*985389)
s$dp_total_12<- (s$Dp_stats_mean_12*869575)
s$dp_total_13<- (s$Dp_stats_mean_13*290339)
s$dp_total_14<- (s$Dp_stats_mean_14*511466)
s$dp_total_15<- (s$Dp_stats_mean_15*564767)
s$dp_total_16<- (s$Dp_stats_mean_16*812416)
s$dp_total_17<- (s$Dp_stats_mean_17*975889)
s$dp_total_18<- (s$Dp_stats_mean_18*260705)
s$dp_total_19<- (s$Dp_stats_mean_19*1139792)
s$dp_total_20<- (s$Dp_stats_mean_20*427878)
s$dp_total_21<- (s$Dp_stats_mean_21*179086)
s$dp_total_22<- (s$Dp_stats_mean_22*386611)
s$dp_total_x<- (s$Dp_stats_mean_x*323534)
s$dp_total_y<- (s$Dp_stats_mean_y*223)
##Sum all together and then divide by total n variants to get mean. 
s$total_dps = rowSums(s[,c('dp_total_1', 'dp_total_2','dp_total_3','dp_total_4','dp_total_5','dp_total_6','dp_total_7','dp_total_8','dp_total_9','dp_total_10','dp_total_11','dp_total_12','dp_total_13','dp_total_14','dp_total_15','dp_total_16','dp_total_17','dp_total_18','dp_total_19','dp_total_20','dp_total_21','dp_total_22','dp_total_x', 'dp_total_y')])
s$mean_dp=(s$total_dps/16443449)
# Plot mean depth per sample 
ggplot(s, aes(mean_dp))+
  geom_freqpoly(bins=100)+
  ggtitle('Mean depth per sample')+
  xlab('Mean sequencing depth')

# Mean GQ per sample
s$GQ_total_1 <- (s$GQ_stats_mean_1*1641404)
s$GQ_total_2 <- (s$GQ_stats_mean_2*1191444)
s$GQ_total_3 <- (s$GQ_stats_mean_3*950743)
s$GQ_total_4 <- (s$GQ_stats_mean_4*646847)
s$GQ_total_5 <- (s$GQ_stats_mean_5*719514)
s$GQ_total_6 <- (s$GQ_stats_mean_6*808581)
s$GQ_total_7 <- (s$GQ_stats_mean_7*783576)
s$GQ_total_8 <- (s$GQ_stats_mean_8*598025)
s$GQ_total_9 <- (s$GQ_stats_mean_9*709200)
s$GQ_total_10 <- (s$GQ_stats_mean_10*666445)
s$GQ_total_11<- (s$GQ_stats_mean_11*985389)
s$GQ_total_12<- (s$GQ_stats_mean_12*869575)
s$GQ_total_13<- (s$GQ_stats_mean_13*290339)
s$GQ_total_14<- (s$GQ_stats_mean_14*511466)
s$GQ_total_15<- (s$GQ_stats_mean_15*564767)
s$GQ_total_16<- (s$GQ_stats_mean_16*812416)
s$GQ_total_17<- (s$GQ_stats_mean_17*975889)
s$GQ_total_18<- (s$GQ_stats_mean_18*260705)
s$GQ_total_19<- (s$GQ_stats_mean_19*1139792)
s$GQ_total_20<- (s$GQ_stats_mean_20*427878)
s$GQ_total_21<- (s$GQ_stats_mean_21*179086)
s$GQ_total_22<- (s$GQ_stats_mean_22*386611)
s$GQ_total_x<- (s$GQ_stats_mean_x*323534)
s$GQ_total_y<- (s$GQ_stats_mean_y*223)
##Sum all GQ together and divide by total variants
s$total_GQs = rowSums(s[,c('GQ_total_1', 'GQ_total_2','GQ_total_3','GQ_total_4','GQ_total_5','GQ_total_6','GQ_total_7','GQ_total_8','GQ_total_9','GQ_total_10','GQ_total_11','GQ_total_12','GQ_total_13','GQ_total_14','GQ_total_15','GQ_total_16','GQ_total_17','GQ_total_18','GQ_total_19','GQ_total_20','GQ_total_21','GQ_total_22','GQ_total_x', 'GQ_total_y')])
s$mean_GQ=(s$total_GQs/16443449)
# Plot 
ggplot(s, aes(mean_GQ))+
  geom_freqpoly(bins=100)+
  ggtitle('Mean genotype quality per sample')+
  xlab('Mean genotype quality')

# Mean call rate per sample
s$Call_rate_total_1 <- (s$Call_rate_1*1641404)
s$Call_rate_total_2 <- (s$Call_rate_2*1191444)
s$Call_rate_total_3 <- (s$Call_rate_3*950743)
s$Call_rate_total_4 <- (s$Call_rate_4*646847)
s$Call_rate_total_5 <- (s$Call_rate_5*719514)
s$Call_rate_total_6 <- (s$Call_rate_6*808581)
s$Call_rate_total_7 <- (s$Call_rate_7*783576)
s$Call_rate_total_8 <- (s$Call_rate_8*598025)
s$Call_rate_total_9 <- (s$Call_rate_9*709200)
s$Call_rate_total_10 <- (s$Call_rate_10*666445)
s$Call_rate_total_11<- (s$Call_rate_11*985389)
s$Call_rate_total_12<- (s$Call_rate_12*869575)
s$Call_rate_total_13<- (s$Call_rate_13*290339)
s$Call_rate_total_14<- (s$Call_rate_14*511466)
s$Call_rate_total_15<- (s$Call_rate_15*564767)
s$Call_rate_total_16<- (s$Call_rate_16*812416)
s$Call_rate_total_17<- (s$Call_rate_17*975889)
s$Call_rate_total_18<- (s$Call_rate_18*260705)
s$Call_rate_total_19<- (s$Call_rate_19*1139792)
s$Call_rate_total_20<- (s$Call_rate_20*427878)
s$Call_rate_total_21<- (s$Call_rate_21*179086)
s$Call_rate_total_22<- (s$Call_rate_22*386611)
s$Call_rate_total_x<- (s$Call_rate_x*323534)
s$Call_rate_total_y<- (s$Call_rate_y*223)

## Sum all Call_rate together and divide by total n variants
s$total_Call_rates = rowSums(s[,c('Call_rate_total_1', 'Call_rate_total_2','Call_rate_total_3','Call_rate_total_4','Call_rate_total_5','Call_rate_total_6','Call_rate_total_7','Call_rate_total_8','Call_rate_total_9','Call_rate_total_10','Call_rate_total_11','Call_rate_total_12','Call_rate_total_13','Call_rate_total_14','Call_rate_total_15','Call_rate_total_16','Call_rate_total_17','Call_rate_total_18','Call_rate_total_19','Call_rate_total_20','Call_rate_total_21','Call_rate_total_22','Call_rate_total_x')])
s$mean_Call_rate=(s$total_Call_rates/16443449)

# Plot and add line where cut-off will be applied.
ggplot(s, aes(mean_Call_rate))+
  geom_freqpoly(bins=100)+
  ggtitle('Mean call rate per sample')+
  xlab('Mean call rate')+
  geom_vline(xintercept = 0.8, colour='red')

# Save table of means, apply cutoffs and save out a table of samples to keep
sample_qc_means=s[,c('sample_id','mean_Call_rate','mean_GQ', 'mean_dp', 'mean_Ins_Del', 'mean_Ti_Tv', 'mean_Het_Hom')] 
write.csv(sample_qc_means, 'sample_qc_means.csv', row.names = F)
high_CR=subset(s, s$mean_Call_rate >= 0.8)
samples_to_keep=high_CR$sample_id
write.table(samples_to_keep, 'sample_qc_keep.tsv', row.names = FALSE)

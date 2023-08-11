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

# Read in post genotype QC variant QC metrics and reformat. Repeat the below script for each chromosome and save as 'chr...'
# chr_1
s <- read.csv("chr_1/postgeno_var_qc.csv", header=FALSE)
#Remove row 1
s <- s[-1,]
# Reformat so only values remain
s$V2 <- gsub("\\[|\\]", "", s$V2)
s$V3 <- gsub("\\[|\\]", "", s$V3)
s$V4 <- sub("^.*:", "", s$V4, perl=TRUE)
s$V5 <- sub("^.*:", "", s$V5, perl=TRUE)
s$V6 <- sub("^.*:", "", s$V6, perl=TRUE)
s$V7 <- sub("^.*:", "", s$V7, perl=TRUE)
s$V7 = substr(s$V7,1,nchar(s$V7)-1)
s$V8 <- sub("^.*:", "", s$V8, perl=TRUE)
s$V9 <- sub("^.*:", "", s$V9, perl=TRUE)
s$V10 <- sub("^.*:", "", s$V10, perl=TRUE)
s$V11 <- sub("^.*:", "", s$V11, perl=TRUE)
s$V11 = substr(s$V11,1,nchar(s$V11)-1)
s$V12 <- sub("^.*:", "", s$V12, perl=TRUE)
s$V12 <- gsub("\\[|\\]", "", s$V12)
s$V13 <- gsub("\\[|\\]", "", s$V13)
s$V14 <- sub("^.*:", "", s$V14, perl=TRUE)
s$V14 <- gsub("\\[|\\]", "", s$V14)
s$V15 <- gsub("\\[|\\]", "", s$V15)
s$V16 <- sub("^.*:", "", s$V16, perl=TRUE)
s$V17 <- sub("^.*:", "", s$V17, perl=TRUE)
s$V17 <- gsub("\\[|\\]", "", s$V17)
s$V18 <- gsub("\\[|\\]", "", s$V18)
s$V19 <- sub("^.*:", "", s$V19, perl=TRUE)
s$V20 <- sub("^.*:", "", s$V20, perl=TRUE)
s$V21 <- sub("^.*:", "", s$V21, perl=TRUE)
s$V22 <- sub("^.*:", "", s$V22, perl=TRUE)
s$V23 <- sub("^.*:", "", s$V23, perl=TRUE)
s$V24 <- sub("^.*:", "", s$V24, perl=TRUE)
s$V25 <- sub("^.*:", "", s$V25, perl=TRUE)
s$V26 <- sub("^.*:", "", s$V26, perl=TRUE)
s$V26 = substr(s$V26,1,nchar(s$V26)-1)
# Rename cols
names(s)[names(s) == "V1"] <- "Locus"
names(s)[names(s) == "V2"] <- "Ref_allele"
names(s)[names(s) == "V3"] <- "Alternate_allele"
names(s)[names(s) == "V4"] <- "Dp_stats_mean"
names(s)[names(s) == "V5"] <- "Dp_stats_stdev"
names(s)[names(s) == "V6"] <- "Dp_stats_min"
names(s)[names(s) == "V7"] <- "Dp_stats_max"
names(s)[names(s) == "V8"] <- "GQ_stats_mean"
names(s)[names(s) == "V9"] <- "GQ_stats_stdev"
names(s)[names(s) == "V10"] <- "GQ_stats_min"
names(s)[names(s) == "V11"] <- "GQ_stats_max"
names(s)[names(s) == "V12"] <- "Allele_count_major"
names(s)[names(s) == "V13"] <- "Allele_count_minor"
names(s)[names(s) == "V14"] <- "Major_allele_frequency"
names(s)[names(s) == "V15"] <- "Minor_allele_frequency"
names(s)[names(s) == "V16"] <- "AN"
names(s)[names(s) == "V17"] <- "Homozygote_count_major"
names(s)[names(s) == "V18"] <- "Homozygote_count_minor"
names(s)[names(s) == "V19"] <- "Call_rate"
names(s)[names(s) == "V20"] <- "n_called"
names(s)[names(s) == "V21"] <- "n_not_called"
names(s)[names(s) == "V22"] <- "n_filtered"
names(s)[names(s) == "V23"] <- "n_het"
names(s)[names(s) == "V24"] <- "n_non_ref"
names(s)[names(s) == "V25"] <- "het_freq_hwe"
names(s)[names(s) == "V26"] <- "p_hwe"
# Rename as 'chr...'
chr_1=s

# Merge variants from all chromosomes into one table and write 
s=rbind(chr_1, chr_2, chr_3, chr_4,chr_5,chr_6,chr_7,chr_8,chr_9,chr_10,chr_11,chr_12,chr_13,chr_14,chr_15, chr_16, chr_17, chr_18, chr_19, chr_20, chr_21, chr_22, chr_23, chr_24)
write.csv(s, 'variant_qc_allchr.csv', row.names = F)

# Visualise variant QC metrics 
s <- data.frame(sapply(s, as.numeric))
## Depth 
ggplot(s, aes(Dp_stats_mean))+
  geom_freqpoly(bins=1000)+
  ggtitle('Mean depth per variant')+
  xlab('Mean depth')
## Genotype quality (add line for the cut-off)
ggplot(s, aes(GQ_stats_mean))+
  geom_freqpoly(bins=500)+
  ggtitle('Mean genotype quality per variant')+
  xlab('Mean genotype quality')+
  geom_vline(xintercept = 50, colour='red')
## Call rate
ggplot(s, aes(Call_rate))+
  geom_freqpoly(bins=1000)+
  ggtitle('Call rate per variant')+
  xlab('Call rate')+
  geom_vline(xintercept = 0.9, colour='red')
# p_hwe
ggplot(s, aes(p_hwe))+
  geom_freqpoly(bins=1000)+
  ggtitle('HWE p value per variant')+
  xlab('HWE p value')
# Minor allele freq
ggplot(s, aes(Minor_allele_frequency))+
  geom_freqpoly(bins=1000)+
  ggtitle('Minor allele frequency (MAF) per variant')+
  xlab('MAF')+
  scale_y_log10()
# Alternate homozygous count
ggplot(s, aes(Homozygote_count_minor))+
  geom_freqpoly(bins=1000)+
  ggtitle('Alternate allele homozygote count per variant')+
  xlab('n alt homozygous')+
  scale_y_log10()

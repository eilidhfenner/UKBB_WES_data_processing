# Load libraries and read and format data

## Libraries
library(dplyr)
library(vioplot)
library(ggplot2)
setwd("/Aug_2021/QC_metrics/")

## Read in imputed sex (tsv file created in `3_impute_sex.py`)
sex=read.table('imputed_sex.tsv', header = TRUE)

## Read in y depth and format
s <- read.csv("/chr_24/pre_sample_qc.csv", header=FALSE)
s <- s[-1,]
s = s %>% select(V1, V2)
s$V1 <- sub("^.*:", "", s$V1, perl=TRUE)
s$V2 <- sub("^.*:", "", s$V2, perl=TRUE)
names(s)[names(s) == "V1"] <- "sample_id"
names(s)[names(s) == "V2"] <- "Dp_stats_mean_y"
chry <- s
chry = chry %>% mutate_if(is.character,as.numeric)

## Read in self reported sex and recode
basic=read.table("/Phenotypes/split_phenotypes/basicinfo.txt", header=T)
basic = basic %>% select(f.eid, f.31.0.0)
basic$f.31.0.0 <- as.factor(basic$f.31.0.0)
basic$f.31.0.0 <- plyr::revalue(basic$f.31.0.0, c("0"="Female", "1"="Male"))

# Remove those removed by sample QC (file created in `R_Scripts/Sample_QC.R`)
to_keep=read.csv("sample_qc_keep.tsv", header=T)


# Merge tables into one dataframe
sex <- merge(sex, chry, by.x="s", by.y = "sample_id") 
sex <- merge(sex, basic, by.x="s", by.y = "f.eid") 
sex<- merge(sex, to_keep, by.x="s", by.y="x")


# Visualise data 
## F-stat, coloured by self reported sex 
ggplot(sex, aes(f_stat,group=f.31.0.0, colour=f.31.0.0))+
  geom_histogram(bins=40)+
  ggtitle('Imputed sex f-stat coloured by self reported sex')

## Y depth, coloured by self reported sex and flipped x axis to present with f stat 
ggplot(sex, aes(Dp_stats_mean_y ,group=f.31.0.0, colour=f.31.0.0))+
  geom_histogram(bins=40)+
  ggtitle('Y depth coloured by self reported sex')+
  scale_x_reverse()

# Highlight those with mismatching imputed and self reported sex
sex$match=ifelse(((sex$f_stat<0.6)&(sex$f.31.0.0=='Female')), T, ifelse(((sex$f_stat>0.6)&(sex$f.31.0.0=='Male')), T, F))

# Look at f stats and y depth of the mismatching samples 
mismatch=subset(sex, (sex$match==F))
ggplot(mismatch, aes(f_stat, ,group=f.31.0.0, colour=f.31.0.0))+
  geom_histogram(bins=40)+
  ggtitle('Imputed sex f-stat of samples with mismatching imputed and self-reported sex, coloured by self reported sex')

ggplot(mismatch, aes(Dp_stats_mean_y ,group=f.31.0.0, colour=f.31.0.0))+
  geom_histogram(bins=40)+
  ggtitle('Y depth of samples with mismatching imputed and self-reported sex, coloured by self reported sex')+
  scale_x_reverse()


# Save a list of samples to keep (matching imputed and self-reported sex)
samples_to_keep=subset(sex, (sex$match==T))
write.csv(samples_to_keep, "sample_qc_keep_imp_sex.csv")
to_keep_imputed_sex=samples_to_keep$s
to_keep=as.data.table(to_keep_imputed_sex)
write.table(to_keep, 'sex_imputation_ids_to_keep.tsv', row.names = F)
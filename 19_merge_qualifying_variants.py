## This is for pLI, but should be rerun for each gene set. 

library(dplyr)
library(ggplot2)
library(reshape2)
library(janitor)
library(tibble)
library(tidyverse)

library(dplyr)
library(ggplot2)
library(reshape2)
library(janitor)
library(tibble)
library(tidyverse)


chr_1=read.table('/scratch/c.c1928239/new_builds/chr_1/new/chr_1_LoFi_pli_counts.tsv', header=TRUE)
chr_2=read.table('/scratch/c.c1928239/new_builds/chr_2/new/chr_2_LoFi_pli_counts.tsv', header=TRUE)


chr_3=read.table('/scratch/c.c1928239/new_builds/chr_3/new/chr_3_LoFi_pli_counts.tsv', header=TRUE)


chr_4=read.table('/scratch/c.c1928239/new_builds/chr_4/new/chr_4_LoFi_pli_counts.tsv', header=TRUE)


chr_5=read.table('/scratch/c.c1928239/new_builds/chr_5/new/chr_5_LoFi_pli_counts.tsv', header=TRUE)


chr_6=read.table('/scratch/c.c1928239/new_builds/chr_6/new/chr_6_LoFi_pli_counts.tsv', header=TRUE)


chr_7=read.table('/scratch/c.c1928239/new_builds/chr_7/new/chr_7_LoFi_pli_counts.tsv', header=TRUE)


chr_8=read.table('/scratch/c.c1928239/new_builds/chr_8/new/chr_8_LoFi_pli_counts.tsv', header=TRUE)


chr_9=read.table('/scratch/c.c1928239/new_builds/chr_9/new/chr_9_LoFi_pli_counts.tsv', header=TRUE)

chr_10=read.table('/scratch/c.c1928239/new_builds/chr_10/new/chr_10_LoFi_pli_counts.tsv', header=TRUE)

chr_11=read.table('/scratch/c.c1928239/new_builds/chr_11/new/chr_11_LoFi_pli_counts.tsv', header=TRUE)


chr_12=read.table('/scratch/c.c1928239/new_builds/chr_12/new/chr_12_LoFi_pli_counts.tsv', header=TRUE)


chr_13=read.table('/scratch/c.c1928239/new_builds/chr_13/new/chr_13_LoFi_pli_counts.tsv', header=TRUE)


chr_14=read.table('/scratch/c.c1928239/new_builds/chr_14/new/chr_14_LoFi_pli_counts.tsv', header=TRUE)

chr_15=read.table('/scratch/c.c1928239/new_builds/chr_15/new/chr_15_LoFi_pli_counts.tsv', header=TRUE)



chr_16=read.table('/scratch/c.c1928239/new_builds/chr_16/new/chr_16_LoFi_pli_counts.tsv', header=TRUE)

chr_17=read.table('/scratch/c.c1928239/new_builds/chr_17/new/chr_17_LoFi_pli_counts.tsv', header=TRUE)

chr_18=read.table('/scratch/c.c1928239/new_builds/chr_18/new/chr_18_LoFi_pli_counts.tsv', header=TRUE)


chr_19=read.table('/scratch/c.c1928239/new_builds/chr_19/new/chr_19_LoFi_pli_counts.tsv', header=TRUE)


chr_20=read.table('/scratch/c.c1928239/new_builds/chr_20/new/chr_20_LoFi_pli_counts.tsv', header=TRUE)

chr_21=read.table('/scratch/c.c1928239/new_builds/chr_21/new/chr_21_LoFi_pli_counts.tsv', header=TRUE)


chr_22=read.table('/scratch/c.c1928239/new_builds/chr_22/new/chr_22_LoFi_pli_counts.tsv', header=TRUE)




s=merge(chr_1, chr_2, by='s') #363



s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))


s=merge(s, chr_3, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))



s=merge(s, chr_4, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_5, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_6, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_7, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_8, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_9, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))



s=merge(s, chr_10, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_11, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_12, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))



s=merge(s, chr_13, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))



s=merge(s, chr_14, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_15, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_16, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_17, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_18, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_19, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_20, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_21, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))




s=merge(s, chr_22, by='s')

s$n_AC1 = s$n_AC1.x + s$n_AC1.y
s$n_AC2 = s$n_AC2.x + s$n_AC2.y
s$n_AC3 = s$n_AC3.x + s$n_AC3.y
s$n_AC4 = s$n_AC4.x + s$n_AC4.y
s$n_AC5 = s$n_AC5.x + s$n_AC5.y
s$n_AC6to10 = s$n_AC6to10.x + s$n_AC6to10.y
s$n_AC11to20 = s$n_AC11to20.x + s$n_AC11to20.y
s$n_AC21to50 = s$n_AC21to50.x + s$n_AC21to50.y
s$n_AC51to100 = s$n_AC51to100.x + s$n_AC51to100.y
s$n_AC101to200 = s$n_AC101to200.x + s$n_AC101to200.y

## HC LoF
s$n_HC_LoF_AC1 = s$n_HC_LoF_AC1.x + s$n_HC_LoF_AC1.y
s$n_HC_LoF_AC2 = s$n_HC_LoF_AC2.x + s$n_HC_LoF_AC2.y
s$n_HC_LoF_AC3 = s$n_HC_LoF_AC3.x + s$n_HC_LoF_AC3.y
s$n_HC_LoF_AC4 = s$n_HC_LoF_AC4.x + s$n_HC_LoF_AC4.y
s$n_HC_LoF_AC5 = s$n_HC_LoF_AC5.x + s$n_HC_LoF_AC5.y
s$n_HC_LoF_AC6to10 = s$n_HC_LoF_AC6to10.x + s$n_HC_LoF_AC6to10.y
s$n_HC_LoF_AC11to20 = s$n_HC_LoF_AC11to20.x + s$n_HC_LoF_AC11to20.y
s$n_HC_LoF_AC21to50 = s$n_HC_LoF_AC21to50.x + s$n_HC_LoF_AC21to50.y
s$n_HC_LoF_AC51to100 = s$n_HC_LoF_AC51to100.x + s$n_HC_LoF_AC51to100.y
s$n_HC_LoF_AC101to200 = s$n_HC_LoF_AC101to200.x + s$n_HC_LoF_AC101to200.y
## REVEL
### 75 
s$n_REVEL75_Miss_AC1 = s$n_REVEL75_Miss_AC1.x + s$n_REVEL75_Miss_AC1.y
s$n_REVEL75_Miss_AC2 = s$n_REVEL75_Miss_AC2.x + s$n_REVEL75_Miss_AC2.y
s$n_REVEL75_Miss_AC3 = s$n_REVEL75_Miss_AC3.x + s$n_REVEL75_Miss_AC3.y
s$n_REVEL75_Miss_AC4 = s$n_REVEL75_Miss_AC4.x + s$n_REVEL75_Miss_AC4.y
s$n_REVEL75_Miss_AC5 = s$n_REVEL75_Miss_AC5.x + s$n_REVEL75_Miss_AC5.y
s$n_REVEL75_Miss_AC6to10 = s$n_REVEL75_Miss_AC6to10.x + s$n_REVEL75_Miss_AC6to10.y
s$n_REVEL75_Miss_AC11to20 = s$n_REVEL75_Miss_AC11to20.x + s$n_REVEL75_Miss_AC11to20.y
s$n_REVEL75_Miss_AC21to50 = s$n_REVEL75_Miss_AC21to50.x + s$n_REVEL75_Miss_AC21to50.y
s$n_REVEL75_Miss_AC51to100 = s$n_REVEL75_Miss_AC51to100.x + s$n_REVEL75_Miss_AC51to100.y
s$n_REVEL75_Miss_AC101to200 = s$n_REVEL75_Miss_AC101to200.x + s$n_REVEL75_Miss_AC101to200.y

#Synonymous
s$n_Syn_AC1 = s$n_Syn_AC1.x + s$n_Syn_AC1.y
s$n_Syn_AC2 = s$n_Syn_AC2.x + s$n_Syn_AC2.y
s$n_Syn_AC3 = s$n_Syn_AC3.x + s$n_Syn_AC3.y
s$n_Syn_AC4 = s$n_Syn_AC4.x + s$n_Syn_AC4.y
s$n_Syn_AC5 = s$n_Syn_AC5.x + s$n_Syn_AC5.y
s$n_Syn_AC6to10 = s$n_Syn_AC6to10.x + s$n_Syn_AC6to10.y
s$n_Syn_AC11to20 = s$n_Syn_AC11to20.x + s$n_Syn_AC11to20.y
s$n_Syn_AC21to50 = s$n_Syn_AC21to50.x + s$n_Syn_AC21to50.y
s$n_Syn_AC51to100 = s$n_Syn_AC51to100.x + s$n_Syn_AC51to100.y
s$n_Syn_AC101to200 = s$n_Syn_AC101to200.x + s$n_Syn_AC101to200.y

s = s %>% select(1, 82:ncol(s))


write_csv(s, '/scratch/c.c1928239/regression_analyses/updated_counts/LoFi_pli_genes_counts.csv')
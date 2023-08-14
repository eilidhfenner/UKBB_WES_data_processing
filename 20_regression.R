# This is for pLI but should be run for each gene set.

library(dplyr)
library(ggplot2)
library(reshape2)
library(janitor)
library(tibble)
library(tidyverse)




# Read in cleaned phenotypes. 
phen=read.csv('/scratch/c.c1928239/regression_analyses/phenotypes.csv')
# Filter on ancestry here
phen=subset(phen, phen$PCA_calc_ancestry=="European")
phen=phen[,c(2:ncol(phen))]


### Split phenotypes into groups, FI and NM need to be separate as they have additional covariates. 
## Cog phen includes all cog tests excluding FI and NM 
cog_phen=as.list(colnames(phen[,c(4,7:13,27)]))
names(cog_phen)=c(colnames(phen[,c(4,7:13,27)]))

FI_phen=as.list(colnames(phen[,c(2, 61)]))
names(FI_phen)=c(colnames(phen[,c(2, 61)]))

NM_phen=as.list(colnames(phen[,c(5, 61)]))
names(NM_phen)=c(colnames(phen[,c(5, 61)]))

# Covariates
covars <- list(AC1 = c("Exome_wide_n_Syn_AC1+assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10"))
syn_covars<- list(AC1 = c("assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10"))
FI_covars <- list(AC1 = c("Exome_wide_n_Syn_AC1+assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10+FI_source"))
syn_FI_covars <- list(AC1 = c("assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10+FI_source"))
NM_covars <- list(AC1 = c("Exome_wide_n_Syn_AC1+assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10+NM_source"))
syn_NM_covars <- list(AC1 = c("assessment_centre+batch+Sex__1_is_Male+Standardised_age+Standardised_age_sq+sex_st_age+sex_st_age_squared+PC1+PC2+PC3+PC4+PC5+PC6+PC7+PC8+PC9+PC10+NM_source"))

# Read in the counts of variants in LoFi genes and select the vars of interest. 
counts=read.csv('/scratch/c.c1928239/regression_analyses/updated_counts/LoFi_pli_genes_counts.csv')
counts=counts[,c(1,30,128,156)]


# Qualifying variants
## Per AC set 
# Diff ACs
AC1_qual_vars=as.list(colnames(counts[,c(2,3)]))
names(AC1_qual_vars)=c(colnames(counts[,c(2,3)]))
AC1_syn_vars=as.list(colnames(counts[,c(2,4)]))
names(AC1_syn_vars)=c(colnames(counts[,c(2,4)]))
AC1_syn_vars=AC1_syn_vars[[2]]

data=merge(counts, phen, by.x='s', by.y='f.eid')



# AC1 
## Run glm  
fit <- lapply(cog_phen, function(p) {
  lapply(AC1_qual_vars, function(v) {
    model = lm(as.formula(paste0(p, "~", v, "+", covars[[1]])), data=data)
    count = data %>% group_by(!is.na(!!as.name(p))) %>% summarise(var_count=sum(!!as.name(v)))
    return(list(model = model, count=count))
  })
})

## Save important information 
results_table <- lapply(seq(fit), function(x) {
  lapply(seq(fit[[1]]), function(y) {
    list(phen=fit[[x]][[y]][[1]][[13]][[2]], 
         qual_var = names(fit[[x]][[y]][[1]][[1]][2]), 
         beta= fit[[x]][[y]][[1]][[1]][[2]],
         se = summary(fit[[x]][[y]][[1]])$coefficients[2,2],
         p_val = summary(fit[[x]][[y]][[1]])$coefficients[2,4],
         t_val = summary(fit[[x]][[y]][[1]])$coefficients[2,3],
         or = exp(fit[[x]][[y]][[1]][[1]][[2]]),
         upper_ci = confint(fit[[x]][[y]][[1]])[2,2], 
         lower_ci = confint(fit[[x]][[y]][[1]])[2,1],
         n_mutations_cases=as.numeric(fit[[x]][[y]][[2]][2,2]),
         n_mutations_controls=NA,
         n_people=length(fit[[x]][[y]][[1]][[2]]),
         formula = fit[[x]][[y]][[1]][[13]]
    )
  })
})
# Put into dataframe
df <- data.frame(matrix(unlist(results_table), nrow=length(results_table), byrow = TRUE))
d1 <- df[1:13]
names(d1)[1]= 'phenotype'
names(d1)[2]= 'qualifying_variant'
names(d1)[3]= 'beta'
names(d1)[4]= 'standard_error'
names(d1)[5]= 'p_value'
names(d1)[6]= 'z_t_value'
names(d1)[7]= 'odds_ratio'
names(d1)[8]= 'upper_ci'
names(d1)[9]= 'lower_ci'
names(d1)[10]= 'n_mutations_cases'
names(d1)[11]= 'n_mutations_controls'
names(d1)[12]= 'n_samples'
names(d1)[13]= 'formula'
d1$annotation='HC LoF'
d2<- df[14:26]
d2$annotation='Revel >.75 Missense'
all<- rbind(d1, setNames(d2, names(d1)))
all$AC='1'
all$regression='lm'
all$gene_set='LoFi_pLI'
all_results=all

# AC1 syn
## Run glm  
fit <- lapply(cog_phen, function(p) {
  lapply(AC1_syn_vars, function(v) {
    model = lm(as.formula(paste0(p, "~", v, "+", syn_covars[[1]])), data=data)
    count = data %>% group_by(!is.na(!!as.name(p))) %>% summarise(var_count=sum(!!as.name(v)))
    return(list(model = model, count=count))
  })
})


## Save important information 
results_table <- lapply(seq(fit), function(x) {
  lapply(seq(fit[[1]]), function(y) {
    list(phen=fit[[x]][[y]][[1]][[13]][[2]], 
         qual_var = names(fit[[x]][[y]][[1]][[1]][2]), 
         beta= fit[[x]][[y]][[1]][[1]][[2]],
         se = summary(fit[[x]][[y]][[1]])$coefficients[2,2],
         p_val = summary(fit[[x]][[y]][[1]])$coefficients[2,4],
         t_val = summary(fit[[x]][[y]][[1]])$coefficients[2,3],
         or = exp(fit[[x]][[y]][[1]][[1]][[2]]),
         upper_ci = confint(fit[[x]][[y]][[1]])[2,2], 
         lower_ci = confint(fit[[x]][[y]][[1]])[2,1],
         n_mutations_cases=as.numeric(fit[[x]][[y]][[2]][2,2]),
         n_mutations_controls=NA,
         n_people=length(fit[[x]][[y]][[1]][[2]]),
         formula = fit[[x]][[y]][[1]][[13]]
    )
  })
})
# Put into dataframe
df <- data.frame(matrix(unlist(results_table), nrow=length(results_table), byrow = TRUE))
d1 <- df[1:13]
names(d1)[1]= 'phenotype'
names(d1)[2]= 'qualifying_variant'
names(d1)[3]= 'beta'
names(d1)[4]= 'standard_error'
names(d1)[5]= 'p_value'
names(d1)[6]= 'z_t_value'
names(d1)[7]= 'odds_ratio'
names(d1)[8]= 'upper_ci'
names(d1)[9]= 'lower_ci'
names(d1)[10]= 'n_mutations_cases'
names(d1)[11]= 'n_mutations_controls'
names(d1)[12]= 'n_samples'
names(d1)[13]= 'formula'
d1$annotation='Synonymous'
all=d1
all$AC='1'
all$regression='lm'
all$gene_set='LoFi_pLI'
all_results=rbind(all_results, all)



## Save out 
mid <- apply(all_results, 2, as.character)
write.csv(mid, '/scratch/c.c1928239/regression_analyses/regression_LoFi_pLI_genes.csv')

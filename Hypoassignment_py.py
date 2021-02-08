import pandas as pd
import scipy 
from scipy import stats
import statsmodels.api as sm
from statsmodels.formula.api import ols

#####Sol - 1- Dataset- cutlets

Cutlets=pd.read_csv("D:\Modules\Module 5/Cutlets.csv")
Cutlets


Cutlets.columns="UnitA","UnitB"

Cut = Cutlets.iloc[0:34,]n

##########Normality Test ############
print(stats.shapiro(Cut.UnitA))    #Shapiro Test
print(stats.shapiro(Cut.UnitB))
 #p high null fly data is normal

######## Variance test #########
scipy.stats.levene(Cut.UnitA, Cut.UnitB)
help(scipy.stats.levene)
# p-value = 0.583 > 0.05 so p high null fly => Equal variances

######## 2 Sample T test ################
scipy.stats.ttest_ind(Cut.UnitA, Cut.UnitB)
#Null Hypothesis -> Diamter of both the units are equal 
# Alternative Hypothesis -> Diamter of both the units are unequal 
# p-value = 0.36 > 0.05 => p high null fly => accept Null hypothesis
#Conclusion ;There is no difference in Diameter of both the units


###############################################
###Sol- 2 dataset - Labtat
LabTAT=pd.read_csv("D:\Modules\Module 5/LabTAT.csv")
LabTAT.columns="Lab1","Lab2","Lab3","Lab4"
Lab=LabTAT.iloc[0:120,]
Lab
##########Normality Test ############

print(stats.shapiro(Lab.Lab1))    #Shapiro Test
print(stats.shapiro(Lab.Lab2))
print(stats.shapiro(Lab.Lab3))

#p high null fly data is normal

######## Variance test #########
scipy.stats.levene(Lab.Lab1,Lab.Lab2)
scipy.stats.levene(Lab.Lab2,Lab.Lab3)
scipy.stats.levene(Lab.Lab3,Lab.Lab4)
scipy.stats.levene(Lab.Lab1,Lab.Lab4)
###in all cases p-high Null fly , Variance are equal so will perform one way anova test

############# One - Way Anova###################

mod = ols('Lab1 ~ Lab1+Lab2+Lab3+Lab4',data=Lab).fit()

aov_table=sm.stats.anova_lm(mod, type=2)
print(aov_table)

##p-value is low for Lab1 and lab2 => p low null go => accept alternate hypothesis
#Yes there is difference in TAT in all reports of laboratory

###############################################
###Sol- 4 Dataset - Customer order form

CustomerOrderform=pd.read_csv("D:\Modules\Module 5/CustomerOrderform.csv")
CustomerOrderform[0:300,]
Customer=CustomerOrderform.iloc[0:300,]

count=pd.crosstab(Customer.Malta,Customer.India)
count=pd.crosstab(Customer["Error Free"],Customer["Defective"])
count
Chisquares_results=scipy.stats.chi2_contingency(count)

Chi_square=[['','Test Statistic','p-value'],['Sample Data',Chisquares_results[0],Chisquares_results[1]]]


###############################################
###Sol- 5 Dataset - Fantaloons
import numpy as np

Fantaloons = pd.read_csv("D:\Modules\Module 5/Fantaloons.csv")
Fanta=Fantaloons.iloc[0:400,]

from statsmodels.stats.proportion import proportions_ztest

tab1 = Fanta.Weekdays.value_counts()
tab1
tab2 = Fanta.Weekend.value_counts()
tab2

count = np.array([66,47])
nobs = np.array([233,167])

######## 2-proportion test ###########

stats,pval = proportions_ztest(count, nobs,alternative='two-sided') 
print(pval) 
# Ha -> Proportions of Female =  Proportions of male
# Ho -> Proportions of female is not equal to Proportions of male
# p-value = 0.9681 > 0.05 p high null fly; accept Null hypothesis i.e.
#proportion of female and male is equal on Weekdays and weekend  








#=========================================================================
#  Sol - 1- Dataset- cutlets
#=========================================================================

library(readr)
Cutlets <- read_csv("D:/Assignment/hypothesis testing/Cutlets.csv")
View(Cutlets)
attach(Cutlets)

#############Normality test###############


shapiro.test(Cutlets$`Unit A`) #p=0.32
shapiro.test(Cutlets$`Unit B`) #P= 0.52
# Data is normally distributed p>0.05 p high null fly 
y1 <- `Unit A`
y2 <- `Unit B`

###########variene test##########

var.test(y1,y2) # having equal variene so 2 sample t test for equal varience

############ 2 sample t test##########
t.test(y1,y2,alternative = "two.sided",conf.level = 0.95,correct = TRUE)
#Null Hypothesis -> Diamter of both the units are equal 
# Alternative Hypothesis -> Diamter of both the units are unequal 
# p-value = 0.4723 > 0.05 => p high null fly => accept Null hypothesis
#Conclusion ;There is no difference in Diameter of both the units

#==================================================================================
#               Sol- 2 dataset - Labtat
#===================================================================================
library(readr)
LabTAT <- read_csv("D:/Modules/Module 5/LabTAT.csv")
View(LabTAT)

colnames(LabTAT)<-c("Lab1","Lab2","Lab3","Lab4")
View(LabTAT)
attach(LabTAT)
#########normaliy test#######
shapiro.test(LabTAT$Lab1)#p=0.55
shapiro.test(LabTAT$Lab2)#p=0.86
shapiro.test(LabTAT$Lab3)#p=0.42
shapiro.test(LabTAT$Lab4)#p=0.66
summary(LabTAT)
# P>alpha(0.5) -> P high Null fly -> Fail to reject Null hypothesis.
#Conclusion: Data of Lab1,Lab2,Lab3,Lab4 are assumed to be normal.


#######Variance test######
var.test(Lab1,Lab2) #p=0.16
var.test(Lab2,Lab3) #p= 0.27
var.test(Lab3,Lab4) #p= 0.31
var.test(Lab1,Lab4) #p= 0.14

###in all cases p-high Null fly , Variance are equal so will perform one way anova test


Stacked_Data <- stack(LabTAT)
View(Stacked_Data)
attach(Stacked_Data)

Anova_results <- aov(values~ind,data = Stacked_Data)
summary(Anova_results)
#Null Hypothesis -> All laboratories having equal TAT 
# Alternative Hypothesis -> atleast one laboratory is having least TAT.
# p-value = 2e-16 < 0.05 => p low null go => accept alternate hypothesis
#Yes there is difference in TAT in all reports of laboratory
  
#=================================================================================
#               ANS- 3, dataset - BuyerRatio
#================================================================================= 

library(readr)
BuyerRatio <- read_csv("C:/Users/om/Desktop/Harsh_150620/Modules/Module 5/BuyerRatio.csv")
View(BuyerRatio)
# Ho -> the  Proportions of all regions are equal
# Ha ->atleast the  Proportions of one region is not equal
BuyerRatio<-rbind(c(50,142,131,70),c(435, 1523, 1356, 750))
chisq.test(BuyerRatio)
#p value = 0.66 >0.05 p high null fly-> fail to reject null hypothesis
#Conclusion: The Proportions of all regions are assumed to be equal

#final conclusion: Male-female buyer ratios are assumed similar across all the regions

#=================================================================================
#                   Sol- 4 Dataset - Customer order form
#=================================================================================


library(readr)
Costomer_OrderForm <- read_csv("D:/Assignment/hypothesis testing/OrderForm.csv")
View(Costomer_OrderForm)
Stacked_Data <- stack(Costomer_OrderForm)

View(Stacked_Data)
attach(Stacked_Data)
table(Stacked_Data$ind,Stacked_Data$values)
chisq.test(table(Stacked_Data$ind,Stacked_Data$values))
# Ho -> all centers have equal Proportions of defect
# Ha -> atleast one of the center defect is not equal to other
# p value = 0.27 >0.05 p high null fly
# Conclusion: all centers have equal Proportions of defect assumed to be equal

#===============================================================================
#                       Sol- 5 Dataset - Fantaloons
#============================================================================= 
library(readr)
Faltoons <- read_csv("D:/Assignment/hypothesis testing/Faltoons.csv")
View(Faltoons)
attach(Faltoons)
table1 <- table(Weekdays,Weekend)
table1 
# 2 proportion t test
prop.test(x=c(66,47),n=c(233,167),conf.level = 0.95,correct = FALSE,alternative = "two.sided")
#p=0.96, p high null fly
#prop.test(x=c(66,47),n=c(233,167),conf.level = 0.95,correct = FALSE,alternative = "greater")


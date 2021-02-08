# For reading data set
# importing necessary libraries
import pandas as pd # deals with data frame  
import numpy as np  # deals with numerical values

calories = pd.read_csv("D:\Modules\Module 6 - SLR/calories_consumed.csv")
calories
import matplotlib.pylab as plt #for different types of plots
# Scatter plot
plt.scatter(x=calories['Weight gained (grams)'], y=calories['Calories Consumed'],color='green')
#possitive relation
calories.columns="weight","Calories"
np.corrcoef(calories.weight) #strong correlation
np.corrcoef(calories.Calories)#strong correlation
help(np.corrcoef)

import statsmodels.formula.api as smf

model = smf.ols('weight ~ Calories', data=calories).fit()
model.summary()

pred1 = model.predict(calories)
pred1
print (model.conf_int(0.01)) # 99% confidence interval

res = Calories.weight - pred1
sqres = res*res
mse = np.mean(sqres)
rmse = np.sqrt(mse)
rmse


######### Model building on Transformed Data

# Log Transformation
# x = log(waist); y = at
plt.scatter(x=np.log(wcat['Waist']),y=wcat['AT'],color='brown')
np.corrcoef(np.log(wcat.Waist), wcat.AT) #correlation

model2 = smf.ols('weight ~ np.log(Calories)',data=calories).fit()
model2.summary()

pred2 = model2.predict(calories)
pred2
print(model2.conf_int(0.01)) # 99% confidence level

res2 = calories.weight - pred2
sqres2 = res2*res2
mse2 = np.mean(sqres2)
rmse2 = np.sqrt(mse2)
rmse2
# Exponential transformation
plt.scatter(x=calories['Calories'], y=np.log(calories['weight']),color='orange')

np.corrcoef(wcat.Waist, np.log(wcat.AT)) #correlation

model3 = smf.ols('np.log(weight) ~ Calories',data=calories).fit()
model3.summary()
model.params
pred_log = model3.predict(calories)
pred_log
pred3 = np.exp(pred_log)
pred3
print(model3.conf_int(0.01)) # 99% confidence level

res3 = calories.weight - pred3
sqres3 = res3*res3
mse3 = np.mean(sqres3)
rmse3 = np.sqrt(mse3)
rmse3


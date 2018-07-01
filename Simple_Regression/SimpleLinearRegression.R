# Simple Linear Regression
#importing dataset
dataset = read.csv('Salary_Data.csv')

#splitting dataset into traing set and test set
# install.package(caTools)
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
traing_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

#Fitting Simple Linear Regression to training set
#lm - linear model
regressor = lm(formula = Salary ~ YearsExperience, data = traing_set)
#summary(regressor)
#Coefficients:
#  Estimate Std. Error t value Pr(>|t|)    
#(Intercept)        25592       2646   9.672 1.49e-08 ***  
# * - no statical significance *** - high stastical significance

#  YearsExperience     9365        421  22.245 1.52e-14 ***
#  ---
#  Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1

#Predicting the Test set results;
y_pred = predict(regressor, newdata = test_set)

#> y_pred
#2         4         5         8        11        16        20        21 
#37766.77  44322.33  46195.35  55560.43  62115.99  71481.07  81782.66  89274.72 
#24        26 
#102385.84 109877.90 

#Visualize the training result
install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = traing_set$YearsExperience, y = traing_set$Salary),
             colour = 'red') +
  geom_line(aes(x = traing_set$YearsExperience, y = predict(regressor, newdata = traing_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (Training set)') +
  xlab('YearsExperience') +
  ylab('Salary')
  

#Visualize the test result
install.packages('ggplot2')
library(ggplot2)
ggplot() + 
  geom_point(aes(x = test_set$YearsExperience, y = test_set$Salary),
             colour = 'red') +
  geom_line(aes(x = traing_set$YearsExperience, y = predict(regressor, newdata = traing_set)),
            colour = 'blue') +
  ggtitle('Salary vs Experience (Test set)') +
  xlab('YearsExperience') +
  ylab('Salary')







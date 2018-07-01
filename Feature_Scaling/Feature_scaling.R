#importing dataset
dataset = read.csv('Data.csv')


#taking care of missing data
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x,na.rm = TRUE)),
                     dataset$Age)

dataset$salary = ifelse(is.na(dataset$salary),
                        ave(dataset$salary, FUN = function(x) mean(x,na.rm = TRUE)),
                        dataset$salary)
#Encoding categorical data
dataset$country = factor(dataset$country,
                         levels = c('France','spain','germany'),
                         labels = c(1,2,3))
dataset$purchased = factor(dataset$purchased,
                           levels = c('Yes','no'),
                           labels = c(1,0))


#splitting dataset into traing set and test set
# install.package(caTools)
library(caTools)
set.seed(123)
split = sample.split(dataset$purchased, SplitRatio = 0.8)
traing_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)
#Factor not giving numberic so you get x is must numberic error 
#Feature Scaling 
traing_set[, 2:3] = scale(traing_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])




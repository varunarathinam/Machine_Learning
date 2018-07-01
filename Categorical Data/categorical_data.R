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

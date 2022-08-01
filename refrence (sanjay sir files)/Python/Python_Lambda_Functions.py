'''
    Author : Sanjay Sukhwani
    Purpose : Lambda Functions
    Date : 2022-07-22 
    Time : 16:30:57 
'''

def square(a):
    return a*a

# Defining Lambda Function for the same : 
# Lambda definition does not include a “return” statement, it always contains an expression that is returned.

sq = lambda a : a*a

pow = lambda x,y : x**y

cube = lambda x : x*x*x

# Using if-else in Lambda Function : 
# Syntax : lambda <arguments> : <true_value> if(<condition>) else <false_value>
Max = lambda n1,n2 : n1 if(n1>n2) else n2

# Using if-elif-else
# Syntax : lambda <arguments> : <true_value> if(<condition>) else <true_value2> if(condition2) else <false_value>)
identifyNum = lambda x : 1 if(x>0) else (-1 if(x<0) else 0)

n = int(input("Enter number : "))
print(identifyNum(n))
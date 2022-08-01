'''
    Author : Sanjay Sukhwani
    Purpose : Map Function
    Date : 2022-07-22 
    Time : 17:13:45 
'''

''' 

    # Map Function :
        -> map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

    # Syntax :
        map(fun, iter)

        Where,
            o fun : It is a function to which map passes each element of given iterable.
            o iter : It is a iterable which is to be mapped.Returns :

        Returns :
            o Returns a list of the results after applying the given function  
            to each item of a given iterable (list, tuple etc.)
          
'''

def add(n):
        return n + n

numbers = (1, 2, 3, 4)

result=[]
for num in numbers:
    result.append(add(num))

result = map(add, numbers)
print(list(result))

numbers = [1, 2, 3, 4]
result = map(add, numbers)
print(list(result))
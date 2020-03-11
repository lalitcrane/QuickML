

# Reload a package after changes

import imp  #imp is a standard package in python
imp.reload(MyPackage)

or 

import importlib
importlib.reload(MyPackage)


# Print statements
foo = 'foo'
bar = 'bar'

foobar = '%s%s' % (foo, bar) # It is OK
foobar = '{0}{1}'.format(foo, bar) # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar) # It is best

#Lambada
f = lambda x, y : x + y
z = f(2,1) # gives answer as 3

#map function r = map(func, seq)
def fahrenheit(T):
    return ((float(9)/5)*T + 32)
def celsius(T):
    return (float(5)/9)*(T-32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
C = map(celsius, F)

# Combining Map and Lambada
Celcius = map(lambda x: (float(5)/9)*(x-32), Fahrenheit)

# Filter
result = filter(lambda x: x % 2, myarray)  # will return elements with even values

#Reduce
reduce(lambda x,y: x+y, [1,2,3,4])  #will return addition of all elements
# Calculating the sum of the numbers from 1 to 100:
reduce(lambda x, y: x+y, range(1,101))


# Print Statements

name = 'Tushar'
age = 23
print(f"Hello, My name is {name} and I'm {age} years old.") 

import datetime 
  
today = datetime.datetime.today() 
print(f"{today:%B %d, %Y}")   # Output = April 04, 2018

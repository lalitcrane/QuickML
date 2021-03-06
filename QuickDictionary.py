Filtering Dictionary in one line
dict((k, v) for (k, v) in points.iteritems() if v[0] < 5 and v[1] < 5)
Or
dict((k, v) for k, v in points.items() if all(x < 5 for x in v))
Or
newDict = { key:value for (key,value) in dictOfNames.items() if key % 2 == 0}

# Filter dictionary by keeping elements whose keys are divisible by 2
newDict = dict(filter(lambda elem: elem[0] % 2 == 0, dictOfNames.items()))
----------------------------------------------
Python
newDict = dict()

# Iterate over all the items in dictionary and filter items which has even keys
for (key, value) in dictOfNames.items():
# Check if key is even then add pair to new dictionary
    if key % 2 == 0:
        newDict[key] = value

print('Filtered Dictionary : ')
print(newDict)

--------------------------------------
newDict = dict()
# Iterate over all the items in dictionary and filter items which has even keys
for (key, value) in dictOfNames.items():
   # Check if key is even then add pair to new dictionary
   if key % 2 == 0:
       newDict[key] = value
 
print('Filtered Dictionary : ')
print(newDict)


Filtering Dictionary by creating a filter method for it.
class FilterDict(dict):
    def __init__(self, input_dict):
        for key, value in input_dict.iteritems():
            self[key] = value
    def filter(self, criteria):
        for key, value in self.items():
            if (criteria(value)):
                self.pop(key)

my_dict = FilterDict( {'a':(3,4), 'b':(1,2), 'c':(5,5), 'd':(3,3)} )
my_dict.filter(lambda x: x[0] < 5 and x[1] < 5)

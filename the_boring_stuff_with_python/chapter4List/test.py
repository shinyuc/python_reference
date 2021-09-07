import copy
spam = [['A', 1] , 'B', 'C', 'D']
print(id(spam))
cheese = copy.deepcopy(spam)
print(id(cheese))
cheese[2] = 42
print(spam)
print(cheese)
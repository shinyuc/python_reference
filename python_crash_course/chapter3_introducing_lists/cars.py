# Organizing a List
# Permanently with the sort() Method
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_1 = cars
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']
print(cars_1)  # ['toyota', 'subaru', 'bmw', 'audi']
# Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Here is the sorted list:')
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']

print('Here is the original list:')
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
# Printing a List in Reverse Order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']
# Finding the length of a List
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
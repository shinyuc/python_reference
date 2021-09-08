# 3-1 Names
names = ['Shiyu', 'Cheng', 'Alex', 'Bob']
for name in names:
    print(name)
# 3-2 Greetings
for name in names:
    message = f"Hello, {name}!"
    print(message)
# 3-3 Your Own List
brands = ['Honda', 'Bmw', 'Toyota']
for brand in brands:
    message = f"I would like to own a {brand}."
# 3-4 Guest List
names = ['Alex', 'Bob', 'Charlie']
for name in names:
    print(f'Hi {name.title()}, I would like to invite you to dinner.')
# 3-5 Changing Guest List
names = ['Alex', 'Bob', 'Charlie']
print(names)
names.remove('Charlie')
names.append('Denial')
print(names)
# 3-6 More Guests
names = ['Alex', 'Bob', 'Charlie']
print(names)
names.insert(0, 'Cheng')
names.insert(2, 'Harbin')
names.append('Shiyu')
print(names)  # ['Cheng', 'Alex', 'Harbin', 'Bob', 'Charlie', 'Shiyu']
# 3-7 Shrinking Guest List
names = ['Cheng', 'Alex', 'Harbin', 'Bob', 'Charlie', 'Shiyu']
print('I can invite only two people for dinner.')
i = 6
while i > 2:
    names.pop()
    i -= 1
print(names)
# 3-8 Seeing the World
locations = ['Harbin', 'Beijing', 'Worcester']
print('The original list is:')
print(locations)  # ['Harbin', 'Beijing', 'Worcester']
print('The sorted list is:')
print(sorted(locations))  # ['Beijing', 'Harbin', 'Worcester']
print('The list now is:')
print(locations)  # ['Harbin', 'Beijing', 'Worcester']
locations.reverse()
print(locations)  # ['Worcester', 'Beijing', 'Harbin']
locations.reverse()
print(locations)  # ['Harbin', 'Beijing', 'Worcester']
locations.sort()
print(locations)  # ['Beijing', 'Harbin', 'Worcester']
locations.sort(reverse=True)
print(locations)  # ['Worcester', 'Harbin', 'Beijing']
# 3-9 Dinner Guests
names = ['Alex', 'Bob', 'Charlie']
number = len(names)
print(f"The number of guests is {number}.")
#  3-10 Every Function

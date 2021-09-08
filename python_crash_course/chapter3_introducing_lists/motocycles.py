# Change(1) Add(2) and Remove(3)
# Change
#       lists[1] = 'item'
# Add(1) append()
#       lists.append('item')
# Add(2) insert()
#       lists.insert(1, 'item')
# Remove(1) del
#       del lists[1]
# Remove(2) pop()
#       lists.pop() pop the last item
#       lists.pop(1)
# Remove(3) remove()
#       lists.remove('item')


motorcycles = ['Honda', 'yamaha', 'suzuki']
print(motorcycles)
# Modifying Elements in a List
motorcycles[0] = 'ducati'
print(motorcycles)
# Adding Elements to a List
motorcycles.append('ducati')
print(motorcycles)
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
# Inserting Elements into a list
motorcycles = ['Honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)
# Removing Elements from a list del&pop
# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']

del motorcycles[1]
print(motorcycles)
# Removing an Item Using the pop() method
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)  # ['honda', 'yamaha']
print(popped_motorcycle)    # suzuki

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")
# Popping Items from any Position in a list
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
# Removing an Item by Value (Just remove the first occurrence)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me!")


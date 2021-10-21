# 4-1 Pizzas
pizzas = ['cheese', 'pepperoni', 'margherita']
for pizza in pizzas:
    print(f"I love {pizza} pizza!")

print("I do really love pizza!\n")
# 4-2 Animals
animals = ['dog', 'cat', 'bird']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")
# 4-3 Counting to Twenty
for i in range(21):
    print(i)
# 4-4 One Million
x = range(1, 10)
for number in x:
    print(number)
# 4-5 Summing a Million
x = list(range(1, 100))
print(sum(x))
# 4-6 Odd Numbers
even_numbers = list(range(2, 21, 2))
for even_number in even_numbers:
    print(even_number)
# 4-7 Threes
threes = []
for value in range(1, 11):
    three = value*3
    threes.append(three)

print(threes)
# 4-8 Cubes
cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)

print(cubes)
# 4-9 Cube Comprehension
cubes = [value**3 for value in range(1, 11)]
print(cubes)
# 4-10 Slices
players = ['charles', 'martina', 'michael', 'florenece', 'eli']
print("The first three items in the list are:")
print(players[0:3])  # ['charles', 'martina', 'michael']
print("The middle three items in the list are:")
print(players[1:4])  # ['martina', 'michael', 'florenece']
print("The last three items in the list are:")
print(players[-3:])  # ['michael', 'florenece', 'eli']
# 4-11 Buffet
basic_foods = ('beef', 'pizza', 'cake', 'ice cream', 'juice')
for food in basic_foods:
    print(food)
print('The second dish is:')
print(basic_foods[1])
basic_foods = ('fish', 'sandwich', 'cake', 'ice cream', 'juice')
for food in basic_foods:
    print(food)

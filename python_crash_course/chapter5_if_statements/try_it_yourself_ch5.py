# 5-1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(f"The result is {car == 'audi'}.")
# 5-2 More Conditional Tests
# Tests for equality and inequality with strings
name = 'apple'
name_1 = 'Apple'
print(f"Is name equal to name_1? The answer is: {name == name_1}.")
print(f"Is name unequal to name_1? The answer is: {name != name_1}.")
# Tests using the lower() function
print(f"Is name equal to name_1? "
      f"The answer is: {name.lower() == name_1.lower()}.")
# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
age = 20
age_1 = 25
print(f"Is age equal to age_1? The answer is: {age == age_1}.")
print(f"Is age unequal to age_1? The answer is: {age != age_1}.")
print(f"Is age greater than age_1? The answer is: {age > age_1}.")
print(f"Is age less than age_1? The answer is: {age < age_1}.")
print(f"Is age greater than or equal to age_1? The answer is: {age >= age_1}.")
print(f"Is age less than or equal to age_1? The answer is: {age <= age_1}.")
# Tests using the and keyword and the or keyword
print(age > 23 and age_1 > 23)
print(age > 23 or age_1 > 23)
# Test whether an item is in a list
age = [10, 11, 12]
if 11 in age:
    print('11 is in list age.')
# Test whether an item is not in a list
color = ['red', 'yellow', 'blue']
if "green" not in color:
    print('Green in not in color list.')




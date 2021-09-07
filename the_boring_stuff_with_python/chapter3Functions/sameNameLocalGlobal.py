def spam():
    global eggs
    eggs = 'spam'  # this is the global because there’s a global statement


def bacon():
    eggs = 'bacon'
    # this is a local because
    # there’s an assignment statement for it in that function


def ham():
    print(eggs)
    # this is the global because
    # there is no assignment statement or global statement


eggs = 42  # this is the global
spam()
print(eggs)

# The code in a function can’t use a local variable named eggs
# and then use the global eggs variable later in that same function.

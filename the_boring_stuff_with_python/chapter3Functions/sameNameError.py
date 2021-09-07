def spam():
    print(eggs)#ERROR!
    eggs = 'spam local'  # assignment makes 'eggs' a local variable

eggs = 'global'
spam()
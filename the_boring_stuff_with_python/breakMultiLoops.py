# Method 1 Using Flag
print('Method 1')
flag = True

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i, j, k)
            if i == j == k == 1:
                flag = False
                print('break')
                break
        if not flag:
            break
    if not flag:
        break

# Method 2 Using loop else
print('Method 2')

for i in range(3):
    for j in range(3):
        for k in range(3):
            print(i, j, k)
            if i == j == k == 1:
                print('break')
                break
        else:       # 如果循环内被break跳出，就不执行else。
            continue
        break
    else:
        continue
    break
# Method 3 Function
print('Method 3')


def loop():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i, j, k)
                if i == j == k == 1:
                    print('break')
                    return


loop()
# Method 4 Exception
print('Method 4')


class Break(Exception):
    pass


try:
    for i in range(3):
        for j in range(3):
            for k in range(3):
                print(i, j, k)
                if i == j == k == 1:
                    raise Break('break')
except Break as e:
    print(e)
# Method 5
print('Method 5')
from itertools import product

for i, j, k in product(range(3), range(3), range(3)):
    print(i, j, k)
    if i == j == k == 1:
        print('break')
        break

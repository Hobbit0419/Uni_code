from random import randint

def delete(my_list, number):
    for n in my_list:
        if n == number:
            my_list.pop(my_list.index(n))

def rand_list(length, min, max):
    l = []
    for i in range(length):
        l.append(randint(min, max))
    return l

test = rand_list(10,0,10)

print(test)
delete(test, randint(0,10))
print(test)
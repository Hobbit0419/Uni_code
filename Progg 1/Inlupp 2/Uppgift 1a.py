from random import randint

def delete(my_list, number):
    intermediate = []
    for n in my_list:
        if n != number:
            intermediate.append(n)
    my_list.clear()
    my_list.extend(intermediate)

def rand_list(length, min, max):
    l = []
    for i in range(length):
        l.append(randint(min, max))
    return l

test = rand_list(10,0,10)

print(test)
delete(test, randint(0,10))
print(test)
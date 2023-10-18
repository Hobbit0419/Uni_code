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


def empty_list(list, range):
    iteration_count = 0
    while len(list) != 0:
        delete(list, randint(range[0], range[1]))
        iteration_count += 1
    print(iteration_count)
    return iteration_count

test = rand_list(10, 0, 10)

empty_list(test, (0, 10))

print(test)
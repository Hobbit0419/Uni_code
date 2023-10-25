from random import randint

def delete(my_list, number):
    for n in my_list: # går igenom listan och kollar om siffran anget finns och plockar bort den
        if n == number:
            my_list.pop(my_list.index(n))

def rand_list(length, min, max): # skapar en lista med random siffror mellan min och max med ett antal element lika med length
    l = []
    for i in range(length):
        l.append(randint(min, max))
    return l

test = [1,2,4,7,7,7,8,9]
number = 7
print(test)
delete(test, number)
print(number)
print(test)
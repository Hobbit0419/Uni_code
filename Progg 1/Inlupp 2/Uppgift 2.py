from random import randint

def rand_list(length, min, max):
    l = []
    for i in range(length):
        l.append(randint(min, max))
    return l


def smooth(list_a, n):
    output_list = []
    for i in range(len(list_a)):
        if i + 1 + n > len(list_a):
            output_list.append((sum(list_a[i-n:]) + ((i+n - len(list_a)+1)*list_a[-1]))/(2*n+1)) #hanterar randvärden åt höger
            print(list_a[i-n:])
        elif i - n < 0:
            output_list.append((sum(list_a[:i+n+1]) + (abs(2*i-n)*list_a[0]))/(2*n+1)) #hanterar randvärden åt vänster
        else:
            output_list.append(sum(list_a[i-n:i+n+1])/(2*n+1)) #alla icke randvärden
    return output_list


test = [1,2,6,4,5,0,1,2]
smooth_test = smooth(test, 1)

print(test)
print(smooth_test)

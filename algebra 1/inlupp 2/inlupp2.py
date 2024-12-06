numbers = [256217472, 9394664064, 3170691216]

for number in numbers:
    div = 0
    for i in range(1,number):
        if number % i == 0:
            div += 1
    print(div)
import random			# paket med slumptalsfunktioner

number = random.randint(1,100)	# Slumptal mellan 1 och 100
ans = 0
while ans != number:			# "Evighetsloop"
    ans = int(input('Gissa: '))
    if ans < number:
        print('För litet!')
    elif ans > number:
        print('För stort!')
    else:
        print('Rätt!')

print('Det för den här gången')
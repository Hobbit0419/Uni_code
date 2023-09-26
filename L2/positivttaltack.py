tal = 0
försök = 0

while tal <= 0:
    tal = int(input('Vänligen mata in ett positivt heltal. '))
    försök += 1

if försök > 3:
    print(f'Yay du kan följa instruktioner och matade in talet {tal}.')
else:
    print('OK')
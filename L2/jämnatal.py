numbers = []   # En tom lista skapas
evennumbers = []
print('Mata in positiva tal. Avbryt med 0')
x = int(input('Första: '))
while x > 0:  # Så länge som x > 0
    numbers.append(x)  # Lägg till värdet av x sist i listan
    x = int(input('Nästa: '))
print('Inmatad lista: ', numbers) # Skriv ut hela listan

while x < len(numbers):
    if numbers[x] % 2 == 0:
        evennumbers.append(numbers[x])
    x += 1
print(f'Dessa är de jämna talen i listan {evennumbers} de är {len(evennumbers)} till antalet')

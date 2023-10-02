kapital = int(input("Vad är ditt nuvarande kapital? "))
tid = int(input("Hur lång är din sparhorisont? "))
räntesats = float(input("Vad är din förväntade årliga tillväxt i procent? "))/100

tillväxt = kapital*((1+räntesats)**tid)

print(f'Ditt slutgiltliga kapital efter {tid} år med en förväntad till växt på {int(räntesats*100)}% är {int(round(tillväxt, 0))}')
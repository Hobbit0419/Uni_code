# Studentversion av filen.
# Givet är ett skal till klassen Light
# och kod (funktionen demo_light) som testar klassen Light.
# Fyll i det som saknas i klassen Light sÃ¥ att utskriften nedan fÃ¥s.

class Light:
    """Representerar ett trafikljus"""
    """Se specifikation av klassen på kursens webbbsida"""
    def __init__(self,period, green_period): #konstruktör
        self.period = period # antalet tidssteg mellan två växlingar från grönt till rött och tillbaka
        self.green_period = green_period
        self.internal_time = 0
        
    def step(self):
          self.internal_time = (self.internal_time + 1) % self.period #börjar en ny period vid 7 och det är grön i 3 omgångar
          # påbörjar en ny period
          
    def is_green(self): # retunerar True om grön annars false om röd
        return self.internal_time < self.green_period # mindre än grön perioden och 
    
    def __str__(self): # om ovan är true då g annars r
        return '(G)' if self.is_green() else '(R)'
    
def demo_light():
    """För demonstration av klassen Light"""
    a_light = Light(7, 3) # Skapar ett trafikljus, period 7, green time 3 
    # Simulera 15 tidssteg
    for t in range(15):
        print(t+1, a_light, a_light.is_green())
        a_light.step() # Nästa steg för trafikljuset

def demo_light():
    """För demonstration av klassen Light"""
    a_light = Light(7, 3) # Skapa ett trafikljus, period 7, green time 3
    # Simulera 15 tidssteg
    for t in range(15):
        print(t+1, a_light, a_light.is_green())
        a_light.step() # NÃ¤sta steg fÃ¶r trafikljuset

def main():
    print('\nLight demonstration')
    demo_light()

if __name__ == '__main__':  # If this file is the main program, you are running:
    main()                  # Call the main function above
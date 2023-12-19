# Given studentversion av:
# Trafik system 1
# Två filer (lane1, lane2) och ett trafikljus (light) mellan dem.
# Och en kö, före lane2..
# lane1 - light - lane2 - kö
# Uppgift:
# I klassen TrafficSystem1 skall metoden number_in_system()
# modifieras.

from fVehicleAndLane_Stud import Lane, Vehicle
from fLight_Stud import Light
from fDestinations import Destinations
from time import sleep  # behövs för sleep-fkn


class TrafficSystem1:
    """Representerar ett trafik system"""

    # Konstruktorn
    def __init__(self):
        self.time = 0   # Tiden är noll, initialt
        self.lane1 = Lane(5)  # Fil efter trafikljuset
        self.lane2 = Lane(5)  # Fil framför trafikljuset
        self.light = Light(10, 8) # Trafikljus, period 10, green period 8
        self.queue = [] # Kön längst till höger är initialt tom
        self.generator = Destinations() # skapar ett Destinations-objekt

    # Skriver ut trafiksystemet vid aktuell tid som exvis
    #   26: [WSSSW](G)[SWWSW]  ['W', 'S']
    # dvs tiden, filen efter trafikljuset, trafikljuset, filen framför trafikljuset, kön
    def snapshot(self):
        # Skapa en sträng som representerar kön
        sq = str([x.get_destination() for x in self.queue])
        # Skapa en sträng med värdet på self.time högerjusterat över 4 positioner
        stime = '%4d' % (self.time) + ": "
        snr = '%2d' % (self.number_in_system())
        # Bygg upp strängen med alla dess beståndsdelar
        s = stime + '('+snr+') ' + str(self.lane1) + str(self.light) + str(self.lane2) + "  " + sq
        print(s)
        
    # Stegar trafiksystemet från vänster till höger
    def step(self):
        self.time += 1
        self.lane1.remove_first() # Tag bort fordon först i lane1
        self.lane1.step()         # Stega lane1 
        if self.light.is_green(): # Om trafikljuset är grönt...
            # Flytta fordonet från lane2 till lane1
            self.lane1.enter(self.lane2.remove_first())
        self.light.step() # Stega trafikljuset
        self.lane2.step() # Stega lane2

        # Nytt fordon vid detta tidssteg?
        destination = self.generator.step() # Ger S, W eller None från generatorn
        if destination != None: # Om nytt fordon:
            # Skapa fordonet och lägg det sist i kön
            self.queue.append(Vehicle(destination, self.time))

        # Om det finns minst ett fordon i kön OCH sista positionen i lane2 är ledig:
        if len(self.queue) > 0 and self.lane2.last_free():
            # Flytta fordonet från första position i kön till sista position i lane2.
            self.lane2.enter(self.queue.pop(0))

    # Beräknar och returnerar hur många fordon som för tillfället finns i trafikssystemet
    # dvs summan av fordon i de båda filerna (lane1, lane2) och i kön (queue).
    # Denna metod skall modifieras
    def number_in_system(self):
        vehicle_amount = self.lane1.number_in_lane() + self.lane2.number_in_lane() + len(self.queue)
        return vehicle_amount


# Funktion som testkör TrafficSystem1
def main():
    ts = TrafficSystem1()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.1) # Vänta 100 ms
    print('\nFinal state:')
    ts.snapshot()
    
# Testkör main
# if __name__ == '__main__':
main()
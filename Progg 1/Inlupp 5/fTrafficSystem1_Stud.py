from fVehicleAndLane_Stud import Lane, Vehicle
from fLight_Stud import Light
from fDestinations import Destinations
from time import sleep



class TrafficSystem1:

    # Konstruktorn
    def __init__(self):
        self.time = 0   # Tiden är noll, initialt
        self.lane1 = Lane(5)  # Fil efter trafikljuset
        self.lane2 = Lane(5)  # Fil framför trafikljuset
        self.light = Light(10, 8) # Trafikljus, period 10, green period 8
        self.queue = [] # Kön längst till höger är initialt tom
        self.generator = Destinations() # skapar ett Destinations-objekt


    # Skriver ut trafiksystemet vid aktuell tid som exvis
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
            self.lane1.enter(self.lane2.remove_first()) #Flytta fordonet från lane2 till lane1

        self.light.step() #Stega trafikljuset
        self.lane2.step() #Stega lane2

        # Nytt fordon vid detta tidssteg?
        destination = self.generator.step() # Ger S, W eller None från generatorn
        if destination != None: # Om nytt fordon:
            self.queue.append(Vehicle(destination, self.time)) #Skapa fordonet och lägg det sist i kön

        # Om det finns minst ett fordon i kön OCH sista positionen i lane2 är ledig:
        if len(self.queue) > 0 and self.lane2.last_free():
            self.lane2.enter(self.queue.pop(0)) #Flytta fordonet från första position i kön till sista position i lane2.


    # Beräknar och returnerar hur många fordon som för tillfället finns i trafikssystemet
    def number_in_system(self):
        vehicle_amount = self.lane1.number_in_lane() + self.lane2.number_in_lane() + len(self.queue)
        return vehicle_amount



# Funktion som testkör TrafficSystem1
def main():
    ts = TrafficSystem1()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.001)
    print('\nFinal state:')
    ts.snapshot()

if __name__ == '__main__':
    main()
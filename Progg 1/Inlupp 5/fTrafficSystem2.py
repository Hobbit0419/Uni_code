from fVehicleAndLane_Stud import Lane, Vehicle
from fLight_Stud import Light
from fDestinations import Destinations
from time import sleep  
from statistics import *



class TrafficSystem2:
    # Konstruktorn
    def __init__(self):
        self.time = 0
        self.lane = Lane(11)
        self.laneW = Lane(8)
        self.laneS = Lane(8)
        self.lightW = Light(14, 6)
        self.lightS = Light(14, 4)
        self.queue = [] #Kön längst till höger är initialt tom
        self.queue_time = 0 #Räknare som registrerar antal gånger kö bildas
        self.generator = Destinations() #Skapar ett Destinations-objekt
        self.block = '' #Tecken för att indikera blockageering i delningspunkten
        self.timesBlocked = 0 #Räknare för antal gånger det uppstår blockering
        self.exitS = [] #Fordorn som lämmnar systemet med destination South
        self.exitW = [] #Samma som ovan fast West
        self.total_cars = 0
 
    
    def snapshot(self): # Skriver ut trafiksystemet vid aktuell tid som exvis

        sq = str([x.get_destination() for x in self.queue]) # Skapa en sträng som representerar kön

        stime = '%4d' % (self.time) + ": "# Skapa en sträng med värdet på self.time högerjusterat över 4 positioner

        snr = '%2d' % (self.number_in_system()) # Antal fordon i systemet

        # Bygg upp två strängar med alla dess beståndsdelar
        s1 = stime + '('+snr+') ' + str(self.lightW) + ' ' + str(self.laneW)\
            + str(self.block) + str(self.lane) + "  " + sq
        s2 = str(self.lightS) + ' ' + str(self.laneS)
        print(s1)
        print('          ', s2)
        
    
    def step(self): #Stegar trafiksystemet från vänster till höger, om det finns 
        
        self.time += 1
        lane = str(self.lane)
        
        #Nedanstående ifsatser kollar ljusen och låter bilar köra om det är grönt 
        if self.lightS.is_green():
            laneS = str(self.laneS)
            if self.lightS.is_green(): 
                if laneS[1] == 'S': 
                    self.exitS.append(self.time - self.laneS.get_first().get_borntime()) #"Skriver ner" tiden det tog för bilen att komma till sin destination                
                self.laneS.remove_first() 
        
        
        if self.lightW.is_green():
            laneW = str(self.laneW)
            if self.lightW.is_green(): 
                if laneW[1] == 'W': 
                    self.exitW.append(self.time - self.laneW.get_first().get_borntime())                
                self.laneW.remove_first() 
        
        self.laneS.step()
        self.laneW.step()
        self.lightS.step()
        self.lightW.step()
        
        #Nedanstående ifsatser kollar om det är blockerat
        if lane[1] == 'W' and self.laneW.last_free():
            self.laneW.enter(self.lane.remove_first())
            self.block = ''
        elif lane[1] == 'W' and not self.laneW.last_free(): 
            self.block = '*'
            self.timesBlocked += 1

        if lane[1] == 'S' and self.laneS.last_free(): 
            self.laneS.enter(self.lane.remove_first())
            self.block = '' 
        elif lane[1] == 'S' and not self.laneS.last_free():
            self.block = '*'
            self.timesBlocked += 1

        self.lane.step()

        destination = self.generator.step() #Skapa nya bilar ibland
        if destination != None:
            self.queue.append(Vehicle(destination, self.time))
            self.total_cars += 1

        if len(self.queue) > 0 and self.lane.last_free():
            self.lane.enter(self.queue.pop(0))

        if len(self.queue) > 0:
            self.queue_time += 1

    def number_in_system(self):
        vehicle_amount = self.lane.number_in_lane() + self.laneS.number_in_lane() + self.laneW.number_in_lane() + len(self.queue)
        return vehicle_amount
    
    def print_statistics(self):  #Skapar en metod för att printa statestiken    

        print('\n', f'Statistics after {self.time} timesteps:', '\n')
        print(f'Created vehicles:    {self.total_cars}')
        print(f'In system       :    {self.number_in_system()}\n')

        print('At exit          West         South')
        print(f'Vehicles out:     {len(self.exitW)}           {len(self.exitS)}')
        print(f'Minimal time:     {min(self.exitW)}           {min(self.exitS)}')
        print(f'Maximal time:     {max(self.exitW)}           {max(self.exitS)}')
        print(f'Mean time   :     {round(mean(self.exitW), 1)}         {round(mean(self.exitS), 1)}')
        print(f'Median time :     {round(median(self.exitW), 1)}           {round(median(self.exitS), 1)} \n')
        
        print(f'Blocked     :    {round(((self.timesBlocked/self.time)*100), 1)}%')
        print(f'Queue       :    {round(((self.queue_time/self.time)*100), 1)}%')

        
# Funktion som testkör TrafficSystem2
def main():
    ts = TrafficSystem2()
    for i in range(100):
        ts.snapshot()
        ts.step()
        sleep(0.001) 
    print('\nFinal state:')
    ts.snapshot()
    ts.print_statistics() 
    

main()
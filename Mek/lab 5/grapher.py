import csv
import re
from derivative import dxdt
from matplotlib import pyplot as pp
import numpy as np
from os import listdir

class Lab5:
    def __init__(self, inputdir = ""):
        self.inputfiles = listdir(inputdir)
        self.inputdir = inputdir
        self.ch1 = []
        self.ch2 = []
        self.ch1v = []
        self.ch2v = []
        self.data = []
        self.time = []
        self.files = []

    def csv_reader(self, file_name):
        self.ch1 = []
        self.ch2 = []
        self.time = []

        input_file = open(file_name, 'r')
        
        data_rows = csv.reader(input_file, delimiter=';')
        for row in data_rows:
            self.data.append(row)   

    def data_separator(self):
        for line in self.data:
            self.time.append(line[0])
            self.ch2.append(line[1])
            self.ch1.append(line[2])
        self.time.pop(0)
        self.ch1.pop(0)
        self.ch2.pop(0) 

    def data_cleaner(self):
        for n in range(len(self.ch1)):
            if self.ch1[n] == '':
                self.ch1[n] = self.ch1[n - 1]
        for n in range(len(self.ch1)):
            if self.ch1[n] == '':
                self.ch1[n] = self.ch1[n - 1]
        for n in range(len(self.ch2)):
            if self.ch2[n] == '':
                self.ch2[n] = self.ch2[n - 1]
        for n in range(len(self.ch2)):
            if self.ch2[n] == '':
                self.ch2[n] = self.ch2[n - 1]
        for n in self.ch1:
            self.ch1[self.ch1.index(n)] = re.sub(',', '.', n)
        for n in self.ch2:
            self.ch2[self.ch2.index(n)] = re.sub(',', '.', n)
        for n in self.time:
            self.time[self.time.index(n)] = re.sub(',', '.', n)    

        self.time = list(map(float, self.time))
        self.ch1 = list(map(float, self.ch1))
        self.ch2 = list(map(float, self.ch2))
        self.time = np.array(self.time)
        self.ch1 = np.array(self.ch1)
        self.ch2 = np.array(self.ch2)
        self.ch1v = dxdt(self.ch1, self.time, kind="savitzky_golay", left=.5, right=.5, order=3)
        self.ch2v = dxdt(self.ch2, self.time, kind="savitzky_golay", left=.5, right=.5, order=3)

    def data_reader(self, file):
        self.csv_reader(file)
        self.data_separator()
        self.data_cleaner()
        self.data = []

    def data_illustrator(self):
        for file in self.inputfiles:
            title = file.replace('.csv', '')
            self.data_reader(self.inputdir + file)
            pp.plot(self.time, self.ch1v, label='Hastighet')
            pp.plot(self.time, self.ch1, label='Avstånd till givare')
            pp.ylabel('avstånd(m) & hastighet(m/s)')
            pp.xlabel('tid(s)')
            pp.title(f'Försök {file} vagn B')
            pp.legend()
            pp.savefig(f'försök_{title}_vagn_b.png')
            pp.close()
            pp.plot(self.time, self.ch2v, label='Hastighet')
            pp.plot(self.time, self.ch2, label='Avstånd till givare')
            pp.ylabel('avstånd(m) & hastighet(m/s)')
            pp.xlabel('tid(s)')
            pp.title(f'Försök {title} vagn A')
            pp.legend()
            pp.savefig(f'försök_{title}_vagn_a.png')
            pp.close()

    def debugg(self):
        for file in self.inputfiles:
            title = file.replace('.csv', '')
            self.data_reader(self.inputdir + file)
        print(self.ch1, self.ch2)

test = Lab5('Uni_code/Mek/lab 5/data/')

test.data_illustrator()
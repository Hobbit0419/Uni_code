import csv
from icecream import ic
from matplotlib import pyplot as pp

def smooth(list_a, n):
    output_list = []
    for i in range(len(list_a)):
        if i + 1 + n > len(list_a):
            output_list.append((sum(list_a[i-n:]) + ((i+n - len(list_a)+1)*list_a[-1]))/(2*n+1)) #hanterar randvärden åt höger
            print(list_a[i-n:])
        elif i - n < 0:
            output_list.append((sum(list_a[:i+n+1]) + (abs(2*i-n)*list_a[0]))/(2*n+1)) #hanterar randvärden åt vänster
        else:
            output_list.append(sum(list_a[i-n:i+n+1])/(2*n+1)) #alla icke randvärden
    return output_list

def csv_reader(file_name):
    input_file = open(file_name, 'r')
    data = {}
    
    data_rows = csv.reader(input_file)
    for row in data_rows:
        data[str.lower(row[1])] = list(map(float, row[3:]))
    return data
        
def data_illustrator(input_data):
    countries = ['dnk', 'fin', 'isl', 'nor', 'swe']
    colors = ['red', 'green', 'yellow', 'blue', 'purple']

    for country in zip(countries, colors):
        smooth_data = smooth(input_data[country[0]], 5)
        pp.plot(input_data['country code'] ,input_data[country[0]], linestyle = 'dotted', color = country[1])
        pp.plot(input_data['country code'] ,smooth_data, color = country[1])   
    pp.show() 
        
CO2_data = csv_reader('Progg 1/Inlupp 4/CO2Emissions_filtered.csv')

data_illustrator(CO2_data)
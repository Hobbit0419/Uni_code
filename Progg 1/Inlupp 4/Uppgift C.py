from numpy import average
from matplotlib import pyplot as pp

def data_import(input_file):
    data_list = []
    output_dic = {}
    file = open(input_file, 'r')
    for line in file:
        data = line.split(' ')
        while("" in data):
            data.remove("")
        while("1\n" in data):
            data.remove("1\n")
        data_list.append( list(map(int, data[:3])) + (list(map(float, data[3:]))))
        
    for entry in data_list:
        if entry[0] in output_dic:
            output_dic[entry[0]].append(entry[1:])
        else:              
            output_dic[entry[0]] = []
            output_dic[entry[0]].append(entry[1:])
    return output_dic

def yearly_average_temp(input, month = 5, year_range = [1722, 2022]):
    average_temp = {}
    for year in range(year_range[0], year_range[1] + 1):
        temp_list = []
        for temp in input[year]:
            if temp[0] == month:
                temp_list.append(temp[2])
        average_temp[year] = average(temp_list)
    return(average_temp)
                
def plotter(input):
    plotting_data = {17:[], 18:[], 19:[], 20:[]}
    data_array = []
    for year in input:
        if year <= 1799:
            plotting_data[17].append(input[year])
        elif year <= 1899:
            plotting_data[18].append(input[year])
        elif year <= 1999:
            plotting_data[19].append(input[year])
        else:
            plotting_data[20].append(input[year])
    
    for centry in plotting_data:
           data_array.append(plotting_data[centry])
           
    fig, ax = pp.subplots()
    ax.boxplot(data_array)
    pp.xticks([1, 2, 3, 4], [1700, 1800, 1900, 2000])
    pp.title('Medeltemperatur på några platser i maj, 1722-2022')
    pp.ylabel('Temperaturspridning')
    pp.xlabel('Bergström, H., and Moberg, A.: 2002, Daily air temperature and pressure series for Uppsala 1722-1998. \n Climatic Change, 53, 213-252')            
    pp.show()

test = data_import('Progg 1/Inlupp 4/uppsala_tm_1722-2022.dat')
test_1 = yearly_average_temp(test)
plotter(test_1)
import pandas as pd
import numpy as np
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def gaussian(x, amplitude, mean, stddev):
    return amplitude * np.exp(-((x - mean) / stddev)**2)


def plot_maker(file):
    # Load the CSV file
    data = pd.read_csv(file, sep=';', decimal=',', dtype={'Channel n': int, 'Events N': int})

    channel_numbers = np.array(data['Channel n'], dtype=int)
    number_of_events = np.array(data['Events N'], dtype=int)

    # Calibrate x-axis
    energy = (channel_numbers * 35.729032258064514 - 1064.3677419354826) / 1000 

    #find peaks
    peaks, _ = find_peaks(number_of_events, height=70, width=15, distance=20)


    peak_centers = []
    peak_uncertainties = []
    window_sizes = []

    # Define colors for the plots
    colors = ['springgreen', 'deepskyblue', 'lightpink']
    color_counter = 0

    fig, ax = plt.subplots()

    # Fit gaussians to peaks
    for peak in peaks:

        # Initial window size
        window_size = 40

        # Iterate over window sizes in order to be able to fit more peaks
        while window_size > 1:  
            
            # Calculate the window limits and extract windows
            window_start = max(0, peak - window_size)
            window_end = min(len(energy), peak + window_size)
            x_window = energy[window_start:window_end]
            y_window = number_of_events[window_start:window_end]

            # Make initial guess for the curve fit
            initial_guess = [y_window.max(), energy[peak], 1]

            # Try to fit the gaussian
            try:
                popt, pcov = curve_fit(gaussian, x_window, y_window, p0=initial_guess)
                peak_centers.append(popt[1])
                peak_uncertainties.append(np.sqrt(pcov[1, 1]))
                window_sizes.append(window_size)
                ax.plot(x_window, gaussian(x_window, *popt), label=f'Fit: Center={popt[1]:.2f}keV $\sigma$ = {popt[-1]:.2f}', color=colors[color_counter])
                color_counter += 1
                break  
            # If gaussian could not be fit reduce window size
            except RuntimeError:
                print(f"Could not fit peak at {peak} with window size {window_size}")
                window_size -= 5  


    #Print the results
    for center, uncertainty in zip(peak_centers, peak_uncertainties):
        print(f"Center: {center}, Uncertainty: {uncertainty}")

    #Finish and show the plot
    ax.plot(energy, number_of_events, label='Data', zorder=1, color=colors[color_counter])
    ax.set_title(file[:-4])
    ax.set_xlabel('Energy (keV)')
    ax.set_ylabel('Events')
    fig.set_figheight(5)
    fig.set_figwidth(10)
    ax.legend()
    fig.savefig(f'figs/{file[:-4]}.png')

files = ['2.csv', '5krona.csv', '7.csv', '10krona.csv', '20eurocent.csv', 'bricka.csv', 'Cu.csv', 'Fe.csv', 'Mo.csv', 'Ti.csv']

for file in files:
    plot_maker(file)
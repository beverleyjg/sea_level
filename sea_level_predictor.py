import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    df.info()
    print(df.head)

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y, label = 'original data', s = 0.2)

    print(len(x), " vs ", len(y))
    print('y original: ', y)

    # Create first line of best fit
    fit1 = linregress(x, y)

    xtend = np.arange(1880,2051,1)
    yfit1 = fit1.intercept + fit1.slope*xtend
    plt.plot(xtend, yfit1, 'b', label = 'first fit: based on 1880 onwards')
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # Create second line of best fit
    x_cut, y_cut = df[df['Year'] >= 2000]['Year'], df[df['Year'] >= 2000]['CSIRO Adjusted Sea Level']
    fit2 = linregress(x_cut, y_cut)
    xtend2 = np.arange(2000,2051,1)
    plt.plot(xtend2, fit2.intercept + fit2.slope*xtend2, 'g', label = 'second fit: based on 2000 onwards')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
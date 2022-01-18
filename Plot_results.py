

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from matplotlib.dates import AutoDateFormatter, AutoDateLocator
from matplotlib.ticker import MaxNLocator
#plot results
def plot_results(dates,hours):
            plt.style.use('own_plot_style.mplstyle')
            #sort results
            zipped = zip( dates,hours) #zip lists
            tuples = zip(*sorted(zipped)) #make tuplse
            dates,hours = [ list(tuple) for tuple in  tuples] #divide to two list
            #make figure and plot
            fig, ax = plt.subplots(figsize=(14,10))
            xtick_locator = AutoDateLocator()
            xtick_formatter = AutoDateFormatter(xtick_locator)
            ax = plt.axes()
            ax.xaxis.set_major_locator(xtick_locator)
            ax.xaxis.set_major_formatter(xtick_formatter)
            ax.yaxis.set_major_locator(MaxNLocator(integer=True))
            ax.plot(dates,hours,'-o', label="Studied in hours")
            plt.grid(True)
            plt.title("Stats")
            plt.xlabel("Date")
            plt.ylabel("Time studied (Hours)")
            plt.legend()
            plt.show()
            
            
        

import numpy as np
import matplotlib.pyplot as plt
import textwrap

#reading txt files (data is already in Volts)
data = np.genfromtxt("data.txt",comments="\n")
settings = np.genfromtxt("settings.txt",comments="\n")

# init times
times = np.linspace(0, settings, len(data))

# init figure
fig = plt.figure()
ax = fig.add_subplot(111)

# init axes
ax.set_xlim([min(times), 1.05*max(times)])
ax.set_ylim([min(data), 1.05*max(data)])

# init title
location = ['center', 'left', 'right']
myTitle = "Data analysis (capacitor charging-discharging)"
ax.set_title("\n".join(textwrap.wrap(myTitle, 80)), loc =location[0])
ax.set_xlabel('time, s')
ax.set_ylabel('voltage, V')

# plotting data: (linestyle, linewidth, color) 
plt.plot(times, data,
        linestyle = '-',
        linewidth = 1,
        color = 'darkblue',
        marker='.',
        mew = 2,
        markevery = 50,
        label = 'Voltage(t)')
plt.legend()

# add a grid  
plt.minorticks_on()      
plt.grid(which='major', color='lightgrey', linestyle='-', linewidth=1)
plt.grid(which='minor', color='lightgrey', linestyle='--', linewidth=0.5) 

# add a text
plt.text(78, 2.5,"charging time = {: .2f}".format(times[np.argmax(data)]))
plt.text(78, 2,"discharging time = {: .2f}".format(settings - times[np.argmax(data)]))

# save plot
plt.savefig('plotted_data.svg')
plt.show()

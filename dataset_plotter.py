""" dataset_plotter.py, March 2019

A program that obtains data using dataset_reader.py and plots it

Created for a Digital Technology data analytics assignment
"""

import numpy as np
import matplotlib.pyplot as plt
import dataset_reader as data # This is the module I created

''' Constants '''
# Maxiumum and minimum constants for the graph
XMIN = 2005
XMAX = 2020

''' Obtaining and Organising Data '''

# Create data objects for everything
flow_to_sa = data.DatasetReader('data/flowtosa_historical_1403.csv', 0, 1)
falls_creek_rainfall = data.DatasetReader('data/daily_rainfall_falls_creek.csv', 2, 5)
yaouk_rainfall = data.DatasetReader('data/daily_rainfall_yaouk.csv', 2, 5)

# Obtain x and y values using the objects, and the iterations
x1 = flow_to_sa.get_years()
y1 = flow_to_sa.get_total()
z1 = flow_to_sa.get_iterations()

x2 = falls_creek_rainfall.get_years()
y2 = falls_creek_rainfall.get_total()
z2 = falls_creek_rainfall.get_iterations()

x3 = yaouk_rainfall.get_years()
y3 = yaouk_rainfall.get_total()
z3 = yaouk_rainfall.get_iterations()

# Combine the data
c = []
d = []

## Get every single year between Falls Creek and Yaouk
for i in x2:
	c.append(i)
	for j in x3:
		c.append(j)
c = list(set(c)) # Remove duplicates and order from lowest to highest

## Get every single total, and count the iterations
for i in range(len(c)):
	year = c[i]
	d.append([0, 0]) # Create a blank entry
	
	# Iterate through Falls Creek Rainfall and find all approprate data
	for j in range(len(x2)):
		if year == x2[j]:
			d[i][0] += y2[j]
			d[i][1] += 1
	
	# Iterate through Yaouk Rainfall and find all approprate data
	for k in range(len(x3)):
		if year == x3[k]:
			d[i][0] += y3[k]
			d[i][1] += 1

## Average out data
d_av = []

for i in d:
	d_av.append(i[0]/i[1])

## Flow to SA vs Average
a = []
b = []

## This aligns itself with the data from Flow to SA
## e.g., it only uses the years present in flow_to_sa
for i in range(len(x1)):
	for j in range(len(c)):
		# Determine which values have the same year
		# This is done to match up data with the appropriate year
		if x1[i] == c[j]:
			a.append(d_av[j]) # Rainfall
			b.append(y1[i]) # Water Flow

## Iteration table ##
# Shows reliability of data

# Flow to SA
print('\nFlow to SA')
print('Year:\t|\tIterations:')
print('========|=============')
for i in range(len(x1)):
	print(str(x1[i]) + '\t|\t' + str(z1[i]))

# Falls Creek Rainfall
print('\nFalls Creek Rainfall')
print('Year:\t|\tIterations:')
print('========|=============')
for i in range(len(x2)):
	print(str(x2[i]) + '\t|\t' + str(z2[i]))

# Yaouk Rainfall
print('\nYaouk Rainfall')
print('Year:\t|\tIterations:')
print('========|=============')
for i in range(len(x3)):
        print(str(x3[i]) + '\t|\t' + str(z3[i]))

''' Plot the Data '''

## Line/Scatter Graphs ##
# Shows relationship between rainfall and water flow

# Flow to SA
plt.subplot(2, 2, 1)
plt.plot(x1, y1, 'o-', color='red')
plt.title('Water Flow To SA')
plt.ylabel('Discharge (ML)')
plt.grid(True)
plt.xlim(xmin=XMIN, xmax=XMAX)

# Falls Creek Rainfall
plt.subplot(2, 2, 2)
plt.plot(x2, y2, 'o-', color='blue')
plt.title('Falls Creek Rainfall')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.xlim(xmin=XMIN, xmax=XMAX)

# Yaouk Rainfall
plt.subplot(2, 2, 3)
plt.plot(x3, y3, 'o-', color='#ff8d8d')
plt.title('Yaouk Rainfall')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.xlim(xmin=XMIN, xmax=XMAX)

# Average Rainfall vs Water Flow to SA
plt.subplot(2, 2, 4)
plt.plot(a, b, 'o', color='#318037')
plt.title('Rainfall vs Water Flow')
plt.xlabel('Average Rainfall (mm)')
plt.ylabel('Water Flow to SA (ML)')
plt.grid(True)
#plt.ylim(ymin=0)

## Trendline calculation, taken from:
## https://stackoverflow.com/questions/26447191/how-to-add-trendline-in-python-matplotlib-dot-scatter-graphs
z = np.polyfit(a, b, 1)
p = np.poly1d(z)
plt.plot(a, p(a), '-', color='#8a0000')
print("y = %.3fx + %.3f"%(z[0],z[1])) # Line equation

plt.tight_layout() # Formatting
plt.show() # Display the graphs

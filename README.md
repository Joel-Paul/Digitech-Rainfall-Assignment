# Digitech-Rainfall-Assignment
A program I created for my Digital Technologies assignment in 2019. It takes rainfall and water flow data from .csv files and graphs them.

The purpose of this script was to compare the rainfall at various locations with the water flow into South Australia, and then analyse the data.
The purpose of `dataset_reader.py` is to look through a given .csv file and extracts whatever information is requested, though it does not display it in any way.
`dataset_plotter.py` takes the output of `dataset_reader.py`, performs calculations such as averaging values, and plots the data using `matplotlib`.

This is the graphical output of this program:

![image](https://user-images.githubusercontent.com/37064691/102040227-4ad0b700-3e20-11eb-8717-bb4810dc515e.png)

I apologise that the code isn't as clean as I would like it to be, but I wanted to keep it how I originally wrote the code back in 2019.
This program was originally made using Pythonista 3 for iOS (https://apps.apple.com/us/app/pythonista-3/id1085978097).

## Requirements
* numpy
* matplotlib

## Running
Run `dataset_plotter.py` from the command line.
(e.g. `python dataset_plitter.py`)

## Sources of Data
* The water flow into South Australia was downloaded from the Murray-Darling Basin Authority website, at:
https://riverdata.mdba.gov.au/sites/default/files/liveriverdata/csv/flowtosa_historical.csv
* The rainfall at Yarrawonga Weir Upstream was obtained from:
https://riverdata.mdba.gov.au/sites/default/files/liveriverdata/csv/409216a_historical.csv
* The rainfall from Falls Creek and Yaouk were obtained from:
http://www.bom.gov.au/climate/data/

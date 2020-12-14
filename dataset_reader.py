""" dataset_reader.py, 18 March 2019

A program that reads a CSV file that contains information about various datasets

Created for a Digital Technology data analytics assignment
An improvement over csv_reader, with 'cleaner' code
"""

import csv

class DatasetReader():
	'Runs when the class is initialised'
	def __init__(self, file, year_column, data_column):
		self.year_dict = {} # Dictionary to hold data values
		
		# Open the data file
		with open(file) as csv_file:
			csv_reader = csv.reader(csv_file, delimiter=',') # Object to read CSV file
			
			## Obtain the data
			# Go through each row and find the year
			for row in csv_reader:
				try:
                                        # Takes the last four characters from the cell and tries to read it as the year
					# If this is not an integer it will cause an error which will be caught
					# If it is an integer, we will assume it's the year
					year = int(row[year_column][-4:])
					
					# Only obtain data from dates with valid entries
					# Valid entries must have a number
					if row[data_column] == '':
						## If the entry is not valid, skip it by causing an error
						# Not a very clean way to exit this, but oh well
						int('Cause an error because I don\'t know how to exit this')
						
					else:
						## Else save the data as a float
						daily_data = float(row[data_column]) # The data for that day
					
					try:
						# If the dictionary item already exists, append to it
						self.year_dict[year][0] += daily_data # The total data for this year
						self.year_dict[year][1] += 1 # Number of times this year is recorded
					except KeyError as e:
						# Otherwise create a new dictionary item
						self.year_dict[year] = [daily_data, 1]
					
				except ValueError as e:
					# Ignore the row if there is no integer (year)
					#print(e)
					pass
	
	'Returns a list of years for this data set'
	def get_years(self):
		years = []
		for year in self.year_dict:
			years.append(year)
			
		return years
	
	'Returns a list of the total data for each year'
	def get_total(self):
		total = []
		years = self.get_years()
		
		for year in years:
			total.append(self.year_dict[year][0])
			
		return total
	
	'Returns a list of the number of times each year is recorded'
	def get_iterations(self):
		iterations = []
		years = self.get_years()
		
		for year in years:
			iterations.append(self.year_dict[year][1])
			
		return iterations
	
	'Returns a list of the average data for each year by dividing the total by the iterations'
	def get_rate(self):
		rate = []
		total = self.get_total()
		iterations = self.get_iterations()
		
		for i in range(len(total)):
			rate.append(total[i]/iterations[i])
		
		return rate

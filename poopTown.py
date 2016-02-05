import pandas as pd 

input_dataframe = pd.read_csv('lecz-urban-rural-population-land-area-estimates_codebook.csv')

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv', 'rU') as inputFile:
		inputReader = csv.reader(inputFile)
		for line in inputReader:
			print(line)
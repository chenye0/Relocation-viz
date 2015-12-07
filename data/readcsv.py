import csv

# with open('Weather.csv') as f:
# 	weather = f.readlines()
# print weather

f = open('Weather.csv')
csv_f = csv.reader(f)

for row in csv_f:
	print row
# for row in csv_f:
# 	print row,csv_f.length
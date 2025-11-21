import csv
 
file='PathFinder_Raw_Data/Watermaze_output/31-1.csv'

csvfil = csv.DictReader(file)

print(dir(csvfil))

print(csvfil.fieldnames)

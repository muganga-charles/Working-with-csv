import csv
house=set()
with open ('Greenhouse.csv',"r", encoding='UTF') as file:
    reader=csv.DictReader(file)

    for row in reader:
        house.add(row['region'].strip().upper())


    for houses in sorted(house):
        print(houses)#prints the sorted list of houses without repeating
    
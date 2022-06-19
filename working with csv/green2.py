import csv
house={}
with open ('Greenhouse.csv',"r", encoding='UTF8') as file:
    reader=csv.DictReader(file)

    for row in reader:
        place=row['region'].strip().upper()
        if place in house:
            house[place]+=1
        else:
            house[place]=1
            

    def sorted_houses(place):
        return house[place]

    for i in sorted(house ,key=sorted_houses,reverse=True):
        print(i,house[i])
    
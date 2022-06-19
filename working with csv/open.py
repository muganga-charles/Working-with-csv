import csv
# count = 0
# with open("gross movies.csv","r" , encoding='UTF8') as file:
#     reader=csv.reader(file)
#     next(reader)
#     for row in reader:
#         count += 1
#         print(row[0])


# movies ={}
# with open("gross movies.csv","r" , encoding='UTF8') as file:
#     reader=csv.DictReader(file)
    
#     for row in reader:
#         print(row['Film'])
"""
prints in accending order and with no duplicate
"""
# films =set()
# with open("gross movies.csv","r" , encoding='UTF8') as file:
#     reader=csv.DictReader(file)
    
#     for row in reader:
#         films.add(row['Film'].strip().upper())

#     for film in sorted(films):
#         print(film)    
        
"""
prints with a count
"""
films ={}
with open("gross movies.csv","r" , encoding='UTF8') as file:
    reader=csv.DictReader(file)
    
    for row in reader:
        film=(row['Film'].strip().upper())
        if film in films:
            films[film] += 1
        else:
            films[film] = 1    
    def f(film):
        return films[film]

    for film in sorted(films,key=f,reverse=True):
        print(film, films[film])


    
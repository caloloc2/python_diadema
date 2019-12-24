import csv

def exportar_csv(data, nombre_archivo):
    myFile = open(nombre_archivo, 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(data)
    return True

myData = [["first_name", "second_name", "Grade"],
          ['Alex', 'Brian', 'A'],
          ['Tom', 'Smith', 'B']]

if (exportar_csv(myData, 'calolo.csv')):
    print "Hecho"
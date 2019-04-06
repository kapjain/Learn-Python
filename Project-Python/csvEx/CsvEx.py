import csv

# export to csv https://djangotricks.blogspot.in/2013/12/how-to-export-data-as-excel.html
#initial data data 2017/12/29 4 5 red
#to read CSV data in from a file and then use it in Python. For this, we use the csv module. CSV literally stands for comma separated variable, where the comma is 
#what is known as a "delimiter." While you can also just simply use Python's split() function, to separate lines and data within each line, the CSV module can also be
# used to make things easy.

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    print(type(readCSV))
    for row in readCSV:
        print(row)
        #print(row[0])
        #print(row[0],row[1],row[2],)

with open('example.csv','w') as csvfile:
    writeCSV = csv.writer(csvfile, delimiter=',')
    seq = [['First row', 'Foo', 'Bar', 'Baz'],['First row', 'Foo', 'Bar', 'Baz']]
    for row in seq:
        writeCSV.writerow(row)

input("wait here")
#Above, we've shown how to open a CSV file and read each row, as well as reference specific data on each row.
#Next, we will show how to pull out specific data from the spreadsheet and save it to a list variable:

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

#Once we have this data, what can we do with it? Maybe we are curious about what color something was on a specific date.


with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:') #red
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate) # 1/2/2014
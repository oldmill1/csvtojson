import csv

SETTINGS = {
    'csv_file': 'strings.csv',
    'to_language': 'de'
}

f = open('%s.json' % SETTINGS['to_language'], 'wb')

csvfile = open(SETTINGS['csv_file'], 'rU')
csvFileArray = []

for row in csv.reader(csvfile, delimiter=","):
    csvFileArray.append(row)

fileData = "{"

for index in range(len(csvFileArray)):
    formattedData = csvFileArray[index]
    translatedData = formattedData[2]
    fileData = fileData + "\n" + '"' + formattedData[0] + '": "' + translatedData + '",'

fileData = fileData + "\n}"

with f:
    f.write(fileData)

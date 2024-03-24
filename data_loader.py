import csv

# import pandas as pd
# xlsx_file = pd.read_excel('Questions.xlsx')
# xlsx_file.to_csv('Questions.csv', index=False)


def column_to_list(csv_file, column_name):
    values = []
    i=0
    with open(csv_file, 'r', encoding='utf-8') as file:  # Specify the encoding
        print("Open")
        reader = csv.DictReader(file)
        for row in reader:
            print(i)
            values.append(row[column_name])
            i+=1
    return values


print("Starting")
column_values = column_to_list('Questions.csv', 'question')
print(column_values)

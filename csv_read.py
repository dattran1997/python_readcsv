import csv

# read file record

with open('./record.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    key = []
    record = []
    for row in csv_reader:
        if line_count == 0:
            key = row
            # print(row)
            line_count += 1
        else:
            record_data = {
                key[0]: row[0],
                key[1]: row[1]
            }

            record.append(record_data)
            line_count += 1
    print(record)


# write file record use record from read file record

with open('records.csv','w', newline='') as csvfile:
    # print('--------------------')
    # print(record)

    #creating  a csv writer object
    csvwriter = csv.writer(csvfile)

    #writing the fields
    csvwriter.writerow(['name','score'])

    # writing the data rows
    

    csvwriter.writerows(rows)





# read file words

with open('./words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    key = []
    words = []
    for row in csv_reader:
        if line_count == 0:
            key = row
            # print(row)
            line_count += 1
        else:
            word_data = {
                key[0]: row[0],
            }

            words.append(word_data)
            line_count += 1
    print(words)
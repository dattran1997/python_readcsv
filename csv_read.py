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

with open('./record.csv','w', newline='') as csvfile:
    # print('--------------------')
    # print(record)

    record_list = []

    new_data = {
        'name': 'dat',
        'score': '10'
    }
    
    # add new data
    record_list.append([new_data['name'], new_data['score']])

    #creating  a csv writer object
    csvwriter = csv.writer(csvfile)

    #writing the fields
    csvwriter.writerow(['name', 'score'])

    # load data
    for data in record:
        record_list.append([data['name'], data['score']])

    # print('-----------')
    # print(record_list)

    # writing the data rows
    csvwriter.writerows(record_list)




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
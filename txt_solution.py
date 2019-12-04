import csv

with open('./txt/record.txt', 'r') as file:
    # remove space between character
    stripped = (line.strip() for line in file)
    # for line in stripped:
    #     print(line)

    lines = (line.split("-") for line in stripped if line)
    # for line in lines:
    #     print(line)

    # write csv file
    with open('record.csv', 'w', newline='') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('name', 'score'))
        writer.writerows(lines)


# with open('./txt/words.txt', 'r') as file:
#     # remove space between character
#     stripped = (line.strip() for line in file)
#     for line in stripped:
#         print(line)

#     lines = (line.split("") for line in stripped if line)
#     for line in lines:
#         print(line)

#     # write csv file
#     with open('words.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerow('question')
#         writer.writerows(lines)


# with open('record.csv') as csv_file:
#     reader = csv.reader(csv_file)
#     mydict = dict(reader)
#     print(mydict)


    
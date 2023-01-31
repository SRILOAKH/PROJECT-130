import csv
dataset_1=[]
dataset_2=[]
with open("dwarf_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)
with open("bright_stars.csv","r") as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)
headers_1=dataset_1[0]
headers_2=dataset_2[0]
stars_data_1=dataset_1[1:]
stars_data_2=dataset_2[1:]
headers=headers_1+headers_2
stars_data=[]
for i in stars_data_1:
    stars_data.append(i)
for i in stars_data_2:
    stars_data.append(i)
with open("merged_dataset.csv", "a+") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(stars_data)

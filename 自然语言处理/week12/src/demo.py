import csv

with open('names.tsv', 'w', newline='') as csvfile:
    fieldnames = ['na', 'id','sentiment','review']
    writer = csv.DictWriter(csvfile,delimiter='\t',fieldnames=fieldnames)

    #writer.writeheader()
    writer.writerow({'na': 3.14159, 'id': 'Beans'})

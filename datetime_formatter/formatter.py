import csv
import sys
import datetime

reader = csv.reader(open('jcrew_factory_purchasedata_20191216.csv'))
writer = csv.writer(open('new_jcrew_factory_purchasedata_20191216.csv', 'wb'), lineterminator='\n')

# skip headers
next(reader)

for row in reader:
  date = row[2]
  d_pattern = '%Y-%m-%d %H:%M:%S.0'
  d = datetime.datetime.strptime(date, d_pattern)
  new_date = d.strftime('%m/%d/%Y %I:%M')
  row[2] = new_date
  writer.writerow(row)
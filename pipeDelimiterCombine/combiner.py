import csv
import sys
import datetime

reader = csv.reader(open('TX_boot_Order_history_20191209114456.csv'))
writer = csv.writer(open('TX_boot_orders_combined.csv', 'wb'), lineterminator='\n')




temp = {}

writer.writerow(['order_id', 'email', 'created',  'order_total', 'product_ids'])
# build our set of rows in temp
# skip headers
next(reader)

for row in reader:
    # if we are n the nth row of a known order, update product ID + total
    # in source file order ID is in 2nd indexi
    # pdb.set_trace()
    if temp.get(row[0], None):
        temp[row[0]][3] = float(temp[row[0]][3]) + float(row[3])
        temp[row[0]][4] = temp[row[0]][4] + '|' + row[4]
    else:
        # only write columns that\
        date = row[2] 
        d = datetime.datetime.strptime(date, '%m/%d/%Y %H:%M:%S %p')
        new_date = d.strftime('%m/%d/%Y %I:%M')
        # new_date = 'whattup'
        # print('new_date', new_date)
        temp[row[0]] = [row[0], row[1], new_date, row[3], row[4]]


# print(temp)

for attr, val in temp.items():
    # print(val[2])    
    writer.writerow(val)



import xml.etree.ElementTree as ET
import csv
import datetime

tree = ET.parse("./2-year-feed.xml")
root = tree.getroot()



# open a file for writing
ariat_uk = open('./ariat_uk_2-year-feed.csv', 'w')
ariat_de = open('./ariat_de_2-year-feed.csv', 'w')
ariat_fr = open('./ariat_fr_2-year-feed.csv', 'w')

print('creating or opening CSV files')
# create the csv writer object
csvwriter_uk = csv.writer(ariat_uk)
csvwriter_de = csv.writer(ariat_de)
csvwriter_fr = csv.writer(ariat_fr)

head = ['email', 'products', 'order id', 'total', 'purchase date', 'country']

csvwriter_uk.writerow(head)
csvwriter_de.writerow(head)
csvwriter_fr.writerow(head)

print('looping through xml file...')
for order in root.findall('order'):
    country = order.find('customer-locale').text
    row = []
    email = order.find('customer').find('customer-email').text
    row.append(email)

    productList = order.find('product-lineitems')
    prodArr = []
    for product in productList:
      prodArr.append(product.find('product-id').text.split('_')[0])
    row.append(('|').join(prodArr))

    orderId = order.find('original-order-no').text
    row.append(orderId)

    total = order.find('totals').find('order-total').find('gross-price').text
    row.append(total)

    purchaseDate = order.find('order-date').text
    formattedDate = purchaseDate.split('.')[0]
    row.append(formattedDate)

    row.append(country)

    if country == 'en_GB':
      csvwriter_uk.writerow(row)
    elif country == 'fr_FR':
      csvwriter_fr.writerow(row)        
    elif country == 'de_DE':
      csvwriter_de.writerow(row)

print('trasnform complete, closing CSVs')
ariat_uk.close()
ariat_de.close()
ariat_fr.close()
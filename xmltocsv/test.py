import datetime
import re

# import xml.etree.ElementTree as ET
# import csv


# tree = ET.parse("./test-order-file.xml")
# root = tree.getroot()

# print('hello world')

# # print('tree:', tree)
# # print('root:', root)

# for child in root:
#   print(child.tag, child.attrib)
  


# for order in root.findall('order'):
#   print('does this work')
#   country = order.find('customer-locale').text
#   row = []
#   print('country:', country)
#   if country == 'en_GB':

#     email = order.find('customer').find('customer-email').text
#     row.append(email)

#     # products = order.find('customer')
#     row.append('product placeholder')

#     orderId = order.find('original-order-no').text
#     row.append(orderId)

#     total = order.find('totals').find('order-total').find('gross-price').text
#     row.append(total)

#     purchaseDate = order.find('order-date').text
#     row.append(purchaseDate)


#     row.append(country)
#     print('row:', row)


# orderDate = '2018-05-03T06:46:58.000Z'



# def funcname(self, parameter_list):
#   print('hello')
#   pass

# funcname('self', '')

# newDate = datetime.datetime.fromisoformat(orderDate)
# d = datetime.datetime(*map(int, re.split('[^\d]', orderDate)[:-1]))
# print(d.split(' '))

L = range(10)
x = L[0:8:2]
print(x)

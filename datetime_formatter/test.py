import datetime

date = '2/19/2018 12:00:00 AM'
date1 = '2019-10-17 10:41:22.0'

d_pattern = '%m/%d/%Y %I:%M:%S %p'
d_pattern1 = '%Y-%m-%d %I:%M:%S.0'

d = datetime.datetime.strptime(date1, d_pattern1)


new_date = d.strftime('%m-%d-%Y %I:%M')
print(new_date)
# 02-19-2018 12:00
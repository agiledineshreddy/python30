#Write a program to count the number of emplyees present in 'one.csv'?

import csv
fp=open('one.csv','r')

csv_reader=csv.reader(fp)

user_list=list(csv_reader)
print("No of employees:",len(user_list)-1)
fp.close()
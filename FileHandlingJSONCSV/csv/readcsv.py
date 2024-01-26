#read user.csv, print data

import csv
fp=open('user.csv','r')
user_data=csv.reader(fp)

print(type(user_data))

users = list(user_data)
print(type(users))

for user in users:
    for data in user:
        print(data,'\t',end="")
    print()


fp.close()
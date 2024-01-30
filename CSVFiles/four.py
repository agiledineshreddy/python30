import csv
fp=open('one.csv','r')

emp_data=list(csv.reader(fp))

print(type(emp_data))
print(emp_data[1:])

fp.close()
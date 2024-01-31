#read csv file and 
# 1)print all emp id    
# 2)print alll emp names

import csv
fp=open('one.csv','r')

emp_data=list(csv.reader(fp))
#print(type(emp_data))
#print(emp_data)
#print all emp id
new_emp_data=emp_data[1:] 
#print(new_emp_data)

for emp_list in new_emp_data:
    i=0
    while i<=0:
        print(emp_list[1])
        i=i+1

fp.close()
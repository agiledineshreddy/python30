#read csv file and 
# 1)print all emp id    
# 2)print alll emp names

import csv
fp=open('one.csv','r')

emp_data=list(csv.reader(fp))
print(type(emp_data))

#print all emp id 
for emp_row in emp_data:
    #print(emp_row)
    for word in emp_row:
        print(word,"\t", end="")
    print()
fp.close()
#read user.json file, and write into new json file ie emp.json
import json
fp=open('user.json','r')
emp_data=json.load(fp)
print(type(emp_data))
print(len(emp_data))
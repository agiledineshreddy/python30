#read user.json, write into emp.json
import json
fp1=open('user.json','r')
fp2=open('employee.json','w')

user_data=json.load(fp1)

json.dump(user_data,fp2)

fp1.close()
fp2.close()
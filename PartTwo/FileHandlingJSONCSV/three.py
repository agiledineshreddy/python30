#read user.json, print how many male and female users
import json
fp=open('user.json','r')
user_data=json.load(fp)
print(type(user_data))

mcount=0
fcount=0
for user in user_data:
    if user['gender'] =='Male':
        mcount = mcount+1

    if user['gender'] == 'Female':
        fcount=fcount +1

    
print("No of Male Users:",  mcount)
print("No of FeMale Users:", fcount)
fp.close()
#read index.txt, print only first line

fp=open('index.txt','r')
data=fp.readlines()
print(data)

fp.close()
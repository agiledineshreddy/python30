#read index.txt file, and print only 10 char 

fp=open('index.txt','r')
data=fp.read(34)
print(data)

fp.close()
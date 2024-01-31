enames = ['hishok', 'ranjan', 'sai', 'balaji']

# enames = ['Hishok', 'Ranjan', 'Sai', 'Balaji']
new_enames = []
i = 0
while i <= len(enames)-1:
    new_enames.append(enames[i].title())
    i = i+1

print(new_enames)

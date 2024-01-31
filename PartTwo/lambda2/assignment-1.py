enames = [{'id': 101, 'name': 'rahul', 'sal': 45000},
          {'id': 102, 'name': 'sonia', 'sal': 55000},
          {'id': 103, 'name': 'priya', 'sal': 65000},]

# collection alll names as list or set
new_enames = []
# new_enames = set()
for ename in enames:
    # new_enames.add(ename['name'])
    new_enames.append(ename['name'])

print(type(new_enames))
print(new_enames)

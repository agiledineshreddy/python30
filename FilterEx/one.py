enames_list = [{'id': 101, 'name': 'Rahul', 'gender': 'Male'},
               {'id': 102, 'name': 'Sonai', 'gender': 'Female'},
               {'id': 103, 'name': 'Priyanka', 'gender': 'Female'}]

# print all Female Employees
# collect all female Employees

""" for ename in enames_list:
    if ename['gender'] != 'Female':
        print(ename['name'])
 """
female_Emp_List = set()
for ename in enames_list:
    if ename['gender'] == 'Female':
        female_Emp_List.add(ename['name'])

print(female_Emp_List)

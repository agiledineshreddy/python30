enames_list = [{'id': 101, 'name': 'Rahul', 'gender': 'Male'},
               {'id': 102, 'name': 'Sonai', 'gender': 'Female'},
               {'id': 103, 'name': 'Priyanka', 'gender': 'Female'}]

# print(list(filter(lambda ename: ename['gender'] == 'Female', enames_list)))
filter_obj = filter(lambda ename: ename['gender'] == 'Female', enames_list)
female_employees = list(filter_obj)
print(female_employees)

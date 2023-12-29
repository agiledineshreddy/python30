enames_list = [{'id': 101, 'name': 'Rahul', 'gender': 'Male'},
               {'id': 102, 'name': 'Sonai', 'gender': 'Female'},
               {'id': 103, 'name': 'Priyanka', 'gender': 'Female'}]


def femaledata(ename):
    if ename['gender'] == 'Female':
        return True
    else:
        return False


filter_obj = filter(femaledata, enames_list)
female_employees = list(filter_obj)
print(female_employees)

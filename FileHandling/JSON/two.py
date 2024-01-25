import json
emp_dict = {
    'eid': 101,
    'ename': 'Rahul',
    'esal': 4500.00,
    'avail': True,
    'discount': None
}
print(emp_dict)
# convert python dict to json

emp_str = json.dumps(emp_dict)
print(emp_str)

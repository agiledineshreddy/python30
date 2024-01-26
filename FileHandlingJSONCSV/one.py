import json
emp = {
    'eid':101,
    'ename':'RG',
    'avail':True,
    'discount':None
}
print(type(emp))
emp_json=json.dumps(emp)

print(type(emp_json))
print(emp)
print(emp_json)
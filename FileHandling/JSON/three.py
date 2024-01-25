import json
emp_json = ''' {
    "eid": 101,
    "ename": "Rahul",
    "esal": 4500.0,
    "avail": true,
    "discount": null,
    "location": null
}  '''

print(emp_json)
# convert json to python dict
emp_dict = json.loads(emp_json)

print(emp_dict)

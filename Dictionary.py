students = [
    {"name": "John", "age": 20, "DOB": "2005-03-12", "location": "Nairobi", "admission_no": "ADM001"},
    {"name": "Alice", "age": 22, "DOB": "2003-07-19", "location": "Mombasa", "admission_no": "ADM002"},
    {"name": "Bob", "age": 19, "DOB": "2006-01-05", "location": "Kisumu", "admission_no": "ADM003"},
    {"name": "Eve", "age": 21, "DOB": "2004-11-23", "location": "Nakuru", "admission_no": "ADM004"},
    {"name": "Grace", "age": 20, "DOB": "2005-09-30", "location": "Eldoret", "admission_no": "ADM005"}
]

# Print all
for s in students:
 print(f"{s['admission_no']} - {s['name']}, {s['age']}yrs, DOB: {s['DOB']}, from {s['location']}")
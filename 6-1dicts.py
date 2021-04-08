#6-1 dictionaries
#6-7 people
person_1 = {
    'first_name': 'Ivan',
    'last_name': 'Furlan',
    'hobby': 'Basketball',
    'job': 'Realestate',
    }
person_2 = {
    'first_name': 'Karla',
    'last_name': 'Eisenkohl',
    'hobby': 'Dogs',
    'job': 'Marketing',
    }
person_3 = {
    'first_name': 'Suncica',
    'last_name': 'Grdjan',
    'hobby': 'Art',
    'job': 'Education',
    }

ppl = [person_1, person_2, person_3]

for person in ppl:
    print(f"{person['first_name']} {person['last_name']} has a {person['hobby']} as a hobby and workes in {person['job']}.")

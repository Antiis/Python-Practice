#Ex. 6-9 Places

fav_places={
    'ivan':['slapovi krke','hawai','opatija'],
    'karla':['paris','london','budapest'],
    'gea':['milano','budapest','new york'],
    'suncica':['warsava','osijek','rijeka']
    }

for person in fav_places:
    p = ', '.join(map(str, fav_places[person]))
    print(f"{person.title()}'s favorite places in the world are: {p.title()}")

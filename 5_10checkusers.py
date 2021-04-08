#Excercise 5-10 Checking users

current_users = ['samir','admin','johan','pincer','wallace','lucy']
new_users = ['mcg', 'nuGGie','Phil', 'ADMIN', 'asja', 'lucy']
l_new_users = [x.lower() for x in new_users]
print(current_users)
print(l_new_users)
for user in l_new_users:
    if user in current_users:
        print("Username {} is taken, Enter new username...".format(user))
    else:
        print("{} is available.".format(user))

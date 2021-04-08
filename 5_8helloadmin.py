#Excercise 5-8 - Hello Admin
users = ['samir','admin','johan','pincer','wallace','lucy']
#Excercice 5-9 if list empty
#users = []
if len(users) < 1:
    print("We need to find some users!")
else:
    for user in users:
        if user == "admin":
            print("Hello {},  would you like to see a status report?".format(user))
        else:
            print("Hello {},  thank you for logging in again.".format(user))

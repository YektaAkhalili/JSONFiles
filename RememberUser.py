import json

filename = 'username2.json'

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("What's your username?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you, " + username + "!")       

else:
    print("Welcome back, " + username + "!" )
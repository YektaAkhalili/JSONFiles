import json 

username = input("What's your username? ")

filename = "username.json"
with open(filename, 'w') as f_obj: 
    json.dump(username,f_obj)
    print("We'll remember you next time, " + username + "!")
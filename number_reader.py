import json

filename = 'numbers.json'

with open(filename) as file_object:
    nums = json.load(file_object)

print(nums)
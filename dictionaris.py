empty_dic = {}
print(empty_dic)

print(empty_dic.keys())
print(empty_dic.values())

my_dict = {"first_name": "Prajakta", "Last_name":"shelar", "age": 31}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(f"{my_dict['first_name']} is {my_dict['age']} years old")
print("------------------------")
#adds into dictionaries like list extend or append
my_dict['language'] = "Python"
print(my_dict)
#update dict'
my_dict['language'] = "Java"
print(my_dict)

#del dict
del my_dict['language']
print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

print("------------------------")
my_dict.pop('Last_name')  #deleted
print(my_dict)
my_dict.popitem()  #deleted last item
print(my_dict)
my_dict.clear()
print(my_dict)
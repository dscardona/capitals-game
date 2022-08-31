import random

test_dict = {
    "Mexico": "Mexico City",
    "Belize": "Belmopan",
    "Guatemala": "Guatemala City",
    "El Salvador": "San Salvador",
    "Honduras": "Tegucigalpa",
    "Nicaragua": "Managua",
    "Costa Rica": "San Jose",
    "Panama": "Panama City",
    "Colombia": "Bogota"
}

# options_list =  list(test_dict.values())
# options = random.sample(options_list, 3)
# print(options)

options = random.sample(list(test_dict.values()), 3)
options.append("bogota")
print(options)
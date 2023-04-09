def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


print(get_info(**{'name': 'Pesho', 'town': 'Plovdiv', 'age': 20}))

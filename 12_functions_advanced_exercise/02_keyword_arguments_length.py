def kwargs_length(**kwargs):
    return len(kwargs)


# dictionary = {'name': 'Pesho', 'age': 20}
print(kwargs_length(name='Pesho', age=30, city='Sofia'))

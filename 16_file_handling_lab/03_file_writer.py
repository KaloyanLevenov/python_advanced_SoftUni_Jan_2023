text = ['Some additional text\n', 'Another line of text\n']
# file = open('my_first_file.txt', 'w')
# file.write('I just created my first file\n')
# file.writelines(text)
# file.close()

with open('my_first_file.txt', 'a') as file:
    file.writelines(text)

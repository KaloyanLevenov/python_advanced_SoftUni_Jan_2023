###  Here we are creating the text file first adding some text ###
# some_text = ['This is some random line\n', 'This is the second line\n', 'And this is the third one']
# with open('text.txt', 'w') as file:
#     file.writelines(some_text)

try:
    file = open('text.txt')
    print('File found')
except FileNotFoundError:
    print('File not found')
else:
    file.close()
    print('File is closed.')
finally:
    print('Finaly quit program.')
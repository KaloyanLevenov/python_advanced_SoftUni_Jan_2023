result = []
with open('words.txt', 'r') as words, open('text.txt', 'r') as text:
    list_of_words = words.read().split()
    lines = text.readlines()

    for word in list_of_words:
        word = word.lower()
        word_counter = 0

        for line in lines:
            line = line.lower()
            line = line[1:-2]
            for word_line in line.split():
                if word_line == word:
                    word_counter += 1

        result.append(f'{word} - {word_counter}')

    print(result)

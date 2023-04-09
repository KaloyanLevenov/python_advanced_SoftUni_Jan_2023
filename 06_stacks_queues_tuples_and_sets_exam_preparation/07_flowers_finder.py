from collections import deque

register = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil",
}
flower_found = None
vowels = deque(input().split())
consonants = input().split()

while vowels and consonants:
    vowel = vowels.popleft()
    consonant = consonants.pop()

    for flower in register.keys():
        register[flower] = register[flower].replace(vowel, '')
        register[flower] = register[flower].replace(consonant, '')
        flower_found = register[flower] == ''

        if flower_found:
            found_flower = flower
            print(f"Word found: {found_flower}")
            break

    if flower_found:
        break

else:
    print("Cannot find any word!")

print(f"Vowels left: {' '.join(vowels)}") if vowels else None
print(f"Consonants left: {' '.join(consonants)}") if consonants else None

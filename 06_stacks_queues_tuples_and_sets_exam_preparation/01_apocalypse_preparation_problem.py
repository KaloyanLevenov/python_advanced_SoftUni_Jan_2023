from collections import deque

textiles_are_exhausted = False
medicals_are_exhausted = False
textiles = deque(int(x) for x in input().split(' '))
medicaments = deque(int(x) for x in input().split(' '))

prescription = {
    30: 'Patch',
    40: 'Bandage',
    100: 'MedKit',
}
medical_register = dict()

while True:
    if not (textiles or medicaments):
        textiles_are_exhausted = True
        medicals_are_exhausted = True
        break
    elif textiles and not medicaments:
        medicals_are_exhausted = True
        break
    elif not textiles and medicaments:
        textiles_are_exhausted = True
        break

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    total = current_medicament + current_textile

    if total in prescription.keys():

        if prescription[total] not in medical_register.keys():
            medical_register[prescription[total]] = 0

        medical_register[prescription[total]] += 1

    elif total > 100:
        rest = 0
        if 'MedKit' not in medical_register.keys():
            medical_register['MedKit'] = 0
        medical_register['MedKit'] += 1
        rest = total - 100
        current_medicament = medicaments.pop()
        medicaments.append(current_medicament + rest)

    else:
        medicaments.append(current_medicament + 10)


print("Textiles are empty.") if textiles_are_exhausted and not medicals_are_exhausted else None
print("Medicaments are empty.") if medicals_are_exhausted and not textiles_are_exhausted else None
print("Textiles and medicaments are both empty.") if textiles_are_exhausted and medicals_are_exhausted else None

result = []

for item_name, amount_created in sorted(medical_register.items(), key= lambda x: (-x[1], x[0])):
    string = f'{item_name} - {amount_created}'
    result.append(string)

print(*result, sep='\n') if result else None


if not medicals_are_exhausted:
    medicaments.reverse()
    print('Medicaments left: ', end='')
    print(*medicaments, sep=', ')

elif not textiles_are_exhausted:
    print('Textiles left: ', end='')
    print(*textiles, sep=', ')




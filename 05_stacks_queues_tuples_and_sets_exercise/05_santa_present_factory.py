
from collections import deque

list_of_materials = [int(x) for x in input().split()]
magic_level_deque = deque(int(x) for x in input().split())

presents_register = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

presents_made = []
presents_are_crafted = False
while list_of_materials and magic_level_deque:
    material = list_of_materials.pop() if magic_level_deque[0] or not list_of_materials[-1] else 0
    magic_level = magic_level_deque.popleft() if material or not magic_level_deque[0] else 0
    total_magic_level = material * magic_level

    if not presents_register.get(total_magic_level):
        if 0 > total_magic_level:
            list_of_materials.append(material + magic_level)
        elif 0 < total_magic_level:
            list_of_materials.append(material + 15)
    else:
        present = presents_register[total_magic_level]
        presents_made.append(present)

if {"Doll", "Wooden train"}.issubset(presents_made) or {"Teddy bear", "Bicycle"}.issubset(presents_made):
    presents_are_crafted = True

print("The presents are crafted! Merry Christmas!") if presents_are_crafted else None
print("No presents this Christmas!") if not presents_are_crafted else None
print(f"Materials left: {', '.join(str(x) for x in list_of_materials[::-1])}") if list_of_materials else None
print(f"Magic left: {', '.join(str(x) for x in magic_level_deque)}") if magic_level_deque else None
[print(f"{present}: {presents_made.count(present)}") for present in sorted(set(presents_made))]

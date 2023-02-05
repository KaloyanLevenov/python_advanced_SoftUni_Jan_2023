number_of_input_lines = int(input())
chemical_compounds = set()

for _ in range(number_of_input_lines):
    elements = input().split()
    for element in elements:
        chemical_compounds.add(element)

print(*chemical_compounds, sep = '\n')


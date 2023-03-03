from math import floor
from collections import deque


def check_colors(colors_made):
    color_register = {"orange": lambda x: {"red", "yellow"}.issubset(x),
                      "purple": lambda x: {"red", "blue"}.issubset(x),
                      "green": lambda x: {"yellow", "blue"}.issubset(x),
                      }

    for color in colors_made.copy():
        if color in color_register.keys() and not color_register[color](colors_made):
            colors_made.remove(color)

    return colors_made


MAIN_COLORS = ["red", "yellow", "blue"]
SECONDARY_COLORS = ["orange", "purple", "green"]
color_list = []

single_line_of_strings = deque(input().split())

while single_line_of_strings:
    first_substring = single_line_of_strings.popleft()
    last_substring = single_line_of_strings.pop() if single_line_of_strings else ''

    if first_substring + last_substring in MAIN_COLORS + SECONDARY_COLORS:
        color_list.append(first_substring + last_substring)
    elif last_substring + first_substring in MAIN_COLORS + SECONDARY_COLORS:
        color_list.append(last_substring + first_substring)
    else:
        first_substring = first_substring[:-1]
        last_substring = last_substring[:-1]
        middle_index = floor(len(single_line_of_strings) / 2)
        single_line_of_strings.insert(middle_index, first_substring) if first_substring else None
        single_line_of_strings.insert(middle_index, last_substring) if last_substring else None


color_list = check_colors(color_list)
print(color_list)
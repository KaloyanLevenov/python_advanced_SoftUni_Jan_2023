from collections import deque


def fill_the_box(height, length, width, *args):
    box_volume = height * length * width
    cubes = deque(args)
    total_cubes = sum([element if isinstance(element, int) else 0 for element in cubes])
    command_is_finish = False

    def decrease_volume():
        nonlocal box_volume
        nonlocal total_cubes
        box_volume -= current_cube
        total_cubes -= current_cube

    while cubes:
        current_cube = cubes.popleft()

        if current_cube == 'Finish':
            command_is_finish = True
            break

        decrease_volume()

        if box_volume <= 0:
            return f"No more free space! You have {total_cubes + abs(box_volume)} more cubes."

    if command_is_finish:
        return f"There is free space in the box. You could put {box_volume} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
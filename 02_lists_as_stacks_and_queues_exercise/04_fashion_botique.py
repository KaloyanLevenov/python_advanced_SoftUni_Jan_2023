def taking_out_clothes(shirts, rack_availability):
    number_of_racks = 1
    sum_of_shirts_on_rack = 0
    while shirts:
        current_cloth = shirts.pop()
        sum_of_shirts_on_rack += current_cloth
        if sum_of_shirts_on_rack == rack_availability and shirts:
            number_of_racks += 1
            sum_of_shirts_on_rack = 0
        elif sum_of_shirts_on_rack > rack_availability:
            shirts.append(current_cloth)
            number_of_racks += 1
            sum_of_shirts_on_rack = 0

    print(number_of_racks)


clothes = [int(x) for x in input().split()]

rack_capacity = int(input())
taking_out_clothes(clothes, rack_capacity)


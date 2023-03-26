def separator(*args):
    positive_list = []
    negative_list = []

    def positive_numbers():
        positive_list.append(number)

    def negative_numbers():
        negative_list.append(number)

    for number in args:
        if number > 0:
            positive_numbers()
        elif number < 0:
            negative_numbers()

    print(sum(negative_list))
    print(sum(positive_list))
    print("The negatives are stronger than the positives") if abs(sum(negative_list)) > sum(positive_list) else\
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]
separator(*numbers)

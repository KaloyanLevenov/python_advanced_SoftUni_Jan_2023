from collections import deque

BOX_SIZE = 50
filled_boxes_with_eggs = 0
sequence_of_eggs = deque(int(x) for x in input().split(', ') if int(x) > 0)
sequence_of_papers = deque(map(int, input().split(', ')))


while sequence_of_papers and sequence_of_eggs:

    egg = sequence_of_eggs.popleft()

    if egg == 13:
        sequence_of_papers[0], sequence_of_papers[-1] = sequence_of_papers[-1], sequence_of_papers[0]
        continue

    paper = sequence_of_papers.pop()
    total = egg + paper
    filled_boxes_with_eggs += 1 if total <= 50 else 0

if filled_boxes_with_eggs:
    print(f"Great! You filled {filled_boxes_with_eggs} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

print(f"Eggs left: {', '.join(map(str, sequence_of_eggs))}") if sequence_of_eggs else None
print(f"Pieces of paper left: {', '.join(map(str, sequence_of_papers))}") if sequence_of_papers else None

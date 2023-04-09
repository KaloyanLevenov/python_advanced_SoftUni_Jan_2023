from collections import deque

peaks = {
    80: 'Vihren',
    90: 'Kutelo',
    100: 'Banski Suhodol',
    60: 'Polezhan',
    70: 'Kamenitza',
}
climbed_peaks = []
job_done = False
ran_out_of_supplies = False
daily_portions = deque(int(x) for x in input().split(', '))
daily_stamina = deque(int(x) for x in input().split(', '))

for difficulty, peak in peaks.items():

    while daily_portions and daily_stamina:
        total = daily_portions.pop() + daily_stamina.popleft()
        if total >= difficulty:
            climbed_peaks.append(peak)
            break
        else:
            continue
    else:
        ran_out_of_supplies = True

    if ran_out_of_supplies:
        break

else:
    job_done = True
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")

if not job_done:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if climbed_peaks:
    print("Conquered peaks:",end='\n')
    print(*climbed_peaks, sep='\n')



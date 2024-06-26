sum = 0
num = [1, 12, 84, 20, 15, 728, 89, 90, 55, 6, 20, 605]
for i in range(len(num)):
    if num[i] % 5 == 0:
        sum += num[i]
print(sum)
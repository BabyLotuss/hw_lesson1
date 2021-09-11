list_1 = [i ** 3 for i in range(1, 1001) if i % 2 != 0]
sums1 = 0
sums2 = 0

for idx in range(len(list_1)):
    num_sum = 0
    n = list_1[idx]
    while n:
        num_sum += n % 10
        n = n // 10
    if num_sum % 7 == 0:
        sums1 += list_1[idx]

    list_1[idx] += 17
    num_sum = 0
    n = list_1[idx]
    while n:
        num_sum += n % 10
        n = n // 10
    if num_sum % 7 == 0:
        sums2 += list_1[idx]

print(sums1)
print(sums2)
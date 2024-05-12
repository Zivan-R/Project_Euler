list = [1, 2]
even_list = []
i = 1

while list[i] < 4000000:
    i += 1
    list.append(list[i - 2] + list[i - 1])

for x in range(len(list)):
    if list[x] % 2 == 0:
        even_list.append(list[x])

print(sum(even_list))
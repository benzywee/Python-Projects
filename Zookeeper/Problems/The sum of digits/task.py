number = input()
sum_all = 0
counter = 0
while counter < len(number):
    sum_all = sum_all + int(number[counter])
    counter += 1
print(sum_all)

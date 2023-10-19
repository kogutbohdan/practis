numbers=[]

for number in range(19):
    numbers.append(int(input()))

numbers.sort(reverse=True)
print(numbers)
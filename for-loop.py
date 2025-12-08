l = ['one', 'two', 'three']

for i in l:
  print(i)

print(type(l))
print('x' * 5)

numbers = [1, 5, 3, 6, 6, 7, 3, 8, 3, 7]
largest_number = numbers[0]

for item in numbers:
  if item > largest_number:
    largest_number = item

print('largest_number', largest_number)

# Remove duplicates from list exercise
duplicates_list = [1, 5, 3, 6, 6, 7, 3, 8, 3, 7]
result = []

for item in duplicates_list:
  if item not in result:
    result.append(item)

print('result', result)

def read_data():
    return map(
        lambda s: int(s),
        open("txt1.txt", "r").readlines()) #"IntegerArray.txt"


numbers = read_data()
print numbers
a = [1,7,6,5]

numbers = a

count = 0
index = 0
print a[len(numbers)]
while index < len(numbers):
    for number in numbers[index:]:
        if numbers[index] > number:
            count += 1
    index += 1

print numbers[2:]
print count
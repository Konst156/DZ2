# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

file = open('file.txt')
fd = file.read().splitlines()

n = int(input("Введите число N: "))
number = [i for i in range(-n, n + 1)]

mp = 1
for i in range(len(number)):
    if str(i) in fd:
        mp *= number[i]

print(fd)
print(number)
print(mp)
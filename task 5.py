# Реализуйте алгоритм перемешивания списка.
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print(numbers)
random.shuffle(numbers)
print(numbers)
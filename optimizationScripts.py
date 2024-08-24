import numpy as np


def optimization_script():
    # Использование понимания списка
    squares = [i**2 for i in range(1, 1000001)]
    print(squares)


def script_optimization():
    # Использование NumPy для еще большей производительности
    numbers = np.arange(1, 1000001)
    squares = numbers**2
    print(squares)

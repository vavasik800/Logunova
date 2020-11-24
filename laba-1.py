import numpy as np
import os


def evaluate(array_int):
    even_numbers = [i for i in array_int if i % 2 == 0] # массив всех чётных чисел
    odd_numbers = [i for i in array_int if i % 2 == 1] # массив всех нечётных чисел
    prod_even_numbers = np.prod(even_numbers)
    sum_odd_numbers = sum(odd_numbers)
    return sum_odd_numbers - prod_even_numbers


def CountSize(path):
    files = os.listdir(path)
    size_files = sum([os.path.getsize(path + '\\' +i) for i in files])
    return size_files

def CountMutations(dnk_1, dnk_2):
    count_mutation = 0
    for gen_1, gen_2 in zip(dnk_1, dnk_2):
        if gen_1 != gen_2:
            count_mutation += 1
    return count_mutation

def toRNA(dnk):
    irnk = ''
    for gen in dnk:
        if gen == 'G':
            irnk += 'C'
        elif gen == 'A':
            irnk += 'U'
        elif gen == 'T':
            irnk += 'A'
        elif gen == 'C':
            irnk += 'G'
    trnk = ''
    for gen in irnk:
        if gen == 'C':
            trnk += 'G'
        elif gen == 'U':
            trnk += 'A'
        elif gen == 'A':
            trnk += 'U'
        elif gen == 'G':
            trnk += 'C'
    return trnk

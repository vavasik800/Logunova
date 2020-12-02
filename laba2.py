

def path_in_town(paths):
    """
    Функция, которая возвращает финальный город.
    :param paths: список городов
    :return: финальный город
    """
    for path1 in paths:
        town_in = path1[1] # финальный город в одном массиве
        index = 0
        for path2 in paths:
            town_out = path2[0] # начальный город в остальных
            if town_in == town_out:
              break
            else:
                index += 1 # если финальный город не встретился не разу в массиве, то он финальный
        if index == len(paths):
            return town_in
    return None


A = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
B = [['B', 'C'], ['D', 'B'], ['C', 'A']]
C = [['A', 'Z']]
townA = path_in_town(A)
townB = path_in_town(B)
townC = path_in_town(C)
print(townA)
print(townB)
print(townC)

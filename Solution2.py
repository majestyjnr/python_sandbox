numbers_list = [1, 8]


def missing(lists):
    return [num for num in range(lists[0], lists[-1]) if num not in lists]


print(missing(numbers_list))


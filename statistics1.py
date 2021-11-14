from typing import Iterable

# TEST DATA
FILE_NAME = 'auto_mpg_v1.txt'


def mode_from_list(it: Iterable) -> float:
    frequency = {}
    for num in it:
         frequency.setdefault(num, 0)
         frequency[num] += 1
    # print(frequency)
    highest = max(frequency.values())
    highestFrequencyList = []

    for num, freq in frequency.items(): # .items() converts a dictionary into list of tuples that represents key value pairs
        if freq == highest:
            highestFrequencyList.append(int(num))
    return highestFrequencyList


emp_dict = []
with open(FILE_NAME) as file:
    for line in file:
        emp_dict.append(line.strip())
    modal_values = mode_from_list(emp_dict)

print(modal_values)


# def median_from_list(it: Iterable) -> float:
#     if len(num_file) % 2 == 0:
#         first_mid_num = num_file[len(num_file) // 2]
#         print(first_mid_num)
#         sec_mid_num = num_file[len(num_file) // 2 - 1]
#         print(sec_mid_num)
#         return (int(first_mid_num) + int(sec_mid_num)) / 2
#
#     else:
#         return float(num_file[len(num_file) // 2])
#
#
# num_file = []
#
# with open(FILE_NAME) as file:
#     for line in file:
#         num_file.append(line.strip())
#
# median = median_from_list(num_file)
# print(median)
#


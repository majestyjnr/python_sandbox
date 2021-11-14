# TEST DATA
FILE_NAME = 'auto_mpg_v1.txt'
with open(FILE_NAME) as file:
    for line in file:
        new_lst =[float(x) for x in file]
        new_dict ={}
        for num in new_lst:
            new_dict.setdefault(num, 0)
            new_dict[num] += 1

    # GET the number of lines in the file
    num_lines = sum(1 for line in open(FILE_NAME))

    for key in new_dict:
        rel_freq = new_dict[key] / num_lines
        print(f'{key} \t {new_dict[key]}  \t  {rel_freq}')

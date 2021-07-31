
man = []
other = []

try:
    data = open('bk_head_first/ch04/sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            else:
                pass
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('bk_head_first/ch04/man_data.txt', 'w') as man_file:
        print(man, file=man_file)
    with open('bk_head_first/ch04/other_data.txt', 'w') as other_file:
        print(other, file=other_file)
except IOError as err:
    print('File error: ' + str(err))

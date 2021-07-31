try:
    data = open('bk_head_first/ch03/sketch.txt')

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass

    data.close()
except IOError:
    print('The datafile is missing!')

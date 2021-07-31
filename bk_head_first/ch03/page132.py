import os

if os.path.exists('bk_head_first/ch03/sketch.txt'):
    data = open('bk_head_first/ch03/sketch.txt')
    for each_line in data:
        if not each_line.find(':') == -1:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print('The data file is missing!')
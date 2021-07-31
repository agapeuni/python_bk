man = []
other = []

try:
     man_file = open('bk_head_first/ch04/man_data.txt', 'w')
     other_file = open('bk_head_first/ch04/other_data.txt', 'w')

     print(man, file=man_file)
     print(other, file=other_file)

except IOError:
     print('File error.')

finally:
     man_file.close()
     other_file.close()
     

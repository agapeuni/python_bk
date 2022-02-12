import glob
import os

# READ A FILE
# Read a single text file
input_file = "bk_analytics/1_first/letters.txt"


## Read a text file (older method) ##
print("Output #141:")
filereader = open(input_file, 'r', newline='')
for row in filereader:
    print("{}".format(row.strip()))
filereader.close()


## Read a text file (newer method) ##
print("Output #142:")
with open(input_file, 'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))


print("Output #143:")
# READ MULTIPLE FILES
# Read multiple text files
inputPath = "bk_analytics/1_first"
for input_file in glob.glob(os.path.join(inputPath,'*.txt')):
    with open(input_file, 'r', newline='') as filereader:
       for row in filereader:
           print("{}".format(row.strip()))


# WRITE TO A FILE
# Write to a text file
my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
max_index = len(my_letters)
output_file = "bk_analytics/1_first/output1.txt"
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index-1):
        filewriter.write(my_letters[index_value]+'\t')
    else:
        filewriter.write(my_letters[index_value]+'\n')
filewriter.close()
print("Output #144: Output written to file")

# Write to a CSV file
my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
output_file = "bk_analytics/1_first/output2.txt"
filewriter = open(output_file, 'a')
for index_value in range(len(my_numbers)):
    if index_value < (max_index-1):
        filewriter.write(str(my_numbers[index_value])+',')
    else:
        filewriter.write(str(my_numbers[index_value])+'\n')
filewriter.close()
print("Output #145: Output appended to file")

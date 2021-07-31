def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)


with open('bk_head_first/ch05/james.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')

with open('bk_head_first/ch05/julie.txt') as juf:
    data = juf.readline()
julie = data.strip().split(',')

with open('bk_head_first/ch05/mikey.txt') as mif:
    data = mif.readline()
mikey = data.strip().split(',')

with open('bk_head_first/ch05/sarah.txt') as saf:
    data = saf.readline()
sarah = data.strip().split(',')

clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

for each_t in james:
    clean_james.append(sanitize(each_t))

for each_t in julie:
    clean_julie.append(sanitize(each_t))

for each_t in mikey:
    clean_mikey.append(sanitize(each_t))

for each_t in sarah:
    clean_sarah.append(sanitize(each_t))

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))

"""
['2.01', '2.01', '2.22', '2.34', '2.34', '2.45', '3.01', '3.10', '3.21']
['2.11', '2.11', '2.23', '2.23', '2.59', '3.10', '3.10', '3.21', '3.21']
['2.22', '2.38', '2.49', '3.01', '3.01', '3.02', '3.02', '3.02', '3.22']
['2.18', '2.25', '2.39', '2.54', '2.55', '2.55', '2.55', '2.58', '2.58']
"""

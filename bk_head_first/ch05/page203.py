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

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])

"""
['2.01', '2.22', '2.34']
['2.11', '2.23', '2.59']
['2.22', '2.38', '2.49']
['2.18', '2.25', '2.39']
"""
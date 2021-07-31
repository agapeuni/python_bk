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

print(james)
print(julie)
print(mikey)
print(sarah)

"""
['2-34', '3:21', '2.34', '2.45', '3.01', '2:01', '2:01', '3:10', '2-22']
['2.59', '2.11', '2:11', '2:23', '3-10', '2-23', '3:10', '3.21', '3-21']
['2:22', '3.01', '3:01', '3.02', '3:02', '3.02', '3:22', '2.49', '2:38']
['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55']
"""
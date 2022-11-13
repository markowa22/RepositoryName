# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint
# keys = ['bin', 'dec', 'hex', 'oct']
# i = 16
# dict = {'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct' : oct(i)
#         }
# pprint(dict)

d = []
for i in range(16):
        d.append({'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct' : oct(i)})
# d = [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct' : oct(i)}]
pprint(d)
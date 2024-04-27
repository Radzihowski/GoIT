from functools import reduce

l = [{1: 2, 3: 4}, {5: 6, 7: 8}]
reduce(lambda y, z: str(type(y)) + str(type(z)), l)
reduce(lambda x, y: x + y, map(lambda x: reduce(lambda y, z: str(z) + str(y) + ':' + str(l[z]), x), l))
 
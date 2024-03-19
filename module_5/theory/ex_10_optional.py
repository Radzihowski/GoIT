import collections

temps = [ 0.5, 0.0, -3.5, 0.0, 2.0, 3.5, 0.5, -4.0, -3.5, -0.5, -3.5, -10.5, -14.0, -1.0, -1.0]

temps_count = collections.Counter(temps)
print(temps_count)
print(temps_count.most_common(3))
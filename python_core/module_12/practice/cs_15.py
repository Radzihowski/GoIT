# ід капотом функції copy, deepcopy роблять не більше, ніж викликають методи __copy__, __deepcopy__.
from collections import UserList
from copy import copy, deepcopy

class CopyList(UserList):
    def __init__(self, *data):
        self.data = list(data)

    def __copy__(self):
        new = CopyList()
        new.data = self.data
        return new

    def __deepcopy__(self, memodict):
        new = CopyList()
        for i in self.data:
            new.append(i)
        memodict[id(self)] = new
        return new

    d = CopyList([1, 2, 3, 4])
    c = copy(d)
    dc = deepcopy(d)

    print(id(d), d)
    print(id(c), c)
    print(id(dc), dc)

    print(id(d[0]), d[0])
    print(id(c[0]), c[0])
    print(id(dc[0]), dc[0])
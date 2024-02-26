import json
from colorama import Fore


class X:
    name: str = "John",
    age: int = 30,
    merried: bool = True,
    divorced: bool = False,
    children: list = ("Ann", "Billy"),
    pets: any = None,
    cars:

    class XEncoder(json.JSONEncoder):
        def default(self, x: X):
            if isinstance(x, X):
                return ({q: w for q, w in zip([a for a in x.__dir__() if '__' not in a],
                                              [x.name, x.age, x.merried, x.divorced, x.children, x.pets, x.cars])})

    x = X()
    print(Fore.LIGHTYELLOW_EX, json.dumps(x, cls=XEncoder, indent=4))
    with open('file1.json', "w+") as fo:
        json.dump(x, fo, cls=XEncoder, indent=2)
        with 

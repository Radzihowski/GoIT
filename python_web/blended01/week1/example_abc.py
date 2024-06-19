from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def run(self):
        pass


class Dog(Animal):

    def run(self):
        return "Dog is running"


class Zebra(Animal):

    def run(self):
        return "Zebra is running"


class Fish(Animal):

    def swim(self):
        return "Fish is swimming"



def start_run(animal_list: list[Animal]):
    for animal in animal_list:
        print(animal.run())


if __name__ == "__main__":
    animals = [Dog(), Zebra(),  Fish()] # is not included because it doesn't have a run method
    start_run(animal_list=animals)
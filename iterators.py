# any object that contains countable number of values
# is also any object that can be traversed/looped
myTuple = ("1", "2", 3)
myIterable = iter(myTuple)
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))


x = "Francis"
myIterable = iter(x)
print(next(myIterable))

# create an iterator than returns numbers starting with 1 and increases by one
class Numbers:
    # make numbers iterable
    def __iter__(self):
        self.a = 1
        return self
    # provide traverse a class

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = Numbers()
myiter = iter(myClass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

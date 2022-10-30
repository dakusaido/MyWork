class Iteration:

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        self.coin = -1
        return self

    def __next__(self):
        try:
            self.coin += 1
            return self.lst[self.coin]
        except IndexError:
            return


a = [1, 2, 3, 4, 5, 6]
b = iter(Iteration(a))


for x in iter(b):
    if x is not None:
        print(x)
    else:
        break



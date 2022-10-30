class Remake(list):

    def append(self, num):
        for i in range(list.__len__(self)):
            list.__setitem__(self, i, list.__getitem__(self, i) ** num)


obj = Remake([1, 4, 2, 3])
print(obj)
obj.append(3)
print(obj)
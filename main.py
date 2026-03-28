class Shaxs:
    def __init__(self, yosh):
        self.__yosh = yosh

    def get_yosh(self):
        return self.__yosh

s = Shaxs(25)
print(s.get_yosh())

class Hayvon:
    def ovoz(self):
        print("Ovoz chiqaryapti")

class It(Hayvon):
    def ovoz(self):
        print("Vov-vov")

i = It()
i.ovoz()

class Tortburchak:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def yuza(self):
        return self.a * self.b

t = Tortburchak(4, 5)
print(t.yuza())

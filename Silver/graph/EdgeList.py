class Edgess:
    def __init__ (self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

    def __lt__ (self, other):
        return self.w < other.w

    def __gt__ (self, other):
        return other.__lt__(self)

edgeList = [Edgess(0,1,9),Edgess(0,3,4)]
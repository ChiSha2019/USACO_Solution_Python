class Foo:
    def __init__ (self, a, b, name):
        self.a = a
        self.b = b
        self.name = name

    def __lt__ (self, other):
        if self.a == other.a:
            return self.b < other.b
        return self.a < other.b

    def __gt__ (self, other):
        return other.__lt__(self)

    def __eq__ (self, other):
        return self.a == other.b and self.b == other.b

    def __ne__ (self, other):
        return not self.__eq__(other)
from Silver.compare.Foo import Foo

f1 = Foo(1,2, "first")
f2 = Foo(2,3, "second")
f3 = Foo(1,1, "third")
a =  [f1, f2, f3]
a.sort()
print(a[0].name)
print(a[1].name)
print(a[2].name)
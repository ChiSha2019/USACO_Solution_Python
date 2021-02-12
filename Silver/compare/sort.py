from Silver.compare.Foo import Foo

f1 = Foo(1,1, "first")
f2 = Foo(2,2, "second")
f3 = Foo(2,3, "third")
a = [f2,f1,f3]
a.sort()
print(a[0].name)
print(a[1].name)
print(a[2].name)
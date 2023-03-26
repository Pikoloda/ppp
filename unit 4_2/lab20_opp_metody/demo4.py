class A:
    pass

class B:
    pass

class C(A, B):
    pass


print(C.__bases__)

for c in C.__bases__:
    print(c.__name__)
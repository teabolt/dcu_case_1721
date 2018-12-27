class P(object):
    x = 97

    def __init__(self, a):
        self.a = a
        
    def foo(self):
        return 'red'

class Q(P):
    x = 98

    def __init__(self, a=2, b=3):
        super().__init__(a)
        self.b = b

    def foo(self):
        return 'black'

class R(P):
    x = 99
    def __init__(self, a, c):
        super().__init__(a)
        self.c = c

class S(Q):

    def __init__(self, a, b, d):
        super().__init__(a, b)
        self.d = d

p = P(1)
q = Q()
r = R(5,6)
s = S(7,8,9)
print('A: {}'.format(q.a))
print('B: {}'.format(s.d))
print('C: {}'.format(q.x))
print('D: {}'.format(s.x))
print('E: {}'.format(s.foo()))
print('F: {}'.format(r.foo()))
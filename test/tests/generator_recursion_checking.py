# Some regression tests to make sure recursion-checking works properly with generators

def test(n):
    l = []
    for i in xrange(n):
        g = (i for i in xrange(5))
        g.next()
        l.append(g)

for i in xrange(1000):
    test(3500)

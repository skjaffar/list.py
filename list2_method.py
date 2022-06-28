a={}
# print(type(a))  < class 'dict'>

# g={1,2.3,9,"mom",("munna",6)}
# print(type(g))< class 'set'>

# p={30,89,56}
# print(p[1])

# f={3,52,62}
# j=frozenset(f)
# print(j[3]) < Since frozenset object are immutable>

# d={20,3,58}
# g='hi',1,5,6
# d.add(g)
# print(d)  result {58, 3, 20, ('hi', 1, 5, 6)}


# k={2,3,6}
# k.clear()
# print(k)  < set() >

# a={8,5,6}; b={8,6,2}; c={7,6,3}; d={9,2,5}
# print(a.intersection(b)) (8, 6)
# print(a.intersection(c)) (6)
# print(a.intersection(d)) (5)
# print(b.intersection(d)) (2)
# print(d.intersection(c)) set()

# e={1,6,8,'hai'}
# w={6,9,2,'hello'}
# print(e.union(w))
# print(w.union(e)) # {1, 2, 6, 8, 9, 'hello', 'hai'}    


# d={7,8,9,2}
# s={9,5,1,3}
# p={6,7,2,0}
# d.update(s)
# d.update(p)
# print(d)   # {0, 1, 2, 3, 5, 6, 7, 8, 9}

# d={9,55,6,4,2,3}
# l={9,6,1,10}
# print(d.difference(l)) # {2, 3, 4, 55}
# print(l.difference(d)) # {1, 10}
# print(l.difference(d)) # {2, 3, 4, 55}
# print(d-l)
# print(d+l)

# A = {1, 2, 3, 4}
# B = {5, 6, 3}
# C = {5, 8, 6}
# print('Are A and B disjoint?', A.isdisjoint(B)) # false
# print('Are A and C disjoint?', A.isdisjoint(C)) # true
# print('Are C and B disjoint?', C.isdisjoint(B)) # false

# s={4,5,6,9}
# l={2,6,3,4,8}
# d={7,8,3,6}
# print(s.issubset(l))
# print(l.issuperset(d))
# print(s.issubset(d))

# a={7,9,6,9,3}
# a.copy()
# print(a)


# a={5,12,15,18,20}
# b={15,18,21,25}
# a.symmetric_difference_update(b)
# print(a) 
# b.symmetric_difference_update(a)
# print(b)  



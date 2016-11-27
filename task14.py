#! /usr/bin/env python2.7

def print_test(obj, desc):
	print "%s: val: %s type: %s id: %s" % (desc, str(obj), type(obj), hex(id(obj)))

print "############## int ##############"
a = 1
print_test(a, "a = 1")
a += 1
print_test(a, "a += 1")
b = 2
print_test(b, "b = 2")
c = 1
print_test(c, "c = 1")
d = a / 2
print_test(d, "d = a / 2")
print "#################################"
print "############## float ##############"
a = 1.0
print_test(a, "a = 1")
a += 1.0
print_test(a, "a += 1")
b = 2.0
print_test(b, "b = 2")
print "#################################"
print "############## long ##############"
a = 1L
print_test(a, "a = 1")
a += 1L
print_test(a, "a += 1")
b = 2L
print_test(b, "b = 2")
print "#################################"
print "############## complex ##############"
a = 1j
print_test(a, "a = 1")
a += 1j
print_test(a, "a += 1")
b = 2j
print_test(b, "b = 2")
print "#################################"
print "############## string ##############"
a = 'a'
print_test(a, "a = 'a'")
a += 'b'
print_test(a, "a += 'b'")
b = 'ab'
print_test(b, "b = 'ab'")
d = 'ab'
print_test(d, "d = 'ab'")
c = 'a'
print_test(c, "c = 'a'")
print "#################################"
print "############## list ##############"
a = [1,2,3]
print_test(a, "a = [1,2,3]")
a += [4,5]
print_test(a, "a += [4,5]")
a[0] = 2
print_test(a, "a[0] = 2")
b = [1,2,3]
print_test(b, "b = [1,2,3]")
print "#################################"
print "############## tuple ##############"
a = (1,2,3)
print_test(a, "a = (1,2,3)")
a = a[:-1]
print_test(a, "a = a[:-1]")
b = (1,2,3)
print_test(b, "b = (1,2,3)")
print "#################################"
print "############## set ##############"
a = set([1,2,3])
print_test(a, "a = set([1,2,3])")
a = a | set([4,5])
print_test(a, "a = a | set([4,5])")
b = set([1,2,3])
print_test(b, "b = set([1,2,3])")
c = set([1]) | set([2]) | set([3])
print_test(c, "c = set(1) | set(2) | set(3)")
print "#################################"
print "############## map ##############"
a = {'a' : 1, 'b' : 2}
print_test(a, "a = {'a' : 1, 'b' : 2}")
a['a'] = 2
print_test(a, "a['a'] = 2")
b = {'a' : 1, 'b' : 2}
print_test(b, "b = {'a' : 1, 'b' : 2}")
print "#################################"
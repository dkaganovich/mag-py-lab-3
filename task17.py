#! /usr/bin/env python2.7

def fold(seq):
	if len(seq) == 0:
		raise ValueError("Empty sequence")
	head = seq[0]
	cnt = 1
	for i in xrange(1, len(seq)):
		if head == seq[i]:
			cnt += 1
		else:
			yield cnt
			yield head
			head = seq[i]
			cnt = 1
	yield cnt # flush
	yield head 

def unfold(seq):
	if len(seq) == 0:
		raise ValueError("Empty sequence")
	if len(seq) % 2 != 0:
		raise ValueError("Malformed input")
	i = 0
	while i < len(seq):
		try:
			cnt = int(seq[i])
		except ValueError:
			print "Malformed input"
			raise
		for j in xrange(cnt):
			yield seq[i + 1]
		i += 2

seq = ["hi", "qwerty", "qwerty", [1, 2], 5, 5, 5, 1, 5, 5]
print seq
resfold = [i for i in fold(seq)]
print resfold
resunfold = [i for i in unfold(resfold)]
print resunfold
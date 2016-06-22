#! /usr/bin/python
import matplotlib.pyplot as plt
import os

if not os.path.exists('imgs'):
    os.makedirs('imgs')

content = []

with open('wordlist') as f:
    content = f.read().splitlines()
for word in content:
    objs = list(word.lower())
    vals = []
    for c in objs:
        vals.append(ord(c) - ord('a') + 1)
    y_pos = xrange(len(vals))
    plt.plot(y_pos, vals, alpha = 1)
    plt.xticks(y_pos, objs)
    plt.axis([-1,len(word),0, 26])
    name = word + '.png'
    plt.savefig('imgs/'+name)
    plt.clf()
#    plt.show()

print "TADA!!"


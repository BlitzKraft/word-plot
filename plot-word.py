#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt

content = []
with open('wordlist') as f:
    content = f.read().splitlines()
for word in content:
    objs = list(word.lower())
    vals = []
    for c in objs:
        vals.append(ord(c) - ord('a') + 1)
    y_pos = np.arange(len(vals))
    plt.plot(y_pos, vals, alpha = 0.5)
    plt.xticks(y_pos, objs)
    plt.axis([-1,len(word),0, 26])
    plt.show()


# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
# FEDERAL UNIVERSITY OF UBERLANDIA
# Faculty of Electrical Engineering
# Biomedical Engineering Lab
# ------------------------------------------------------------------------------
# Author: Italo Gustavo Sampaio Fernandes
# Contact: italogsfernandes@gmail.com
# Git: www.github.com/italogfernandes
# ------------------------------------------------------------------------------
# Decription:
# ------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


def autolabel(rects, ax):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%.4f' % float(height),
                ha='center', va='bottom')


def plot_bars(enqueue_times, dequeue_times, xnames):
    N = len(enqueue_times)

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(ind, enqueue_times, width, color='r')

    rects2 = ax.bar(ind + width, dequeue_times, width, color='y')

    # add some text for labels, title and axes ticks
    ax.set_ylabel('Times (ms)')
    ax.set_title('Bench of different queues')
    ax.set_xticks(ind + width / 2)
    ax.set_xticklabels(xnames)

    ax.legend((rects1[0], rects2[0]), ('Enqueue', 'Dequeue'))

    autolabel(rects1,ax)
    autolabel(rects2,ax)





put_times = []
get_times = []
names = []

from timeit import timeit
qnt_vezes = 100000


# Queue
import sys
if sys.version_info.major == 2:
	setup_func = 'from Queue import Queue; a = Queue(maxsize=%d);' % qnt_vezes
else:
	setup_func = 'from queue import Queue; a = Queue(maxsize=%d);' % qnt_vezes
repeat_func = 'a.put(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.put(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.get()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('Queue')

'''
# CircularQueue
setup_func = 'from CircularQueue import  CircularQueue; a = CircularQueue(maxsize=%d);' % qnt_vezes
repeat_func = 'a.put(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.put(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.get()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('CircularQueue')
'''
'''
# Deque
setup_func = 'from collections import deque; a = deque(maxlen=%d);' % qnt_vezes
repeat_func = 'a.append(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.append(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.popleft()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('deque')

'''

'''
# Circular Buffer
setup_func = 'from CircularBuffer import  CircularBuffer; a = CircularBuffer(maxsize=%d);' % qnt_vezes
repeat_func = 'a.put(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.put(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.get()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('CircularBuffer')
'''

'''
# npCircularBuffer
setup_func = 'from npCircularBuffer import  CircularBuffer; a = CircularBuffer(maxsize=%d);' % qnt_vezes
repeat_func = 'a.put(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.put(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.get()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('npCircularBuffer')
'''

'''
# Ring Buffer
setup_func = 'from RingBuffer import  RingBuffer; a = RingBuffer(size_max=%d);' % qnt_vezes
repeat_func = 'a.put(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.put(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.get()'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('npRingBuffer')
'''
'''
# Array
setup_func = 'a = [];'
repeat_func = 'a.append(1.0)'
put_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
setup_func = setup_func + '[a.append(1.0) for n in range(%d)];' % qnt_vezes
repeat_func = 'a.pop(0)'
get_times.append(timeit(repeat_func, setup_func, number=qnt_vezes))
names.append('Array')
'''

# put_times = [1, 2, 3]
# get_times = [1.1, 2.2, 3.3]
# names = ['1','2','3']
plot_bars(put_times, get_times, names)
plt.show()

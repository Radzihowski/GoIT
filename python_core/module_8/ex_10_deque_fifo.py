# FIFO (first in, first out) is a way of organizing data or, in other words, a queue. This expression describes the principle 
# of technical processing of a queue or servicing conflicting requirements by streamlining the process according to the principle
# of: "first come, first served" (FFCS). The one who comesfirst is served first, the one who comes next waits until the first one
# is served, and so on.

# fifo
# Using the deque collection, implement the FIFO data structure. Create the variable fifo, which contains the collection deque. 
# Limit the size using the constant MAX_LEN. The push function adds the value element to the end of the list fifo. The pop function
# gets and returns the first value from the list fifo.
from collections import deque

MAX_LEN = 5

fifo = deque(maxlen=MAX_LEN)


def push(element):
    fifo.append(element)


def pop():
    fifo.appendleft()

push('first')
push('second')
push('third')
push('forth')
push('fifth')
push('sixth')
push('seventh')
print(pop())
    
class Queue:
    def __init__(self, *values):
        self._queue = list(values)

    def append(self, *values):
        self._queue.extend(values)

    def copy(self):
        return Queue(*self._queue)

    def pop(self):
        if self._queue:
            return self._queue.pop(0)
        else:
            return None

    def extend(self, queue):
        self._queue.extend(queue._queue)

    def next(self):
        return Queue(*self._queue[1:])

    def __add__(self, other):
        new_queue = Queue(*self._queue)
        new_queue.extend(other)
        return new_queue

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __eq__(self, other):
        return self._queue == other._queue

    def __rshift__(self, n):
        return Queue(*self._queue[n:])

    def __str__(self):
        if not self._queue:
            return '[]'
        else:
            return '[' + ' -> '.join(map(str, self._queue)) + ']'

    def __next__(self):
        return self.next()

q1 = Queue(1, 2, 3)
print(q1)
q1.append(4, 5)
print(q1)
qx = q1.copy()
print(qx.pop())
print(qx)
q2 = q1.copy()
print(q2)
print(q1 == q2, id(q1) == id(q2))
q3 = q2.next()
print(q1, q2, q3, sep = '\n')
print(q1 + q3)
q3.extend(Queue(1, 2))
print(q3)
q4 = Queue(1, 2)
q4 += q3 >> 4
print(q4)
q5 = next(q4)
print(q4)
print(q5)
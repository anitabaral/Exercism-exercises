class BufferFullException(Exception):
    def __init__(self):
        Exception.__init__(self, *args, **kwargs)

class BufferEmptyException(Exception):
    def __init__(self):
        Exception.__init__(self, *args, **kwargs)


class CircularBuffer:
    def __init__(self, capacity):
        self.index = 0
        self.size = capacity
        self.buf = []

    def read(self):
        if len(self.buf):
            return self.buf.pop(0)
        else:
            raise BufferEmptyException

    def write(self, data):
        if len(self.buf) == self.size:
            raise BufferFullException
        self.buf.append(data)
        self.index = (self.index + 1) % self.size

    def overwrite(self, data):
        if len(self.buf) == self.size:
            self.buf.pop(0)
        self.write(data)

    def clear(self):
        del self.buf[:]

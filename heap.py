class Heap(object):
    def __init__(self):
        self.store = [0]

    def __str__(self):
        return str(self.store[1:])

    def insert(self, value):
        self.store.append(value)
        self.heapify_up(self.length())

    def heapify_up(self, position):
        if position == 1:
            return
        parent = position / 2
        if self.store[parent] < self.store[position]:
            self.swap(parent, position)
            self.heapify_up(parent)

    def heapify_down(self, position):
        if 2 * position > self.length():
            return
        l = 2 * position
        r = 2 * position + 1
        bigger_index = l
        if 2 * position == self.length():
            if self.last_element() > self.store[position]:
                bigger_index = self.length()
        elif self.store[r] > self.store[l]:
            bigger_index = r

        if self.store[bigger_index] > self.store[position]:
            self.swap(position, bigger_index)
            self.heapify_down(bigger_index)

    def swap(self, i, j):
        temp = self.store[i]
        self.store[i] = self.store[j]
        self.store[j] = temp

    def find_max(self):
        if self.length() <= 0:
            raise Exception("Empty heap")
        return self.store[1]

    def delete(self, position):
        current_element = self.store[position]
        last_element = self.last_element()
        self.swap(position, self.length())
        self.store = self.store[:self.length()]
        if current_element < last_element:
            self.heapify_up(position)
        else:
            self.heapify_down(position)

    def length(self):
        return len(self.store) - 1

    def last_element(self):
        return self.store[self.length()]

    def representation(self):
        return self.store[1:]

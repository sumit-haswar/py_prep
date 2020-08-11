from .heap import Heap


class PriorityQueue():

    def __init__(self, list):
        self.heap = Heap(list)
        self.heap.build_max_heap()

    def get_max(self):
        return self.heap.get_max()

    def insert(self, val):
        # add new value to end
        self.heap.data.append(-1)
        self.heap.size = self.heap.size + 1

        self.increase_key(self.heap.size - 1, val)

    def extract_max(self):
        max = self.heap.get_max()
        # swap max with last elem, del last and max-heapify
        self.heap.swap(0, self.heap.size - 1)
        self.heap.delete_last()
        self.heap.max_heapify(0)

        return max

    def increase_key(self, idx, new_val):
        if self.heap.data[idx] > new_val:
            raise Exception("Invalid increment value")

        self.heap.data[idx] = new_val

        while idx > 0 \
                and self.heap.data[self.heap.parent(idx)] < self.heap.data[idx]:
            self.heap.swap(idx, self.heap.parent(idx))
            idx = self.heap.parent(idx)

class Heap():

    def __init__(self, list):
        self.data = list.copy() if list else []
        self.size = len(list) if list else 0

    def left(self, idx):
        return (2 * idx) + 1

    def right(self, idx):
        return (2 * idx) + 2

    def parent(self, idx):
        return (idx - 1) // 2

    def max_heapify(self, idx):
        """

        :param idx:
        :return:
        """
        left = self.left(idx)
        right = self.right(idx)
        largest = idx

        # find largest between idx, left and right
        if left < self.size and self.data[left] > self.data[largest]:
            largest = left

        if right < self.size and self.data[right] > self.data[largest]:
            largest = right

        # set largest to idx OR max-element
        if largest != idx:
            # since idx is not largest, swap and recur
            self.swap(largest, idx)
            self.max_heapify(largest)

    def build_max_heap(self):
        """everything from self.size/2 - - - - self.size - 1 is leaf
        so we iterate from (self.size//2 - 1) to 0
        :param idx:
        :return:
        """
        mid = (self.size // 2) - 1
        for i in range(mid, -1, -1):
            self.max_heapify(i)

    def heap_sort(self):
        """
        :return: sorted list
        """
        # invoke build_max_heap on self, leading to 0th element being Max
        self.build_max_heap()
        # now from rightmost elem to idx=1 we swap, decrement-size and max_heapify(0)
        for idx in range(self.size - 1, 0, -1):
            self.swap(idx, 0)
            self.size = self.size - 1
            self.max_heapify(0)

        return self.data

    def get_max(self):
        if self.data:
            return self.data[0]
        else:
            raise Exception('empty heap !')

    def swap(self, idx_a, idx_b):
        temp = self.data[idx_a]
        self.data[idx_a] = self.data[idx_b]
        self.data[idx_b] = temp

    def delete_last(self):
        del self.data[self.size - 1]
        self.size = self.size - 1

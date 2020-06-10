# python3

class Heap:
    swaps=[]
    n=0
    data=[]

    def ip(self):
        self.n = int(input())
        self.data = list(map(int, input().split()))
        self.builder(self.data)
        return self.swaps
 
    def builder(self, data):
        self.n = len(data)
        for i in range((self.n // 2), -1, -1):
            self.build_heap(i)

    def build_heap(self, i):
        min_index = i
        left = 2*i+1
        if left < self.n and self.data[left] < self.data[min_index]:
            min_index = left
        right = 2*i+2
        if right < self.n and self.data[right] < self.data[min_index]:
            min_index = right
        if i != min_index:
            self.swaps.append((i, min_index))
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]
            self.build_heap(min_index)


    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    '''swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps'''


def main():
    #n = int(input())
    #data = list(map(int, input().split()))
    #assert len(data) == n

    heap = Heap()
    swaps = heap.ip()

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

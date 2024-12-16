# Robert Plastina
# Makes a heap of user input, and allows for a sorted heap to be output.

def maxHeapify(data, n, i):

    root = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] > data[root]:
        root = l

    if r < n and data[r] > data[root]:
        root = r

    if root != i:
        data[i], data[root] = data[root], data[i]

        maxHeapify(data, n, root)


def minHeapify(data, n, i):

    root = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and data[l] < data[root]:
        root = l
    if r < n and data[r] < data[root]:
        root = r

    if root != i:
        data[i], data[root] = data[root], data[i]
        minHeapify(data, n, root)


def buildMaxHeap(data):
    n = len(data)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        maxHeapify(data, n, i)
    return


def buildMinHeap(data):
    n = len(data)
    start = n // 2 - 1
    for i in range(start, -1, -1):
        minHeapify(data, n, i)

def maxheapSort(data):
    n = len(data)
    buildMaxHeap(data)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        maxHeapify(data, i, i=0)


def minheapSort(data):
    n = len(data)
    buildMinHeap(data)
    for i in range(n - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        minHeapify(data, i, i=0)

def main():
    s = input("Enter space separated integers: ")
    data = list(map(int, s.split()))

    buildMaxHeap(data)
    print(f"array representation of heap: {data}")
    maxheapSort(data)
    print(f"sorted heap: {data}")







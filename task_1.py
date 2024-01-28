import heapq


def find_min_expenses(array):
    if not len(array):
        return 0
    heap = []
    for value in array:
        heapq.heappush(heap, value)

    while len(heap) >= 2:
        two_smallest_values = heapq.nsmallest(2, heap)
        heapq.heappop(heap)
        heapq.heapreplace(heap, two_smallest_values[0] + two_smallest_values[1])

    return heap[0]

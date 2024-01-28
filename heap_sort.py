import heapq


def heap_sort(iterable, descending=False):
    sign = -1 if descending else 1
    heap = []
    for value in iterable:
        heapq.heappush(heap, value * sign)

    sorted_array = [heapq.heappop(heap) * sign for _ in range(len(heap))]
    return sorted_array


if __name__ == "__main__":
    # min heap
    arr = [12, 1, 11, 0, 13, 5, 20, 6, 16, 7, 4]
    sorted_arr = heap_sort(arr)
    # heap [0, 1, 5, 6, 4, 11, 20, 12, 16, 13, 7]
    print("Sorted array: ", sorted_arr)
    # Sorted array:  [0, 1, 4, 5, 6, 7, 11, 12, 13, 16, 20]

    # max heap
    sorted_arr_desc = heap_sort(arr, True)
    # max heap [-20, -16, -13, -12, -7, -5, -11, 0, -6, -1, -4]
    print("Descending order sorted array:", sorted_arr_desc)
    # Descending order sorted array: [20, 16, 13, 12, 11, 7, 6, 5, 4, 1, 0]

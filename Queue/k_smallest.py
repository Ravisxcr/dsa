import heapq

def kSmallest(arr, k):
    heap = arr[:k]
    heapq._heapify_max(heap)
    n = len(arr)
    for i in range(k,n):
        if heap[0] > arr[i]:
            heapq._heapreplace_max(heap,arr[i])
    return heap

arr = [10,6,7,2,3,8,9,11,1]
k = 4
elements = kSmallest(arr,4)
for ele in elements:
    print(ele,end=" ")
# step1 : Create a Max Heap (each parent node's value is greater than its child nodes)
         # start index as first non leaf node :  index= size/2 - 1 (upto 0th index)
         #then swap
         # then recursively perform max heap
#step 2: Replace 0th index element with last index element, reduce the array/heap size and
# again perform recursive max heap


def max_heap(n,arr,parent):
    largest=parent
    left=2*parent+1
    right=2*parent+2
    if left<n and arr[left]>arr[largest]:
        largest=left
    if(right < n and arr[right]>arr[largest]):
        largest=right
    if largest!=parent:
        arr[parent],arr[largest]=arr[largest],arr[parent]
        max_heap(n,arr,largest)

def heap_sort(n,arr):

    for j in range(n//2 - 1,-1,-1):
        max_heap(n,arr,j)
    for k in range(n-1,0,-1):
        arr[0],arr[k]=arr[k],arr[0]
        max_heap(k,arr,0)

if __name__ == '__main__':
    n=int(input("enter array size: "))
    print("enter array elements: ")
    arr=list(map(int,input().split()))
    print("Array before sorting: ")
    print(arr)
    heap_sort(n,arr)
    print("Array after heap sorting: ")
    print(arr)


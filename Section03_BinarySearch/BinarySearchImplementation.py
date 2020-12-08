

def binarySearch(arr, target):
    left = 0
    right = len(arr)-1

    while (left <= right):
        mid = (left+right)//2 #[0 5] ==> (0+5)//2=2

        if (arr[mid] == target):
            return mid
        elif (arr[mid] < target):
            left = mid + 1
        elif (arr[mid] > target):
            right = mid - 1

    return -1



arr = [1,2,3,4,5,6]
target = 6

result = binarySearch(arr, target) #index: 5

if result != -1:
    print("Element is present in array: %d" % result)
else:
    print("Element is not present in the array")

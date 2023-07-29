# merge sort 
def merge(arr,low,high):
    mid = int((low + high)/2)
    temp_array = []
    # first index of left half
    l = low 
    # first index of right half
    r = mid + 1
    while (l <= mid and r <= high):
        if arr[l] < arr[r]:
            temp_array.append(arr[l])
            l += 1
        else:
            temp_array.append(arr[r])
            r += 1
    while l <= mid:
        temp_array.append(arr[l])
        l += 1
    while r <= high:
        temp_array.append(arr[r])
        r += 1
    for i in range(low,high,1):
        arr[i] = temp_array[i-low]
        
    

def merge_sort(arr,low,high):
    n = len(arr)
    if low >= high:
        return 
    mid = int((low + high) / 2)
    # for left
    merge_sort(arr,low,mid)
    # for right 
    merge_sort(arr,mid+1,high)
    merge(arr,low,high)
    return arr
    
l = [3,4,2,1,5,9]
n = len(l)
print(merge_sort(l,0,n-1))

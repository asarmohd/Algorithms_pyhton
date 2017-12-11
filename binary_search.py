def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >= l:
 
        mid = l + (r - l)//2
 
        # If element is present at the middle itself
        if x == arr[mid]:
            return mid
         
        # If element is smaller than mid, then it can only
        # be present in left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1
    
    

"""Test array"""
arr = [ 2, 3, 4, 10, 40,50 ]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
 
if result != -1:
    print( "Element is present at index" ,result)
else:
    print( "Element not present" ,result)
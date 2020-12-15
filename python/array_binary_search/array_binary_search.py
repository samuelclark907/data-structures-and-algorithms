cat = [1,3,5,7,9,10,11,12]
dog = 14



# def binary_search(arr,val):
#     for i in arr:
#         # print(i)
#         if val == i:
#             print(arr.index(val))
#         else:
#             print(-1)




def binary_search(arr,val):
    (left, right) = (0, len(arr) - 1)
    while left <= right:
        mid = (left + right) // 2
        if val == arr[mid]:
            return mid
            break
        elif val < arr[mid]:
            right = mid -1
        else:
            left = mid + 1
    return -1




# if __name__ == '__main__':
#     cat = [1,3,5,7,9,10,11,12]
#     dog = 10
#     binary_search(cat,dog)

    


binary_search(cat,dog)
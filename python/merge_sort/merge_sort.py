def mergesort(merge_list):
    n = len(merge_list)
    print(n)
    if n > 1:
        mid = int(n / 2)
        print(mid)
        left = merge_list[0:mid]
        right = merge_list[mid:n]
        mergesort(left)
        mergesort(right)
        merge(left,right,merge_list)
    return merge_list

# mergesort(merge_list)

def merge(left,right,merge_list):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merge_list[k] = left[i]
            i += 1
        else:
            merge_list[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        merge_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merge_list[k] = right[j]
        j += 1
        k += 1

    
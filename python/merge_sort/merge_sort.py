def mergesort(list):
    n = len(lst)
    print(n)
    if n > 1:
        mid = int(n / 2)
        print(mid)
        left = list[0:mid]
        # left = sorted(left)
        # print(left)
        right = list[mid:n]
        # right = sorted(right)
        # print(right)
        mergesort(left)
        mergesort(right)
        merge(left,right,lst)
    return lst

mergesort(list)

def merge(left,right,lst):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    if i < len(left):
        lst[k]

    
def QuickSort(lst, left, right):
    if len(lst) == 1:
        return lst
    if left < right:
        position = Partition(lst, left, right)
        QuickSort(lst, left, position - 1)
        QuickSort(lst, position + 1, right)
    return lst

def Partition(lst, left, right):
    pivot = lst[right]
    i = (left - 1)
    for j in range(left, right):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[right] = lst[right], lst[i+1]
    return (i + 1)

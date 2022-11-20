
def split(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr)//2
    low_arr = split(arr[:mid])
    high_arr = split(arr[mid:])
    merge = merge_sort(low_arr, high_arr)
    return merge



def merge_sort(list1, list2):
    merge = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] <= list2[0]:
            merge.append(list1.pop(0))
        else:
            merge.append(list2.pop(0))

    if len(list1) > 0:
        merge += list1
    if len(list2) > 0:
        merge += list2

    return merge

num_lst = list(map(int, input()))

for i in range(len(num_lst)):
    print(split(num_lst)[len(num_lst) -1 -i], end = '')
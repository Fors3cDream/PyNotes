def quickSort(array):
    if len(array) < 2:
        return array # 基线条件： 为空或者只包含一个元素的数组是 "有序"的
    else:
        pivot = array[0] # 递归条件
        less = [i for i in array[1:] if i <= pivot] # 由所有小于基准值的元素组成的子数组

        greater = [i for i in array[1:] if i > pivot] # 由所有大于基准值的元素组成的子数组

        return quickSort(less) + [pivot] + quickSort(greater)


print(quickSort([10, 5, 2, 3, 17, 6, 11, 23, 33, 21, 12, 9, 7, 8]))

def quick_sort(array):
    """
    O(n*log(n) time complexity in average, degrade to O(n^2) in the worst case, unstable)
    """
    if len(array) < 2:
        return array
    else:
        # select the pivot randomly will guarantee the quick_sort not degrading to O(n^2)
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    a = [1, 3, 2, 5, 4, 9, 7]
    print(quick_sort(a))

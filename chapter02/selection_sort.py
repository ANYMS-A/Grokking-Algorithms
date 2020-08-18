import random


def find_smallest(array):
    """
    find the smallest elements' index of an array
    """
    smallest = array[0]
    smallest_idx = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_idx = i
    return smallest_idx


def selection_sort(array):
    """
    O(n^2) time complexity, unstable!
    """
    new_array = []
    for i in range(len(array)):
        smallest_idx = find_smallest(array)
        new_array.append(array.pop(smallest_idx))
    return new_array


if __name__ == "__main__":
    # create a random array in the Pythonic way
    random_array = [random.randint(0, 50) for _ in range(50)]
    print("random array is: ", random_array)
    # sort the random array
    sorted_array = selection_sort(random_array)
    print("sorted array is: ", sorted_array)

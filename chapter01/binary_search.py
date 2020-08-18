def binary_search(data_list, target_item):
    """
    The basic requirements for using binary search is the data_list must be an "ordered" list!
    """
    low_idx = 0
    high_idx = len(data_list) - 1

    while low_idx <= high_idx:
        mid_idx = (low_idx + high_idx) // 2
        guess = data_list[mid_idx]
        if guess == target_item:
            return mid_idx
        if guess > target_item:
            high_idx = mid_idx - 1
        else:
            low_idx = mid_idx + 1
    # if the data_list doesn't contain the target_item, return None type
    return None


if __name__ == "__main__":
    # set data_list and target_item
    all_data = list(range(100))
    target = 66
    # use binary search
    target_idx = binary_search(all_data, target)
    print(target_idx)

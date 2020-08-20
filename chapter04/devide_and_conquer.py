
def get_list_sum(list_data):
    """
    sum a list in the recursion way
    """
    # check if list_data == []
    if not list_data:
        return 0
    else:
        return list_data[0] + get_list_sum(list_data[1:])


def count_list_elements(list_data):
    """
    count the number of elements in a list
    """
    # check if list_data == []
    if not list_data:
        return 0
    else:
        return 1 + count_list_elements(list_data[1:])


def binary_search_recursion(data_list, target_item):
    """
    In the chapter01 we impalement the binary search by using loop
    we now re-implement it in a recursion way
    !!!NOTE, you might find that in this implementation, we do not require the input list
    to be "ordered"
    """
    half_len = len(data_list) // 2
    # base case
    if data_list[half_len] == target_item:
        return half_len
    if half_len == 0:
        return None
    else:
        half_list_prior = data_list[:half_len]
        half_list_post = data_list[half_len:]
        prior_idx = binary_search_recursion(half_list_prior, target_item)
        post_idx = binary_search_recursion(half_list_post, target_item)
        # if prior_idx is None, which means we can't find target in the prior half part
        if prior_idx:
            return prior_idx
        elif post_idx:
            return half_len + post_idx
        else:
            return None


if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5]
    list_sum = get_list_sum(example_list)
    list_count = count_list_elements(example_list)
    print("sum: ", list_sum)
    print("count: ", list_count)

    idx = binary_search_recursion(example_list, 3)
    print(idx)
    example_list_2 = [4, 2, 3, 5, 6, 7, 9]
    idx = binary_search_recursion(example_list_2, 7)
    print(idx)

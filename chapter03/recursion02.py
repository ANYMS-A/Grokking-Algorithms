
def count_down(idx):
    print(idx)
    # base case, the exit condition
    if idx < 1:
        return
    # recursive case
    else:
        count_down(idx - 1)


if __name__ == "__main__":
    count_down(7)

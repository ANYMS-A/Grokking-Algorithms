"""
Python's dict is actually a hash table
Hash Table has the constant time complexity O(1)
"""


def check_vote(data_dict, name):
    if data_dict.get(name):
        print(f"This guy {name} has voted!")
    else:
        data_dict[name] = True
        print(f"let {name} vote!")


if __name__ == "__main__":
    vote_dict = {}

    check_vote(vote_dict, "mike")
    check_vote(vote_dict, "tom")
    check_vote(vote_dict, "mike")
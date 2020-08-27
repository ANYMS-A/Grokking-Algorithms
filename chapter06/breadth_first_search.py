from collections import deque

"""
Build a graph first
"""
graph = dict()
graph["you"] = ["allan", "jack", "bob"]
graph["bob"] = ["ninja", "peggy"]
graph["allan"] = ["peggy"]
graph["jack"] = ["thom", "johnny"]
graph["ninja"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []


def is_mango_seller(person_name: str):
    if person_name == "johnny":
        return True
    else:
        return False


def breadth_first_search(name):
    """
    Breadth First Search could be basically implemented by a queue(a data structure which could achieve FIFO)
    Think about why!

    The time complexity of the BFS is O(n), where n is the number of the nodes in the graph! Because you have to put all
    of the nodes into the queue under the worst case!
    More specifically, if b represents the "branch" factor of the tree(graph), d is the "depth" of the tree, the time
    complexity should be O(b^(d+1)), and the space complexity is O(b^(d+1)) as well, think about why! Space is a bigger
    problem compared with time

    BFS is "optimal" since it always find a least cost solution( if the cost of each edge is equal)

    """
    search_deque = deque()
    search_deque += graph[name]
    # use a empty list to mark the searched people, or you might involve in an endless loop!
    people_been_searched = []

    while search_deque:

        person = search_deque.popleft()

        if person not in people_been_searched:

            if is_mango_seller(person):
                print(person + " is mango seller!")
                return True
            else:
                search_deque += graph[person]
                people_been_searched.append(person)
    return False


if __name__ == "__main__":
    breadth_first_search("you")

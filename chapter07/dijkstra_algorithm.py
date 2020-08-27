"""
Dijkstra's Algorithm often used on weighted-graph(NOTE the weight value should always be positive,
or the Dijkstra's algorithm won't work!). More specifically, the graph should be a "directed acyclic graph"!

Another intuitive explain is that: an "A* search" will degrade to Dijkstra's Algorithm only when the heuristic
term of the A* is always 0.
"""

# build a graph by using dict
#  we need save both the neighboring info and weights info in the graph
graph = dict()
# create the "start" node, it's a dict as well, think about why we use a dict to represent a node
graph["start"] = dict()
# add neighbor nodes and weights of the start node
graph["start"]["a"] = 6
graph["start"]["b"] = 2
# create "a" node
graph["a"] = dict()
graph["a"]["end"] = 1
# create "b" node
graph["b"] = dict()
graph["b"]["a"] = 3
graph["b"]["end"] = 5
# create "end" node
graph["end"] = dict()

infinity = float("inf")
# create cost list
costs = dict()
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

# create parents list
parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

# create a list to store the processed nodes
processed = []


def find_lowest_cost_node(input_costs: dict):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for key in input_costs:
        cost = input_costs[key]
        if cost < lowest_cost and key not in processed:
            lowest_cost = cost
            lowest_cost_node = key
    return lowest_cost_node


if __name__ == "__main__":
    node = find_lowest_cost_node(costs)
    while node is not None:
        tmp_cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = tmp_cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(parents)
    print(costs)
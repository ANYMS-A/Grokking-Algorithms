"""
When we meet up with an NP-complete problem, it will take us a huge amount time to get
the precise solution, thus we usually use an approximating-algorithm to achieve an decent
result in a much more faster way.

Greedy Algorithm is one of the approximating-algorithm. It seeks local optima, so sometimes it
won't get global optima.
"""
# a set represent the states need to be covered
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# radio stations
stations = dict()
stations[1] = {"id", "nv", "ut"}
stations[2] = {"wa", "id", "mt"}
stations[3] = {"or", "nv", "ca"}
stations[4] = {"nv", "ut"}
stations[5] = {"ca", "az"}

if __name__ == "__main__":
    final_stations = set()

    while states_needed:
        best_station = None
        states_been_covered = set()

        for station, states_covered_by_station in stations.items():
            covered = states_needed & states_covered_by_station
            if len(covered) > len(states_been_covered):
                best_station = station
                states_been_covered = covered

        final_stations.add(best_station)
        states_needed -= states_been_covered

    print(final_stations)

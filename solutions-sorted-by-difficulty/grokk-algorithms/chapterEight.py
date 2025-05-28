def find_minimum_stations(states_needed, stations):
    """
    Find a (greedy) minimal set of radio stations that covers all required states.

    :param states_needed: set of state abbreviations we want to cover
    :param stations: dict mapping station name -> set of states it covers
    :return: set of station names chosen
    """
    # Start with no stations chosen
    final_stations = set()

    # Repeat until we've covered all states
    while states_needed:
        best_station = None       # Will hold the name of the station covering the most uncovered states
        states_covered = set()    # Will hold the actual set of states that station covers this round

        # Example: if states_needed = {"mt", "wa", "or"} and
        # stations["A"] = {"wa","or"}, then covered = {"wa","or"}.

        # Examine each station to see how many uncovered states it covers
        for station, covered_states in stations.items():
            # Compute which of the *still-needed* states this station would cover
            covered = states_needed & covered_states
            # Example intersection:
            #     states_needed = {"mt","wa","or"}
            #     covered_states = {"wa","id","mt"}
            # --> covered = {"mt","wa"}
            #
            # Compare to the best so far:
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered
                # Example: if this is the largest yet, best_station="A", states_covered={"wa","or"}

        # If no station covers any of the remaining states, exit to avoid infinite loop
        if not best_station:
            # E.g., states_needed={"xy"}, but no station has "xy" in its coverage
            break

        # “Use” that station:
        # 1) Remove its covered states from what we still need
        # 2) Record the station in our final answer
        #
        # Example before removal:
        #     states_needed = {"mt","wa","or","id"}
        #     states_covered = {"mt","wa"}
        # After:
        #     states_needed becomes {"or","id"}
        states_needed -= states_covered
        final_stations.add(best_station)

        # Debug print (optional): show progress
        # print(f"Chose {best_station}, covered {states_covered}, still needed: {states_needed}")

    return final_stations


if __name__ == "__main__":
    # --- Example usage ---

    # 1. Define the full set of states we need to cover
    states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
    # Think: We want coverage in Montana (mt), Washington (wa), ..., Arizona (az).

    # 2. Define each station’s coverage
    stations = {
        "kone":   set(["id", "nv", "ut"]),     # K1 covers Idaho, Nevada, Utah
        "ktwo":   set(["wa", "id", "mt"]),     # K2 covers Washington, Idaho, Montana
        "kthree": set(["or", "nv", "ca"]),     # K3 covers Oregon, Nevada, California
        "kfour":  set(["nv", "ut"]),           # K4 covers Nevada, Utah
        "kfive":  set(["ca", "az"])            # K5 covers California, Arizona
    }

    # 3. Run the greedy algorithm
    result = find_minimum_stations(states_needed, stations)

    # 4. Output the chosen stations
    print("Stations selected:", result)
    # Typical output (order may vary):
    # Stations selected: {'ktwo', 'kthree', 'kone', 'kfive'}


#8.1 use the biggest boxes first
#8.2 go to every state in the order of wanting to see them until you run out of time for the next one
#8.3 no
#8.4 yes
#8.5 yes
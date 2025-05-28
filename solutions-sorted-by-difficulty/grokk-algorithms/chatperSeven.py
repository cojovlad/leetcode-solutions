import heapq

def dijkstra(graph, start):
    """
    Compute shortest paths from `start` to all other nodes in `graph`.
    """
    # 1. Initialize distances: start at 0, others at infinity
    #    Example: graph = {'A': [...], 'B': [...], 'C': [...]}
    #    distances = {'A': 0, 'B': inf, 'C': inf}
    distances = {node: float('inf') for node in graph}  # all nodes → ∞
    distances[start] = 0                                 # start → 0

    # 2. Priority queue holds (distance, node)
    #    pq = [(0, 'A')]  # we begin by exploring 'A' at dist 0
    pq = [(0, start)]
    visited = set()  # to track which nodes we've finalized

    print(f"Starting Dijkstra from '{start}'\n")

    # 3. Main loop: process nodes in order of increasing distance
    while pq:
        # Pop the node u with smallest current tentative distance
        current_dist, u = heapq.heappop(pq)
        #    Example pop: (0, 'A') → u='A', current_dist=0

        # Skip if we've already finalized u
        if u in visited:
            #    If u='A' was already visited, we ignore stale entries
            continue

        # Finalize this node: the shortest path to u is now confirmed
        visited.add(u)
        print(f"Finalizing {u} at distance {current_dist}")
        #    Example output: "Finalizing A at distance 0"

        # 4. Relax edges: try improving paths to each neighbor v of u
        for v, weight in graph[u]:
            #    Suppose graph['A'] = [('B', 1), ('C', 2)]
            #    First iteration: v='B', weight=1
            new_dist = current_dist + weight
            #    new_dist = 0 + 1 = 1
            # If the new path is shorter, update and enqueue
            if new_dist < distances[v]:
                #    distances['B'] was ∞, now set to 1
                distances[v] = new_dist
                #    Push (1, 'B') to pq
                heapq.heappush(pq, (new_dist, v))
                print(f"  -> Pushing {v} with distance {new_dist}")
                #    Example output: "  -> Pushing B with distance 1"

        # Loop repeats until pq is empty

    # 5. Report results
    print("\nShortest distances:")
    for node in sorted(distances):
        #    Sorted order: ['A', 'B', 'C']
        print(f"  {node}: {distances[node]}")
        #    Example output:
        #      A: 0
        #      B: 1
        #      C: 2

    return distances

if __name__ == "__main__":
    # Example graph with non-negative weights
    graph_pos = {
        'A': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('C', 0)],
        'C': [('D', 0)],
        'D': []
    }

    print("Example 1: Positive weights only")
    # Calling dijkstra(graph_pos, 'A') proceeds as:
    #   distances = {'A':0, 'B':∞, 'C':∞}
    #   pq = [(0,'A')], visited = {}
    # 1) pop (0,'A'), finalize A, relax edges:
    #      B: new_dist=1 → update & push (1,'B')
    #      C: new_dist=2 → update & push (2,'C')
    #   pq = [(1,'B'), (2,'C')]
    # 2) pop (1,'B'), finalize B, relax edges:
    #      C: new_dist=1+0=1 < 2 → update & push (1,'C')
    #   pq may now have (1,'C'), (2,'C')
    # 3) pop (1,'C'), finalize C (ignore the stale (2,'C'))
    # End → distances: A=0, B=1, C=1
    dijkstra(graph_pos, 'A')

    print("\n" + "="*40 + "\n")

# 7.1 A 9 B 60 C 8 or not possible



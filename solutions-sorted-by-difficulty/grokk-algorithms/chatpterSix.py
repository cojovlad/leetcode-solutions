from collections import deque


def personIsSeller(name):
    return name[-1] == 'm'

def bfs(name):
    search = deque()
    search.append(name)
    visited=set()

    while search:
        person = search.popleft()
        if person not in visited:
            if personIsSeller(person):
                return person
            else:
                search.extend(graph[person])
                visited.add(person)
    return None

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

print(bfs("you"))

# 6.1 shorthest path is 2
# 6.2 shortest path is cab cat bat
# 6.3 invalid valid invalid
# 6.4 wake up exercise shower get dressed brush teeth eat breakfast pack lunch
# 6.5 a c
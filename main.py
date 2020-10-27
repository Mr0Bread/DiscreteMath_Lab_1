graph = {'a': {'b': 10, 'c': 13},
         'b': {'c': 1, 'd': 2},
         'c': {'b': 4, 'd': 8, 'e': 2},
         'd': {'e': 7},
         'e': {'d': 9, 'a': 20}}


def dijkstra(graph, start, goal):
    shortest = {}
    pre = {}
    unseen = graph
    inf = 100
    path = []
    for node in unseen:
        shortest[node] = inf
    shortest[start] = 0
    while unseen:
        minnode = None
        for node in unseen:
            if minnode is None:
                minnode = node
            elif shortest[node] < shortest[minnode]:
                minnode = node
        for childnode, weight in graph[minnode].items():
            if weight + shortest[minnode] < shortest[childnode]:
                shortest[childnode] = weight + shortest[minnode]
                pre[childnode] = minnode
        unseen.pop(minnode)
    print(shortest)
    current = goal
    while current != start:
        try:
            path.insert(0, current)
            current = pre[current]
        except KeyError:
            print('no path!')
            break
    if shortest[goal] != inf:
        print('Shortest distance is ' + str(shortest[goal]))
        print('The path is ' + str(path))


dijkstra(graph, 'e', 'a')

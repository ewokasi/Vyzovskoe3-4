
    # graph=[[0, 235, 215, 0, 0],
    #     [0, 0, 0, 170, 0 ],
    #     [0, 185, 0, 0, 205],
    #     [0,0,120,0,170],
    #     [0,0,0,0,0]]

        
def dijkstra_shortest_path(graph, start, p={}, u=[], d={}):
    if len(p) == 0: p[start] = 0 # инициализация начального пути
    # print "start V: %d, " % (start)
    for x in graph[start]:
        if (x not in u and x != start):
            if (x not in p.keys() or (graph[start][x] + p[start]) < p[x]):
                p[x] = graph[start][x] + p[start]

    u.append(start)

    min_v = 0
    min_x = None
    for x in p:
        # print "x: %d, p[x]: %d, mv %d" % (x, p[x], min_v)
        if (p[x] < min_v or min_v == 0) and x not in u:
                min_x = x
                min_v = p[x]

    if(len(u) < len(graph) and min_x):
        return dijkstra_shortest_path(graph, min_x, p, u)
    else:
        return p

if __name__ == '__main__':
    # инициализация графа с помощью словаря смежности
    a, b, c, d, e = range(5)
    N = [
        {b: 235, c: 215},
        {d: 170},
        { b: 186, e: 205},
        {b: 15, c: 120, e: 170},
        {}  
    ]
    for i in range(1):
        print (dijkstra_shortest_path(N, a))
# b in N[a] - смежность
# len(N[f]) - степень
# N[a][b] - вес (a,b)
# print N[a][b]
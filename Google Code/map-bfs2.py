graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}




# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = [] # keep tracked of explored node
    # keep track of nodes to be checked
    queue = [start] # implement queue as list
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop(0)
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
print('bfs A', bfs_connected_component(graph,'A')) # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
# print(graph)
# for v in graph.keys():
# 	print(graph[v])
# 	print(bfs_connected_component(graph,v)) 

# finds shortest path between 2 nodes of a graph using BFS
def bfs_shortest_path(graph, start, goal):
    # keep track of explored nodes
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is goal
                if neighbour == goal:
                    return new_path
 
            # mark node as explored
            explored.append(node)
 
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist :("
 
#print('shortest path between G and D is',bfs_shortest_path(graph, 'G', 'D'))  # returns ['G', 'C', 'A', 'B', 'D']



def dfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = [] # keep tracked of explored node
    # keep track of nodes to be checked
    queue = [start] # implement queue as list
 
    # keep looping until there are nodes still to be checked
    while queue:
        # pop shallowest node (first node) from queue
        node = queue.pop()
        if node not in explored:
            # add node to list of checked nodes
            explored.append(node)
            neighbours = graph[node]
 
            # add neighbours of node to queue
            for neighbour in neighbours:
                queue.append(neighbour)
    return explored
 
print('dfs A',dfs_connected_component(graph,'A')) # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']



import collections


# def breadth_first_search(graph, root): 
#     visited, queue = set(), collections.deque([root])
#     while queue: 
#         vertex = queue.popleft()
#         for neighbour in graph[vertex]: 
#             if neighbour not in visited: 
#                 visited.add(neighbour) 
#                 queue.append(neighbour) 


# if __name__ == '__main__':
#     graph = {0: [1, 2], 1: [2], 2: []} 
#     breadth_first_search(graph, 0)




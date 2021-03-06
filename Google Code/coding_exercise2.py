graph1 = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B', 'E'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

graph2 = {'A': set(['B', 'C', 'E']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F', 'G']),
         'D': set(['B']),
         'E': set(['A', 'B', 'D']),
         'F': set(['C']),
         'G': set(['C'])}



def bfs_connected_component(graph1, start_vertex):
	queue = [start_vertex]
	explored = []
	while queue:
		node = queue.pop(0)
		if node not in explored:
			explored.append(node)
			neighbors=graph1[node]
			for neighbor in neighbors:
				queue.append(neighbor)
	return explored


from collections import deque

def bfs_connected_component3(graph1, start_vertex):
	queue = deque([start_vertex])
	explored = []
	while queue:
		node = queue.popleft()
		if node not in explored:
			explored.append(node)
			neighbors=graph1[node]
			for neighbor in neighbors:
				queue.append(neighbor)
	return explored



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
        #print(path)
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
 


print('bfs_connected  ', bfs_connected_component(graph1,'A'))
print('bfs_connected 3', bfs_connected_component3(graph1,'A'))
print('bfs_shortest path', bfs_shortest_path(graph1, 'G', 'D'))



from collections import defaultdict, deque

def dfs(node, prev, graph, route, num_tickets):
    route.append(node)
    if prev:
        graph[prev].remove(node)
    
    if len(route) == num_tickets + 1:
        return True
    
    for adj in graph[node]:
        if dfs(adj, node, graph, route, num_tickets):
            return True
    
    route.pop()
    if prev:
        graph[prev].insert(0, node)
    return False
    
def solution(tickets):
    graph = defaultdict(list)
    num_tickets = 0
    for a, b in tickets:
        graph[a].append(b)
        num_tickets += 1
    for key in graph.keys():
        graph[key].sort()
    
    route = []
    dfs("ICN", None, graph, route, num_tickets)    
    
    return route
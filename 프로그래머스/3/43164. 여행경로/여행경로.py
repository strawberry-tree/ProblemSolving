from collections import defaultdict

def dfs(node, prev, graph, route, curr_tickets, num_tickets):
    route.append(node)
    if prev is not None:
        curr_tickets[(prev, node)] -= 1
    
    if num_tickets == 0:
        return True

    for adj in graph[node]:
        if curr_tickets[(node, adj)] > 0:
            if dfs(adj, node, graph, route, curr_tickets, num_tickets - 1):
                return True
    
    route.pop()
    if prev is not None:
        curr_tickets[(prev, node)] += 1

    return False
    
def solution(tickets):
    graph = defaultdict(list)
    curr_tickets = defaultdict(int)
    for a, b in tickets:
        graph[a].append(b)
        curr_tickets[(a, b)] += 1
    for key in graph:
        graph[key] = sorted(graph[key])
    
    route = []
    dfs("ICN", None, graph, route, curr_tickets, len(tickets))    
    
    return route
from collections import defaultdict

def dfs(node, graph, route, curr_tickets, num_tickets):
    route.append(node)
    
    if num_tickets == 0:
        return True

    for adj in graph[node]:
        if curr_tickets[(node, adj)] > 0:
            curr_tickets[(node, adj)] -= 1
            if dfs(adj, graph, route, curr_tickets, num_tickets - 1):
                return True
            curr_tickets[(node, adj)] += 1
    
    route.pop()
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
    dfs("ICN", graph, route, curr_tickets, len(tickets))    
    
    return route
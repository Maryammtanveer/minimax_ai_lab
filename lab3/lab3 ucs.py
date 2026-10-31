import heapq
graph={"A":[("B",1),("C", 6)],
       "B":[("D", 5),("E", 1)],
       "C":[("F", 2), ("g", 6)],
       "D":[],
       "E":[("G", 1)],
       "F":[],
       "G":[]
       }


def ucs (start, goal):
    pq = [(0, start, [start])]
    best ={start: 0}
    order = []
    
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if cost != best [node]:
            continue
        order.append(node)
        print("processing", node, "cost", cost)
        
        
        if node == goal:
            return path, cost, order
        
        
        for child, weight in graph[node]:
            new_cost = cost + weight
            
            
            if new_cost < best.get(child, float("inf")):
                best[child] = new_cost
                heapq.heappush(pq, (new_cost, child, path +[child]))

path, cost, order = ucs("A", "G")
print("ucs path",path)
print("total cost:", cost)
print ("processing order:", order)
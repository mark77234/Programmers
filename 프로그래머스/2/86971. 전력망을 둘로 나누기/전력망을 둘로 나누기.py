from collections import deque

def bfs(n,wires,remove):
    visited = [False] * (n+1)
    visited[1] = True
    q = deque([1])
    cnt = 1
    
    while q:
        node = q.popleft()
        
        for i,(start,end) in enumerate(wires):
            if i == remove:
                continue
            
            if node == start and visited[end] == False:
                q.append(end)
                visited[end] = True
                cnt += 1
            elif node == end and visited[start] == False:
                q.append(start)
                visited[start] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = n
    for i in range(n):
        cnt = bfs(n,wires,i)
        diff = abs(cnt - (n - cnt))
        answer = min(answer,diff)
    
    return answer
    
            
                
            
        
        
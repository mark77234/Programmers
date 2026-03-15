def solution(k, dungeons):
    answer = 0
    visited = [False] * len(dungeons)
    
    def dfs(fatigue,cnt):
        nonlocal answer
        answer = max(answer,cnt)
        
        for i in range(len(dungeons)):
            need,after = dungeons[i]
            
            if visited[i] == False and fatigue >= need:
                visited[i] = True
                dfs(fatigue - after,cnt+1)
                visited[i] = False
    dfs(k,0)
    
    return answer
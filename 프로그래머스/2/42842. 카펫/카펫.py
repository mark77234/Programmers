def solution(brown, yellow):
    for yellow_size in range(1,yellow+1):
        if yellow % yellow_size == 0:
            yellow_x = yellow // yellow_size
            yellow_y = yellow_size
            
            if 2*yellow_x + 2*yellow_y + 4 == brown:
                answer = [yellow_y+2,yellow_x+2]
    return answer
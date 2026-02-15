from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)  # [0](비어있는 다리)를 다리 길이 만큼 채워 줌
    trucks = deque(truck_weights)
    time = 0
    current_weight = 0

    while bridge:
        time += 1
        current_weight -= bridge.popleft() # 빠져나갈 트럭무게 (항상 다리의 첫번재 인덱스를 보내줌)

        if trucks:
            if current_weight + trucks[0] <= weight: # 다리 무게 검증
                truck = trucks.popleft() # 트럭큐의 첫번째 트럭 다리로
                bridge.append(truck) # 다리에 추가
                current_weight += truck # 현재 무게 추가
            else:
                bridge.append(0) # 다리 무게 초과인 경우에는 [0]무게가 없는 다리를 추가
    return time
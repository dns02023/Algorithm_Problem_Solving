### 2019 카카오 개발자 겨울 인턴십 기출문제 : 불량 사용자 ###
### 집합의 특성(순서에 상관없음)을 사용하자 => 조합 경우의 수를 해결할 수 있는 자료형.
### DFS를 통한 모든 경우의 수 탐색

import copy

def solution(user_id, banned_id):
    global result_list, users, bans, result
    result_list = list()
    users = user_id
    bans = banned_id

    result = set()
    dfs(0)
    answer = len(result_list)

    return answer

def dfs(idx):
    if idx == len(bans):
        if result not in result_list:
            result_list.append(copy.deepcopy(result))
            # 넣기전에 copy 잊지말자.
        return

    target = list(bans[idx])
    for user in users:
        u = list(user)
        if len(u) != len(target):
            continue

        flag = 0
        for i in range(len(target)):
            if (u[i] != target[i]) and (target[i] != '*'):
                flag = 1
                break
        if flag == 1:
            continue

        if user not in result:
            result.add(user)
            dfs(idx + 1)
            result.remove(user)







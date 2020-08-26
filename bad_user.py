### 2019 카카오 개발자 겨울 인턴십 기출문제 : 불량 사용자 ###
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







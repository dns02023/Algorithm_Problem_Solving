N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

orders = list()
order = [-1, -1, -1, 0, -1, -1, -1, -1, -1]
results = list()

# 원래 모든 경우의 수(순열)를 다 계산을 해놓고 다시 for문을 돌렸지만, 이것은 for문을 한번 더 돌게 되므로 시간이 더 걸림
# => 시간초과를 방지하기 위해 sort 함수 내에서 종료조건(모든 타순이 결정된 상황)에 도달 시, 경기를 진행해서 score를 계산함.
# => 함수 하나에서 한번의 loop로 탐색을 끝냄

def sort(index):
    #print(idx)
    # index : 몇번째 타자를 결정하는지
    if index == 9:
        # index가 9에 도달했다는 것은 0번째부터 8번째 까지 타순을 모두 결정했다는 것 (order가 결정됨)이므로, 경기를 시작
        total_score = 0
        idx = 0
        # 0번째 타자부터 시작
        for i in range(N):
            first, second, third = 0, 0, 0
            points = arr[i]
            # i번째 이닝에 각 선수들이 하는 행동들 인덱스는 선수들의 등번호(0-9)
            out_cnt = 0
            while out_cnt != 3:
                if points[order[idx]] == 0:
                    # order는 각 선수의 등번호로 구성된 배열. 즉 idx번째 타순인 선수의 등번호는 order[idx]
                    # 그 선수의 i번째 이닝에서 하는 행동은 points[order[idx]]
                    out_cnt = out_cnt + 1
                    idx = (idx + 1) % 9
                # 이 뒤에서부터는 elif 해야지.. if 써버리면 진입해버리잖아.. idx 를 변화시켜주는데!! 그럼 당근 if문 또 들어가지..!! 정신차리자 진짜
                # if, elif, else 알맞게 활용하자 if만 쓸 생각 하지말고
                # 타격후에 1,2,3 루가 어떻게 변하는지, 점수가 어떻게 변하는지 효율적으로 계산하려면 그림을 그려서 문제를 이해하는 습관을 들이자.
                elif points[order[idx]] == 1:
                    total_score = total_score + third
                    third = second
                    second = first
                    first = 1
                    idx = (idx + 1) % 9
                elif points[order[idx]] == 2:
                    total_score = total_score + second + third
                    third = first
                    second = 1
                    first = 0
                    idx = (idx + 1) % 9
                elif points[order[idx]] == 3:
                    total_score = total_score + first + second + third
                    third = 1
                    second = 0
                    first = 0
                    idx = (idx + 1) % 9
                elif points[order[idx]] == 4:
                    total_score = total_score + first + second + third + 1
                    first, second, third = 0, 0, 0
                    idx = (idx + 1) % 9

        results.append(total_score)
        return
    if index == 3:
        sort(index+1)
        # 이미 결정되있음.
    else:
        for i in range(1, 9):
            if i not in order:
                order[index] = i
                sort(index + 1)
                order[index] = -1

sort(0)
print(max(results))





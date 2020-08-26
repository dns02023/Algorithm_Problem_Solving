### 2020 KAKAO INTERNSHIP 경주로 건설 ###

import queue
def solution(board):
    cost_list = list()
    N = len(board)

    dr = [0, 0, 1, -1]
    dc = [1, -1, 0, 0]
    direcs = ['R', 'L', 'D', 'U']

    # 격자의 방문 여부를 고려하는 방식을 새롭게 생각해야함
    # 경로를 찾는 다는 것에 집중하지말고, 최소비용을 찾는 다는 것에 집중하자
    # => 각 board의 격자점마다 방문의 의미(0인지 아닌지) + 그 격자까지 도달하는 최소비용의 의미로
    # 도달 비용을 기록하자 => 방문했서 큐에 넣을지 말지는 0(방문안했음)과 그 격자점으로 더 저렴한 비용으로 업데이트가 가능한지 아닌지를 판단해서 결정
    # => 비용이 더 든다면 가지치기의 의미로 큐에 넣지 않는다.
    visit = [[0 for _ in range(N)] for _ in range(N)]

    q = queue.Queue()
    q.put([0, 0, 0, 'N'])
    visit[0][0] = 1
    # 이렇게 1원이라도 해줘야 다시 시작점을 방문하지 않음

    # 초기화 : 좌표 : (0,0), cost = 0, 방향 : 처음에는 방향이 없음
    while not q.empty():
        node = q.get()
        r, c, cost, direc = node[0], node[1], node[2], node[3]
        if (r == N - 1) and (c == N - 1):
            cost_list.append(cost)
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            new_cost = 0
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if board[nr][nc] == 0:
                if direc == 'N':
                    new_cost = cost + 100
                if (direc == 'R') or (direc == 'L'):
                    if cost == 700:
                        print(1)
                    if (direcs[i] == 'U') or (direcs[i] == 'D'):
                        new_cost = cost + 600
                    elif (direcs[i] == 'R') or (direcs[i] == 'L'):
                        new_cost = cost + 100
                if (direc == 'U') or (direc == 'D'):
                    if (direcs[i] == 'R') or (direcs[i] == 'L'):
                        new_cost = cost + 600
                    elif (direcs[i] == 'U') or (direcs[i] == 'D'):
                        new_cost = cost + 100
            else:
                continue

            if (visit[nr][nc] == 0) or (visit[nr][nc] >= new_cost):
                # 뒤에 >= 으로 해줘야 같은 값의 cost 경우의 수도 put 될수 있음
                if (nr == 1) and (nc == 1):
                    print(direcs[i])
                visit[nr][nc] = new_cost
                q.put([nr, nc, new_cost, direcs[i]])

    print(visit)

    return min(cost_list)
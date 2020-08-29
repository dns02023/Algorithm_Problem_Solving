import queue


N, M, F = map(int, input().split())
# F : 초기연료
space = [list(map(int, input().split())) for _ in range(N)]
s = list(map(int, input().split()))
start = [s[0]-1, s[1]-1, 0]
# 택시 출발점 좌표

people = [list(map(int, input().split())) for _ in range(M)]
# 손님 자료형 : [출발 행, 출발 열, 도착 행, 도착 열]*M

for i in range(len(people)):
    space[people[i][0]-1][people[i][1]-1] = i + 2
    # 손님 번호는 2번부터 시작
    # 즉 나중에 손님 목적지 호출할때, people[i+2 -2][2]-1, people[i+2 -2][3]-1


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def drive(fuel, count):

    # fuel : 현재 남은 연료, count : 현재까지 태운 손님 수
    global space, start, people, M
    #print(fuel, start)
    if count == M:
        return fuel

    target = list()
    #탐색이후 선정된 손님 [번호, 최단거리]
    visit = [[0]*N for _ in range(N)]
    q = queue.Queue()
    q.put(start)
    visit[start[0]][start[1]] = 1
    # bfs에서는 손님들의 최단거리만 계산해서 target 선정만 하자.
    search_count = 0
    # 현재 단계에서 손님을 탐색하는 횟수
    while not q.empty():
        [r, c, timecount] = q.get()
        # 손님이 있다면 후보군에 넣는다.
        if fuel <= timecount:
            #print('not enough fuel for target')
            return -1
        # 아래 조건에 의해 가까운 손님을 찾으면 더 멀리 탐색을 하지 않는다. 이러한 상황에서 timecount가 연료 이상 들면 실패임
        if len(target) != 0:
            # 현재 가장 가까운 손님보다 더 멀리 탐색한다면 break
            if timecount > target[1]:
                break
        if space[r][c] > 1:
            # 손님을 찾았다.
            if len(target) == 0:
                #아직 찾은 손님이 없을 때,
                target = [space[r][c], timecount]
            else:
                #찾은 손님이 있으면 비교 시작
                # if target[1] > timecount:
                #     #이건 말이 안되는 거 같은데.. 어차피 timecount는 증가하니까 같은 경우만 비교하면 될듯
                #     target = [space[r][c], timecount]
                if target[1] == timecount:
                    if people[target[0] - 2][0] - 1 > r:
                        target = [space[r][c], timecount]
                    elif people[target[0] - 2][0] - 1 == r:
                        if people[target[0] - 2][1] - 1 > c:
                            target = [space[r][c], timecount]
            search_count = search_count + 1
            # 남은 손님들을 모두 탐색했다면,
            if search_count == M - count:
                break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < N) and (nr >= 0 ) and (nc < N) and (nc >= 0):
                if space[nr][nc] == 1:
                    continue
                if visit[nr][nc] == 0:
                    q.put([nr, nc, timecount+1])
                    visit[nr][nc] = 1

    #target 선정완료 => 태우러 감
    #만약 target을 탐색못했다면?
    #=>길이 막혀서 도달이 불가능 하다는 것
    if len(target) == 0:
        #print('no target')
        return -1

    fuel = fuel - target[1]

    idx = target[0]
    start2 = [people[idx-2][0] - 1, people[idx-2][1] - 1, 0]
    space[start2[0]][start2[1]] = 0

    dest = [people[idx-2][2] - 1, people[idx-2][3] - 1]

    d_visit = [[0] * N for _ in range(N)]
    d_q = queue.Queue()
    d_q.put(start2)
    d_visit[start2[0]][start2[1]] = 1

    consume = 0
    stop = 0
    arrive = 0
    while not d_q.empty():
        [r, c, timecount] = d_q.get()
        if fuel - timecount < 0:
            #어차피 timecount는 증가하므로 fuel을 초과하게 되면 도달 불가, 실패
            stop = 1
            break
        if (r == dest[0]) and (c == dest[1]):
            consume = timecount
            arrive = 1
            #도착했으면 1로 해줌
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if (nr < N) and (nr >= 0 ) and (nc < N) and (nc >= 0):
                if space[nr][nc] == 1:
                    continue
                if d_visit[nr][nc] == 0:
                    d_q.put([nr, nc, timecount+1])
                    d_visit[nr][nc] = 1

    if stop == 1:
        #print('not enough fuel for dest')
        #연료가 부족하여 도착을 못하면
        return -1
    if arrive == 0:
        #print('목적지 도달불가')
        #도달불가 도착을 못하면
        return -1

    fuel = fuel - consume
    fuel = fuel + 2*consume
    start = [dest[0], dest[1], 0]
    count = count + 1
    return drive(fuel, count)

print(drive(F, 0))















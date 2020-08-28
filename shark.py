import queue
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

shark = list()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            shark.append(i)
            shark.append(j)

dr = [0, 0, 1, -1] #row변화
dc = [1, -1, 0, 0] #column변화
     #right, left, up, down

#bfs로 최단거리를 구할 수 있다. 간선의 가중치가 1이므로, bfs tree의 level(depth)가 증가할때마다 time_count 배열의 요소값을 1씩 증가시킨다.
def feed(map, shark_size, location, feed_count, feed_time):
    map[location[0]][location[1]] = 0
    fish = list()
    #먹을 수 있는 물고기들의 좌표를 저장(list)
    fish_time_count = [[0]*N for _ in range(N)]
    #상어가 해당 fish좌표까지 이동하는 데 걸리는 시간을 저장(NxN)
    flag = [[0]*N for _ in range(N)]
    q = queue.Queue()
    q.put(location)
    flag[location[0]][location[1]] = 1
    time_count = [[0]*N for _ in range(N)]
    while q.empty() != 1:
        r, c = q.get()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and flag[nr][nc] == 0:
                if 0 < map[nr][nc] < shark_size:
                    time_count[nr][nc] = time_count[r][c] + 1
                    #이동할 수 있으므로, time_count 증가
                    #이전 bfs tree의 level(depth)의 time_count에다가 +1을 해주면 현재 depth까지 오는데 걸린 거리
                    fish.append([nr, nc])
                    #먹을 수 있으므로, fish에 추가
                    flag[nr][nc] = 1
                    fish_time_count[nr][nc] = time_count[nr][nc]
                    #해당 fish를 잡아 먹는데 걸리는 시간
                    #먹을 수 있는 물고기를 발견했으므로 이곳에서 더이상 탐색을 하지않음. 큐에 넣지 않는다.
                elif map[nr][nc] == shark_size or map[nr][nc] == 0:
                    time_count[nr][nc] = time_count[r][c] + 1
                    # 이동할 수 있으므로, time_count 증가
                    q.put([nr, nc])
                    #지나만 갈 수 있으므로, 이곳에서 다시 탐색을 해야함. 큐에 넣는다.
                    flag[nr][nc] = 1
    #fish, fish_time_count 완성
    #어떤 fish를 먹을지 결정해야함
    if len(fish) == 0:
        return feed_time
    else:
        shortcut = fish_time_count[fish[0][0]][fish[0][1]]
        cand = list()
        for i in range(len(fish)):
            if shortcut > fish_time_count[fish[i][0]][fish[i][1]]:
                shortcut = fish_time_count[fish[i][0]][fish[i][1]]
        for i in range(len(fish)):
            if fish_time_count[fish[i][0]][fish[i][1]] == shortcut:
                cand.append(fish[i])
        if len(cand) == 1:
            food = cand[0]
        else:
            highest = cand[0][0]
            cand2 = list()
            for i in range(len(cand)):
                if highest > cand[i][0]:
                    highest = cand[i][0]
            for i in range(len(cand)):
                if cand[i][0] == highest:
                    cand2.append(cand[i])
            if len(cand2) == 1:
                food = cand2[0]
            else:
                leftmost = cand2[0][1]
                final = list()
                for i in range(len(cand2)):
                    if leftmost > cand2[i][1]:
                        leftmost = cand2[i][1]
                for i in range(len(cand2)):
                    if cand2[i][1] == leftmost:
                        final.append(cand2[i])
                food = final[0]

                # 최종 food 선정 완료
        map[food[0]][food[1]] = 0
        feed_count = feed_count + 1
        feed_time = feed_time + fish_time_count[food[0]][food[1]]


        if feed_count == shark_size:
            shark_size = shark_size + 1
            feed_count = 0

        return feed(map, shark_size, food, feed_count, feed_time)

print(feed(arr, 2, shark, 0, 0))

































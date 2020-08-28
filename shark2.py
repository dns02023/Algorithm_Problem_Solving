import copy
arr = [list(map(int, input().split())) for _ in range(4)]

# 물고기 list 자료형 2개 만들자 => 위치 격자 map, 물고기 번호 순으로 나열한 list
space = [list() for _ in range(4)]
fish_list = [0]*16
# 인덱스가 물고기 번호 -1 [물고기 행 좌표, 물고기 열 좌표, 방향]

for r in range(4):
    for c in range(4):
        temp = [arr[r][2*c], arr[r][2*c+1]]
        space[r].append(temp)
        temp2 = [r, c, arr[r][2*c+1]]
        fish_list[arr[r][2*c]-1] = temp2

# print(space)
# print(fish_list)

# ↑, ↖, ←, ↙, ↓, ↘, →, ↗
# 1 ,2 ,3 ,4 ,5, 6, 7, 8
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

#상어 좌표
sh = list()
results = list()

def dfs(feed, shark):
   # print(feed)

    global space
    global fish_list

    #print(space)

    if feed == 0:
        start = space[0][0]
        fish_list[start[0]-1] = 'N'
        space[0][0] = ['s', start[1]]
        shark = [0, 0]

        dfs(start[0], shark)
        return

    #물고기 이동
    for i in range(16):
        fish = fish_list[i]
        if fish == 'N':
            continue
        [r, c, dir] = fish
        nr = r + dr[dir-1]
        nc = c + dc[dir-1]

        dir_flag = False
        # 이동할 수 있을 때 까지 반시계 방향 회전
        while not dir_flag:
            if (nr < 4) and (nc < 4) and (nr >= 0) and (nc >= 0):
                if space[nr][nc][0] != 's':
                    dir_flag = True
                else:
                    if dir == 8:
                        dir = 1
                    else:
                        dir = dir + 1

                    nr = r + dr[dir - 1]
                    nc = c + dc[dir - 1]

            else:
                if dir == 8:
                    dir = 1
                else:
                    dir = dir + 1
                # 방향 반시계 회전

                nr = r + dr[dir - 1]
                nc = c + dc[dir - 1]

        space[r][c][1] = dir
        #스왑할 물고기 지정 완료
        swap_fish = space[nr][nc]
        if swap_fish == [0, 0]:
            space[r][c], space[nr][nc] = space[nr][nc], space[r][c]
            fish_list[i] = [nr, nc, dir]
            #빈칸으로 이동한다면,
            #space는 [0,0]이 되고, 이미 죽은 물고기의 상태는 바꿔줄 필요가 없음
        else:
            space[r][c], space[nr][nc] = space[nr][nc], space[r][c]
            # 물고기들의 위치를 바꿔준다. 방향은 그대로
            fish_list[swap_fish[0] - 1] = [r, c, swap_fish[1]]
            fish_list[i] = [nr, nc, dir]
   # print(space)
   # print(fish_list)

    [shark_r, shark_c] = shark
    shark_dir = space[shark_r][shark_c][1]
    #상어는 회전 못함
    nr = shark_r + dr[shark_dir-1]
    nc = shark_c + dc[shark_dir-1]

    #dfs 종료 조건(상어가 움직일 수 없음)
    if (nr >= 4) or (nc >= 4) or (nr < 0) or (nc < 0):
        results.append(feed)
        return

    #이동할 수 있는 후보 격자들
    targets = list()
    while (nr < 4) and (nc < 4) and (nr >= 0) and (nc >= 0):
        if space[nr][nc] == [0, 0]:
            nr = nr + dr[shark_dir - 1]
            nc = nc + dc[shark_dir - 1]
            continue
        targets.append([nr, nc])
        nr = nr + dr[shark_dir-1]
        nc = nc + dc[shark_dir-1]

    if len(targets) == 0:
        results.append(feed)
        return


    # dfs 탐색 시작
    for i in range(len(targets)):
        target = targets[i]
        copy_space = copy.deepcopy(space)
        copy_fish_list = copy.deepcopy(fish_list)

        #상어가 잡아 먹으면 space는 ['s', 방향]
        #그 space를 차지하고 있던 물고기는 fish_list에서 'N'이 된다.
        #그리고 원래 상어가 차지하고 있던 space는 [0, 0]으로 만든다.

        target_fish = space[target[0]][target[1]]
        space[shark_r][shark_c] = [0, 0]
        fish_list[target_fish[0] - 1] = 'N'
        space[target[0]][target[1]] = ['s', target_fish[1]]

        dfs(feed + target_fish[0], target)
        space = copy_space
        fish_list = copy_fish_list


dfs(0, sh)
print(max(results))



























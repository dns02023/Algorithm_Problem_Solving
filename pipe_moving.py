N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
pipe = [[0, 0], [0, 1]]
count = 0

def move():
    global arr, pipe, count

    if pipe[1] == [N-1, N-1]:
        count = count + 1
        return
    else:
        # pipe의 모양에 따라 3가지 방법이 있음
        # 가로
        if pipe[0][0] == pipe[1][0]:
            [r, c] = pipe[0]
            for i in range(2):
                # 공간을 벗어나거나, 벽이면 패스
                if i == 0:
                    if (r < N) and (r >= 0) and (c+2 < N) and (c+2 >= 0):
                        if arr[r][c+2] == 1:
                            continue
                        else:
                            pipe = [[r, c + 1], [r, c + 2]]
                            move()
                            pipe = [[r, c], [r, c+1]]
                else:
                    if (r+1 < N) and (r+1 >= 0) and (c+2 < N) and (c+2 >= 0):
                        if (arr[r+1][c+2] == 1) or (arr[r+1][c+1] ==1) or (arr[r][c+2] ==1):
                            continue
                        else:
                            pipe = [[r, c + 1], [r + 1, c + 2]]
                            move()
                            pipe = [[r, c], [r, c + 1]]



        # 세로
        elif pipe[0][1] == pipe[1][1]:
            [r, c] = pipe[0]
            for i in range(2):
                # 공간을 벗어나거나, 벽이면 패스
                if i == 0:
                    if (r+2 < N) and (r+2 >= 0) and (c < N) and (c >= 0):
                        if arr[r+2][c] == 1:
                            continue
                        else:
                            pipe = [[r+1, c], [r+2, c]]
                            move()
                            pipe = [[r, c], [r+1, c]]
                else:
                    if (r + 2 < N) and (r + 2 >= 0) and (c + 1 < N) and (c + 1 >= 0):
                        if (arr[r + 2][c + 1] == 1) or (arr[r + 2][c] == 1) or (arr[r+1][c + 1] == 1):
                            continue
                        else:
                            pipe = [[r + 1, c], [r + 2, c + 1]]
                            move()
                            pipe = [[r, c], [r+1, c]]
                # 대각선
        else:
            [r, c] = pipe[0]
            for i in range(3):
                if i == 0:
                    if (r+1 < N) and (r+1 >= 0) and (c+2 < N) and (c+2 >= 0):
                        if arr[r+1][c+2] == 1:
                            continue
                        else:
                            pipe = [[r + 1, c+1], [r+1, c+2]]
                            move()
                            pipe = [[r, c], [r+1, c+1]]

                elif i == 1:
                    if (r+2 < N) and (r+2 >= 0) and (c+1 < N) and (c+1 >= 0):
                        if arr[r+2][c+1] == 1:
                            continue
                        else:
                            pipe = [[r + 1, c+1], [r+2, c+1]]
                            move()
                            pipe = [[r, c], [r+1, c+1]]

                else:
                    # 공간을 벗어나거나, 벽이면 패스
                    if (r+2 < N) and (r+2 >= 0) and (c+2 < N) and (c+2 >= 0):
                        if (arr[r+2][c+2] == 1) or (arr[r+2][c+1] ==1) or (arr[r+1][c+2] ==1):
                            continue
                        else:
                            pipe = [[r + 1, c + 1], [r + 2, c + 2]]
                            move()
                            pipe = [[r, c], [r+1, c+1]]

move()
print(count)

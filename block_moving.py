import queue

#로봇의 현재 상태와 현재상태에 도달하기 위해 걸린 시간 정보를 담은 것이 code이다
#code : [수직or수평, 위치, 위치, 위치, 상태에 도달시간]

def solution(board):
    result = 0
    N = len(board)
    robot = ['h', 0, 0, 1, 0]
    #초기 로봇은 수평 [0, 0], [0,1]좌표에 위치하고 경과시간 == 0이다.
    visit = list()
    h_dr = [-1, 1, 0, 0]
    h_dc = [0, 0, -1, 1]
    h_dc2 = [0, 0, -1, 1]
    v_dr = [0, 0, 1, -1]
    v_dr2 = [0, 0, 1, -1]
    v_dc = [-1, 1, 0, 0]

    q = queue.Queue()
    q.put(robot)
    while q.empty() != 1:
        code = q.get()
        buffer = list()
        time = code[4]
        if code[0] == 'h':
            r, c, c2 = code[1], code[2], code[3]

            buffer.append(code)
            # 직선으로 움직이는 경우 4가지
            for i in range(4):
                nr = r + h_dr[i]
                nc = c + h_dc[i]
                nc2 = c2 + h_dc2[i]
                if 0 <= nr < N and 0 <= nc < N and 0 <= nc2 < N:
                    if board[nr][nc] != 1 and board[nr][nc2] != 1:
                        if ['h', nr, nc, nc2] not in visit:
                            q.put(['h', nr, nc, nc2, time+1])
                            buffer.append(['h', nr, nc, nc2, time+1])


            # 회전하는 경우 4가지
            if 0 <= (r - 1) < N:
                if board[r - 1][c2] != 1 and board[r-1][c] != 1:
                    if ['v', r - 1, r, c] not in visit:
                        q.put(['v', r - 1, r, c, time+1])
                        buffer.append(['v', r - 1, r, c, time+1])
            if 0 <= (r + 1) < N:
                if board[r + 1][c2] != 1 and board[r+1][c] != 1:
                    if ['v', r, r + 1, c] not in visit:
                        q.put(['v', r, r + 1, c, time+1])
                        buffer.append(['v', r, r + 1, c, time+1])
            if 0 <= (r - 1) < N:
                if board[r - 1][c] != 1 and board[r-1][c2] != 1:
                    if ['v', r - 1, r, c2] not in visit:
                        q.put(['v', r - 1, r, c2, time+1])
                        buffer.append(['v', r - 1, r, c2, time+1])
            if 0 <= (r + 1) < N:
                if board[r + 1][c] != 1 and board[r+1][c2] != 1:
                    if ['v', r, r + 1, c2] not in visit:
                        q.put(['v', r, r + 1, c2, time+1])
                        buffer.append(['v', r, r + 1, c2, time+1])

        elif code[0] == 'v':
            r, r2, c = code[1], code[2], code[3]

            buffer.append(code)
            # 직선으로 움직이는 경우 4가지
            for i in range(4):
                nr = r + v_dr[i]
                nr2 = r2 + v_dr2[i]
                nc = c + v_dc[i]
                if 0 <= nr < N and 0 <= nc < N and 0 <= nr2 < N:
                    if board[nr][nc] != 1 and board[nr2][nc] != 1:
                        if ['v', nr, nr2, nc] not in visit:
                            q.put(['v', nr, nr2, nc, time + 1])
                            buffer.append(['v', nr, nr2, nc, time+1])


            if 0 <= (c + 1) < N:
                if board[r2][c + 1] != 1 and board[r][c+1] != 1:
                    if ['h', r, c, c + 1] not in visit:
                        q.put(['h', r, c, c + 1, time+1])
                        buffer.append(['h', r, c, c + 1, time+1])
                if board[r][c + 1] != 1 and board[r2][c+1] != 1:
                    if ['h', r2, c, c + 1] not in visit:
                        q.put(['h', r2, c, c + 1, time+1])
                        buffer.append(['h', r2, c, c + 1, time+1])
            if 0 <= (c - 1) < N:
                if board[r2][c - 1] != 1 and board[r][c-1] != 1:
                    if ['h', r, c - 1, c] not in visit:
                        q.put(['h', r, c - 1, c, time+1])
                        buffer.append(['h', r, c - 1, c, time+1])
                if board[r][c - 1] != 1 and board[r2][c-1] != 1:
                    if ['h', r2, c - 1, c] not in visit:
                        q.put(['h', r2, c - 1, c, time+1])
                        buffer.append(['h', r2, c - 1, c, time+1])
        for b in range(len(buffer)):
            visit.append(buffer[b][0:4])


        if (['h', N-1, N-2, N-1] in visit) or (['v', N-2, N-1, N-1] in visit):
            result = time + 1
            break

    return result

ex = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(ex))

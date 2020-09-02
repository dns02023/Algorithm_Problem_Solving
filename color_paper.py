# 10*10 격자이므로 모든 격자점(0 or 1)들에 대해서 다 탐색하는 브루트포스 방식으로 접근해야 함.
# 브루트포스가 가능할 것 같은 문제에서는 과감하게 시도해보자..
# 처음에는 1인 격자점들에 대해서만 완전탐색하는 방식을 시도했는데, 1인 격자점에 대해서 빠르게 접근하려고 격자점 좌표들을 저장하는
# 자료형을 썼다가 오히려 시간복잡도가 증가하고 에러가 발생했음.. 불필요한 자료형을 줄이는게 시간복잡도 측면에서 유리함
# 10*10으로 탐색 수가 크지 않기 때문에 별도의 자료형없이 주어진 격자 배열만으로 브루트포스를 적용하는게 더 효율적임

def solution(start):
    global result, arr, result_count, counts
    # 전역변수 사용시에는 되도록 global을 쓰도록하자.. list라 할지라도 referenced before assignment error가 발생할 수 있음
    row = start[0]
    col = start[1]
    # start 좌표를 맨 좌측 최상단으로 하도록 색종이들을 크기별로 붙이는 dfs 탐색 시작
    if (row == 10):
        # 종료조건 : 맨 마지막 (9,9) 좌표까지 탐색하고 좌표 밖의 10번째 행이 지정되면 탐색 완료인 상황
        count = sum(counts)
        # 5가지 색종이들의 각 갯수들의 총합
        if result == -1:
            # 초기값 -1 이라면
            result = count
            # 비교없이 설정
        else:
            if result > count:
                # 비교
                result = count
        return
    if arr[row][col] == 0:
        # 덮을 필요없는 0 격자점이므로 바로 다음 상태 노드로 탐색 돌입
        # 모든 열 탐색했으면 다음 행으로 돌입
        if col == 9:
            solution([row + 1, 0])
        # 같은 행의 다음 열로 돌입
        elif col < 9:
            solution([row, col + 1])
    # elif 써야한다. 이 함수에서는 다음 상태 노드로 넘기고 끝내야 하므로, 혹시나 arr 값이 어떻게 변하게 될지 모르므로..
    elif arr[row][col] == 1:
        # 덮어야 할 격자점 => 각 크기의 색종이들을 붙여보는 상태노드들을 탐색한다.
        for i in range(4, -1, -1):
            # 큰 것부터 붙여보기
            if counts[i] == 5:
                # 해당 크기의 색종이를 다썼으면 continue (가지치기)
                continue
            mr = row + i
            mc = col + i
            # 해당 크기의 색종이 붙였을 때의 행과 열의 최대 값
            if (mr >= 10) or (mc >= 10):
                # 경계를 벗어나면 가지치기
                continue
            flag = 0
            # 색종이를 붙일 격자점들을 하나씩 탐색하면서 0이면, break 때리고 가지치기
            covered = list()
            # 덮어서 없애버릴 1 격자점들의 좌표값을 담는 배열
            for r in range(row, mr + 1):
                for c in range(col, mc + 1):
                    if arr[r][c] == 0:
                        flag = 1
                        break
                    covered.append([r, c])
                    # 0아니면 덮자
                if flag == 1:
                    break
            if flag == 1:
                #못 덮으니까 가지치기
                continue

            counts[i] = counts[i] + 1
            # 쓴 색종이는 카운트를 기록해주고
            for cov in covered:
                arr[cov[0]][cov[1]] = 0
                # 덮는 작업
            #다음 상태 노드 탐색
            if col == 9:
                solution([row+1, 0])
            elif col < 9:
                solution([row, col+1])
            #dfs이후 다음 자식 상태 노드 탐색을 위한 자료형 복구 작업
            counts[i] = counts[i] - 1
            for cov in covered:
                arr[cov[0]][cov[1]] = 1


arr = [list(map(int, input().split())) for _ in range(10)]

result = -1
counts = [0, 0, 0, 0, 0]

solution([0,0])
print(result)
















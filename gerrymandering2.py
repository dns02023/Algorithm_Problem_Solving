#문제 조건보면서 차분하게 구현하면 됨
#경계선만 표시해주고 1, 2, 3, 4 번째구의 인구들 부터 구하자.
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
#구를 정하기 위해서 각 구마다 사용할 border 인덱스
entire = 0
for i in range(N):
    for j in range(N):
        entire = entire + arr[i][j]


def gerrymandering(map):
    answer = entire
    for r in range(N):
        for c in range(N):
            point = [r, c]
            #기준점
            for d1 in range(1, c+1):
                for d2 in range(1, N-c):
                    #문제의 조건을 활용하여 d1, d2의 범위 결정
                    if (d1 + d2) > N-1-r:
                        #인덱스 초과
                        continue
                    population = list()
                    number = [[0]*N for _ in range(N)]
                    for i in range(d1+1):
                        number[r+i][c-i] = 5
                        number[r+d2+i][c+d2-i] =5
                    for i in range(d2+1):
                        number[r+i][c+i] = 5
                        number[r+d1+i][c-d1+i] = 5
                    #1번 선거구
                    first = 0
                    for x in range(r+d1):
                        for y in range(c+1):
                            if number[x][y] != 0:
                                break
                            number[x][y] = 1
                            first = first + map[x][y]
                    population.append(first)
                    second = 0
                    for x in range(r+d2+1):
                        for y in range(N-1, c, -1):
                            if number[x][y] != 0:
                                break
                            number[x][y] = 2
                            second = second + map[x][y]
                    population.append(second)
                    third = 0
                    for x in range(r+d1, N):
                        for y in range(c-d1+d2):
                            if number[x][y] != 0:
                                break
                            number[x][y] = 3
                            third = third + map[x][y]
                    population.append(third)
                    fourth = 0
                    for x in range(r+d2, N):
                        for y in range(N-1, c-d1+d2-1, -1):
                            if number[x][y] != 0:
                                break
                            number[x][y] = 4
                            fourth = fourth + map[x][y]
                    population.append(fourth)

                    fifth = entire - sum(population)
                    #전체에서 나머지 구들 인구수 빼주면 5번째 구 인구수가 나온다.
                    population.append(fifth)
                    ans = max(population) - min(population)
                    if answer > ans:
                        answer = ans
    return answer

print(gerrymandering(arr))




















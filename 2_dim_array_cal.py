R, C, K = map(int, input().split())
R = R - 1
C = C - 1
a = [list(map(int, input().split())) for _ in range(3)]

def swap(x, i, j):
    x[i], x[j] = x[j], x[i]
def Sort(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i][1] > x[i+1][1]:
                swap(x, i, i+1)
            elif x[i][1] == x[i+1][1]:
                if x[i][0] > x[i+1][0]:
                    swap(x, i, i + 1)

def expansion(arr, row, column, key, cnt):
    if cnt > 100:
        return -1
    row_num = len(arr)
    column_num = len(arr[0])
    if row_num > row and column_num > column:
        if arr[row][column] == key:
            return cnt
    cnt = cnt + 1

    new_arr = list()
    length = 0
    if row_num >= column_num:
        #행정렬
        for i in range(row_num):
            #모든 행배열들에 대해서
            array = arr[i]
            #정렬할 행배열 지정
            pairs = list()
            #[number, count] 숫자, 등장횟수로 구성된 짝들
            for j in range(len(array)):
                if j > 99:
                    break
                number = array[j]
                if number == 0:
                    continue
                flag = 0
                if len(pairs) != 0:
                    for p in pairs:
                        if p[0] == number:
                            p[1] = p[1] + 1
                            flag = 1
                            break
                if flag == 0:
                    pairs.append([number, 1])
            #pairs 완성 => 새로운 행배열 array만들기
            Sort(pairs)
            #print(pairs)
            temp = list()
            for p in pairs:
                temp = temp + p
            #print(temp)
            if len(temp) > length:
                length = len(temp)
            new_arr.append(temp)
        for row_arr in new_arr:
            if len(row_arr) < length:
                for _ in range(length-len(row_arr)):
                    row_arr.append(0)

    elif row_num < column_num:
        #열배열 가져오기
        T_arr = list()
        for c in range(column_num):
            col_vector = list()
            for r in range(row_num):
                if r > 99:
                    break
                col_vector.append(arr[r][c])
            #column vector 완성
            pairs = list()
            for v in range(len(col_vector)):
                number = col_vector[v]
                if number == 0:
                    continue
                flag = 0
                if len(pairs) != 0:
                    for p in pairs:
                        if p[0] == number:
                            p[1] = p[1] + 1
                            flag = 1
                            break
                if flag == 0:
                    pairs.append([number, 1])
            Sort(pairs)
            temp = list()
            for p in pairs:
                temp = temp + p
            if len(temp) > length:
                length = len(temp)
            T_arr.append(temp)
        for col_arr in T_arr:
            if len(col_arr) < length:
                for _ in range(length-len(col_arr)):
                    col_arr.append(0)
        #T_arr을 다시 transpose 시켜주면 new_arr완성
        new_arr = [[0]*column_num for _ in range(length)]
        for k in range(length):
            for h in range(column_num):
                new_arr[k][h] = T_arr[h][k]

    return expansion(new_arr, row, column, key, cnt)


print(expansion(a, R, C, K, 0))


### 2019 KAKAO 개발자 겨울 인턴십 기출 문제 ###
def solution(board, moves):
    bucket = list()
    result = 0

    for move in moves:
        crane = 0
        idx = move - 1

        for r in range(len(board)):
            if board[r][idx] != 0:
                crane = board[r][idx]
                board[r][idx] = 0
                break

        if crane == 0:
            continue

        if len(bucket) == 0:
            bucket.append(crane)
            continue

        flag = 0
        while bucket[-1] == crane:
            flag = 1
            bucket.pop()
            result = result + 1
            if len(bucket) == 0:
                break

        if flag == 1:
            result = result + 1
        else:
            bucket.append(crane)

    return result
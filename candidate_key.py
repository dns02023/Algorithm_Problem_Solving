import itertools
def solution(relation):
    candidate_key = list()
    att_num = len(relation[0])
    att_set = list()
    for i in range(att_num):
        att_set.append(i)

    for i in range(1, att_num+1):
        #attribute 조합 생성
        key_com = list(itertools.combinations(att_set, i))
        key_set = list()
        for k in key_com:
            key_set.append(list(k))

        for key in key_set:
            buffer = list()
            for tuple in relation:
                tuple_buffer = list()
                for key_index in range(len(key)):
                    tuple_buffer.append(tuple[key[key_index]])
                if tuple_buffer not in buffer:
                    buffer.append(tuple_buffer)
            key = set(key)
            if len(buffer) == len(relation):
                #유일성 체크
                if len(candidate_key) == 0:
                    candidate_key.append(key)
                else:
                    flag = 1
                    for c in range(len(candidate_key)):
                        if ((candidate_key[c] & key) == key) or ((candidate_key[c] & key) == candidate_key[c]):
                            flag = 0
                            # 희소성 위배
                    if flag:
                        candidate_key.append(key)


    return len(candidate_key)

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
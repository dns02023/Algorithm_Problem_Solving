### 2019 카카오 개발자 겨울 인턴십 기출문제 : 튜플###
def solution(s):
    s_list = list(s)
    set_list = list()

    temp = list()
    number = ''
    subset_start = 0
    for i in range(len(s_list)):
        if (i == 0) or (i == len(s_list) - 1):
            continue
        if s_list[i] == '{':
            subset_start = 1
            continue
        if s_list[i] == '}':
            subset_start = 0
            temp.append(int(number))
            number = ''
            set_list.append(temp)
            temp = list()
            continue

        if (s_list[i] == ','):
            if subset_start == 1:
                temp.append(int(number))
                number = ''

        else:
            number = number + s_list[i]

    result = [0] * (len(set_list))
    for i in range(len(set_list)):
        length = i + 1
        for j in range(len(set_list)):
            if len(set_list[j]) == length:
                for val in set_list[j]:
                    if val not in result:
                        result[length - 1] = val
                        break

    return result
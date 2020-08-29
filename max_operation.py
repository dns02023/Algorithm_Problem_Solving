import copy


def solution(expression):
    ex_list = list(expression)

    global oper, cands, sorts

    oper = list()
    cands = list()
    sorts = list()

    expression_list = list()

    temp = ''
    for i in range(len(ex_list)):
        if ex_list[i] in ['-', '*', '+']:
            if ex_list[i] not in oper:
                oper.append(ex_list[i])
            expression_list.append(int(temp))
            expression_list.append(ex_list[i])
            temp = ''
        else:
            temp = temp + ex_list[i]
            if i == len(ex_list)-1:
                expression_list.append(int(temp))

    priority(0)
    # print(expression_list)

    dic = dict()
    for o in oper:
        dic[o] = 0

    for i in range(len(expression_list)):
        if type(expression_list[i]) != int:
            dic[expression_list[i]] = dic[expression_list[i]] + 1

    answer = 0
    print(expression_list)
    for sort in cands:
        result = 0
        copy_ex = copy.deepcopy(expression_list)
        for operand in sort:
            num = dic[operand]
            cnt = 0
            while cnt != num:
                print(copy_ex)
                idx = 0
                output = 0
                for i in range(len(copy_ex)):
                    if copy_ex[i] == operand:
                        idx = i
                        break
                if operand == '*':
                    output = copy_ex[idx - 1] * copy_ex[idx + 1]
                if operand == '+':
                    output = copy_ex[idx - 1] + copy_ex[idx + 1]
                if operand == '-':
                    output = copy_ex[idx - 1] - copy_ex[idx + 1]

                del copy_ex[idx]
                del copy_ex[idx]
                copy_ex[idx - 1] = output
                cnt = cnt + 1

        if len(copy_ex) == 1:
            if copy_ex[0] < 0:
                result = abs(copy_ex[0])
                if answer < result:
                    answer = result
            else:
                result = copy_ex[0]
                if answer < result:
                    answer = result

    return answer


def priority(count):
    if len(sorts) == len(oper):
        cands.append(copy.deepcopy(sorts))
        return
    for i in range(len(oper)):
        if oper[i] not in sorts:
            sorts.append(oper[i])
            priority(count + 1)
            sorts.remove(oper[i])

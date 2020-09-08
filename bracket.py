complete = list()
def sol(p):
    #빈칸인가?
    if len(p) == 0:
        b = ''
        complete.append(b)
        return

    #균형잡힌 괄호인가?
    if balanced(p) == 0:
        print('fail')
        return

    #올바른 괄호인가?
    if appropriate(p) == 1:
        complete.append(p)
        return

    #이제부터 균형잡혀있지만 올바르진 않은 괄호들을 split하는 과정
    num_right = 0
    num_left = 0
    split_point = 0
    for index in range(len(p)):
        if p[index] == ')':
            num_right = num_right + 1
        else:
            num_left = num_left + 1
        if num_right == num_left:
            split_point = index
            #최초로 균형이 잡히는 지점이므로, 이곳을 기준으로 자르면 더이상 나눌수 없는 균형잡힌 괄호 문자열이 된다.
            break

    u = p[0:split_point+1]
    v = p[split_point+1:]
    left_temp = '('
    right_temp = ')'

    if appropriate(u) == 1:
        complete.append(u)
        sol(v)

    else:
        complete.append(left_temp)
        sol(v)
        complete.append(right_temp)

        del u[0]
        del u[-1]
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        complete.append(u)

def balanced(string):
    num_right = 0
    num_left = 0
    # 균형잡힌 괄호인가?
    for i in range(len(string)):
        if string[i] == ')':
            num_right = num_right + 1
        else:
            num_left = num_left + 1
    if num_right != num_left:
        return 0
    else:
        return 1

def appropriate(string):
    # 올바른 괄호인가?
    num_right = 0
    num_left = 0
    for i in range(len(string)):
        if string[i] == ')':
            num_right = num_right + 1
        else:
            num_left = num_left + 1
        if num_right > num_left:
            return 0

        if i == len(string) - 1:
            return 1


a = list('()))((()')
print(a)
sol(a)
print(complete)
first = ''
for i in range(len(complete)):
    s = ''.join(complete[i])
    first = first + s
print(first)

















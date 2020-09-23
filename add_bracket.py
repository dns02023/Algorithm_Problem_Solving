import copy
N = int(input())
arr = list(map(str, input()))
# for i in range(len(arr)):
#     if arr[i].isdigit():
#         arr[i] = int(arr[i])

results = list()
operators = list()

def cal(number, cands):
    global operators
    if len(operators) == number:
        operators = sorted(operators)
        if operators not in cands:
            cands.append(copy.deepcopy(operators))
        return
    for i in range(1, N, 2):
        if ((i+2) in operators) or (i in operators) or ((i-2) in operators):
            continue
        operators.append(i)
        cal(number, cands)
        operators.pop()

num = 0
while True:
    temps = list()
    cal(num, temps)
    if len(temps) == 0:
        break
    #print(temps)
    for temp in temps:
        copy_arr = copy.deepcopy(arr)
        for i in range(num):
            idx = temp[i]
            value = 0
            if arr[idx] == '+':
                value = int(arr[idx-1]) + int(arr[idx+1])
            elif arr[idx] == '-':
                value = int(arr[idx-1]) - int(arr[idx+1])
            else:
                value = int(arr[idx - 1]) * int(arr[idx + 1])
            copy_arr[idx-1] = ''
            copy_arr[idx] = str(value)
            copy_arr[idx+1] = ''
        new = list()
        for one in copy_arr:
            if one != '':
                new.append(one)

        #print(new)
        while True:
            if len(new) == 1:
                results.append(int(new[0]))
                break
            else:
                value = 0
                if new[1] == '+':
                    value = int(new[0]) + int(new[2])
                elif new[1] == '-':
                    value = int(new[0]) - int(new[2])
                else:
                    #print(new[1])
                    value = int(new[0]) * int(new[2])
                del new[0]
                del new[0]
                new[0] = str(value)
    num = num + 1



print(max(results))






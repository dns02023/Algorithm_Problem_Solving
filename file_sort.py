def solution(files):
    indices = list()
    heads = list()
    numbers = list()
    tails = list()

    idx = 0
    for file in files:
        indices.append(idx)
        idx = idx + 1

        ch_list = list(file)

        head = ''
        number = ''
        tail = ''

        flag = ''
        for i in range(len(ch_list)):
            if ch_list[i].isalpha():
                ch_list[i] = ch_list[i].lower()

            if i == 0:
                flag = 'head'
                head = head + ch_list[i]
            else:
                if not ch_list[i].isdigit():

                    if flag == 'head':
                        head = head + ch_list[i]
                    elif flag == 'number':
                        tail = tail + ch_list[i]
                        flag = 'tail'
                    elif flag == 'tail':
                        tail = tail + ch_list[i]

                elif ch_list[i].isdigit():
                    if flag == 'head':
                        number = number + ch_list[i]
                        flag = 'number'
                    elif flag == 'number':
                        if len(number) <= 5:
                            number = number + ch_list[i]
                        else:
                            tail = tail + ch_list[i]
                            flag = 'tail'
                    elif flag == 'tail':
                        tail = tail + ch_list[i]

        heads.append(head)
        numbers.append(number)
        tails.append(tail)

    # print(heads)
    # print(numbers)
    # print(tails)

    for i in range(len(heads)):

        for j in range(len(heads) - 1 - i):
            if heads[j] > heads[j + 1]:
                heads[j], heads[j + 1] = heads[j + 1], heads[j]
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                tails[j], tails[j + 1] = tails[j + 1], tails[j]
                indices[j], indices[j + 1] = indices[j + 1], indices[j]

            elif heads[j] == heads[j + 1]:
                if int(numbers[j]) > int(numbers[j + 1]):
                    heads[j], heads[j + 1] = heads[j + 1], heads[j]
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                    tails[j], tails[j + 1] = tails[j + 1], tails[j]
                    indices[j], indices[j + 1] = indices[j + 1], indices[j]

    answer = list()
    for index in indices:
        answer.append(files[index])

    return answer
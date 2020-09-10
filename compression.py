def solution(msg):
    input_list = list()
    words_dict = dict()
    for i in range(1, 27):
        key = chr(i + 64)
        words_dict[key] = i

    msg_list = list(msg)

    last_val = 26
    idx = 0
    while True:
        if idx == len(msg_list):
            break
        string = ''
        while True:
            if idx == len(msg_list):
                input_list.append(words_dict[string])
                break
            string = string + msg_list[idx]
            if string not in words_dict:
                last_val = last_val + 1
                words_dict[string] = last_val
                input_list.append(words_dict[string[:-1]])
                break
            idx = idx + 1

    return input_list
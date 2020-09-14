def solution(m, musicinfos):
    m_len = list()
    m_name = list()
    melody = list()

    for info in musicinfos:
        time = 0
        info_list = info.split(',')

        hour = int(info_list[1][:2]) - int(info_list[0][:2])
        time = (hour*60) - int(info_list[0][-2:]) + int(info_list[1][-2:])

            # 02:58 03:08 => 60 * (03 - 02) - 58 + 08
        m_len.append(time)

        m_name.append(info_list[2])

        temp = list(info_list[3])
        real_list = list()
        idx = 0
        while True:
            if idx == len(temp):
                break
            if temp[idx] == '#':
                new = real_list.pop().lower()
                real_list.append(new)
            else:
                real_list.append(temp[idx])
            idx = idx + 1
        melody.append(real_list)

    # m도 #붙는거 구분해야함 고쳐야함
    temp = list(m)
    real_list = list()
    idx = 0
    # del 쓰지말자!! 오류의 주범임
    while True:
        if idx == len(temp):
            break
        if temp[idx] == '#':
            new = real_list.pop().lower()
            real_list.append(new)
        else:
            real_list.append(temp[idx])
        idx = idx + 1

    music = ''.join(real_list)
    print(music)

    cand = list()
    for i in range(len(musicinfos)):
        song = list()
        replays = int(m_len[i] / len(melody[i]))
        mod = m_len[i] % len(melody[i])
        # 아 딱 배수만큼 재생되지 않네.. 나머지 생각해야함
        for _ in range(replays):
            song = song + melody[i]
        song = song + melody[i][:mod]

        song_str = ''.join(song)
        print(song_str)
        print(len(song_str))

        if music in song_str:
            if len(cand) == 0:
                cand = [m_name[i], m_len[i]]
            else:
                if cand[1] < m_len[i]:
                    cand = [m_name[i], m_len[i]]

    print(m_len)
    if len(cand) == 0:
        return '(None)'
    else:
        return cand[0]

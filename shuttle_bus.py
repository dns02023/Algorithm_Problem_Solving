def solution(n, t, m, timetable):
    answer = ''
    # 시간은 전부 분 단위로 통일

    times = list()
    for time in timetable:
        temp = time.split(':')
        minute = int(temp[0]) * 60 + int(temp[1])
        times.append(minute)

    last = 540 + (n - 1) * t
    # 가장 늦게 오는 버스 시간

    # 먼저 콘이 타는 상황은 배제하고 나머지 크루들이 타는 상황들을 저장하자
    bus_crews = dict()
    start = 540
    sorted_times = sorted(times)
    for i in range(n):
        time = start + i * t
        bus = list()

        while len(bus) < m:
            if len(sorted_times) > 0:
                if time >= sorted_times[0]:
                    bus.append(sorted_times.pop(0))
                else:
                    break
            else:
                break
        bus_crews[time] = bus
    print(bus_crews)

    for arrive in range(last, start - t, -t):
        # 가장 늦게 오는 버스 시간 부터 내림차순
        crews = bus_crews[arrive]
        if len(crews) < m:
            answer = arrive
            break
        else:
            answer = crews[-1] - 1
            # 제일 뒤에 있는 크루보다 1분 일찍 와야 한다.
            break

    hour = int(answer / 60)
    minute = answer % 60

    if hour < 10:
        str_hour = '0' + str(hour)
    else:
        str_hour = str(hour)
    if minute < 10:
        str_minute = '0' + str(minute)
    else:
        str_minute = str(minute)
    result = str_hour + ':' + str_minute

    return result
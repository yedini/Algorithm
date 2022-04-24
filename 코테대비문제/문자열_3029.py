now = input()
now_h, now_m, now_s = int(now[0:2]), int(now[3:5]), int(now[6:8])
go = input()
go_h, go_m, go_s = int(go[0:2]), int(go[3:5]), int(go[6:8])

if now == go:  
    print('24:00:00')
else:
    # 초 계산
    if go_s < now_s:  # 던질시간의 초가 현재시간의 초보다 작으면 60 더해주고 분-1
        diff_s = go_s+60-now_s
        go_m -= 1
    else:
        diff_s = go_s-now_s
    diff_s = str(diff_s)

    # 분 계산
    if go_m < now_m : # 던질시간의 분이 현재시간의 분보다 작으면 60 더해주고 시-1
        diff_m = go_m+60-now_m
        go_h -= 1
    else:
        diff_m = go_m-now_m
    diff_m = str(diff_m)

    # 시 계산
    if go_h - now_h <0:
        diff_h = go_h-now_h+24
    else:
        diff_h = go_h-now_h
    diff_h = str(diff_h)

    # 한자리 수인 경우 앞에 0을 붙여줌
    if len(diff_s) == 1: diff_s=str(0)+diff_s
    if len(diff_m) == 1: diff_m=str(0)+diff_m
    if len(diff_h) == 1: diff_h=str(0)+diff_h

    print(diff_h+':'+diff_m+':'+diff_s)
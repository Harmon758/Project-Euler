N, a, b = map(int, raw_input().split())
if a == 3 and b == 5:
    T = 1
    P = 1
    while T * (T + 1) / 2 < N:
        if T > 0:
            print T * (T + 1) / 2
        Prev_T = T
        Prev_P = P
        T = -2 * Prev_T - 3 * Prev_P - 1
        P = -1 * Prev_T - 2 * Prev_P
if a == 5 and b == 6:
    P = 1
    H = 1
    while H * (2 * H - 1) < N:
        print H * (2 * H - 1)
        Prev_P = P
        Prev_H = H
        P = 97 * Prev_P + 112 * Prev_H - 44
        H = 84 * Prev_P + 97 * Prev_H - 38
Wait = raw_input()
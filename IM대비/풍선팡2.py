T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dr = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]   # 본인, 상, 하, 좌, 우
    mx = 0
    for r in range(N):
        for c in range(M):
            pang_sum = 0
            for d in dr:
                nr = d[0] + r
                nc = d[1] + c
                if 0 <= nr < N and 0 <= nc < M:
                    pang_sum += board[nr][nc]

            if mx < pang_sum:
                mx = pang_sum

    print(f'#{tc} {mx}')
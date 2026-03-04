def solution(sizes):
    wallet_min = []
    wallet_max = []

    for size in sizes:
        wallet_min.append(min(size))
        wallet_max.append(max(size))
    wallet_height = max(wallet_min)
    wallet_width = max(wallet_max)

    return wallet_height * wallet_width
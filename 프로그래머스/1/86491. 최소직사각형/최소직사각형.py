def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1], sizes[i][0]
    max_width = max(size[0] for size in sizes)
    max_height = max(size[1] for size in sizes)

    return max_height * max_width
progresses = [93, 30, 55]
speeds = [1, 30, 5]


def solution(progresses, speeds):
    answer = []
    size = len(progresses)
    to_do = [i for i in range(size - 1, -1, -1)]
    while len(to_do) > 0:
        cnt = 0
        for i in range(size):
            progresses[i] += speeds[i]

        while progresses[to_do[-1]] >= 100:
            to_do.pop()
            cnt += 1
        if cnt > 0:
            answer.append(cnt)

    return answer
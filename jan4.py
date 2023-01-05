def minimumRounds(tasks):
        diff, cnt = Counter(tasks), 0
        if 1 in diff.values():
            return -1
        for i in diff.values():
            cnt+=(i+2)//3
        return cnt
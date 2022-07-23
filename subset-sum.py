subset = set()

def is_safe(subset, j):
    if sum(subset) + j <= M:
        return True
    return False

def solve(subset):

    if sum(subset) == M:
            return True

    for i in INITIALSET.difference(subset):
        new_elemnet = i

        if is_safe(subset, new_elemnet):
            subset.add(new_elemnet)
            if solve(subset):
                return True

            subset.pop()

    return False


def main():
    solve(subset)
    print(subset)

if __name__ == "__main__":
    global M
    global INITIALSET
    INITIALSET = set([int(i) for i in input('nums = ').split(" ")])
    M = int(input('SUM = '))
    main()
    

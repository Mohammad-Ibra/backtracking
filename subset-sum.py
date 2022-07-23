subset = []

def is_safe(subset, j):
    if sum(subset) + INITIALSET[j] <= M:
        return True
    return False

def solve(subset, i):

    for j in range(i,len(INITIALSET)):

        if sum(subset) == M:
            return True

        if is_safe(subset, j):
            subset.append(INITIALSET[j])
            if solve(subset, i+1):
                return True

            subset.pop()

    return False


def main():
    solve(subset, 0)
    print(subset)

if __name__ == "__main__":
    global M
    global INITIALSET
    INITIALSET = [int(i) for i in input('nums = ').split(" ")]
    M = int(input('SUM = '))
    main()
    

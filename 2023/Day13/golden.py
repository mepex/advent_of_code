from itertools import chain


def find_mirrors(pattern):
    # Check vertical
    ncol = len(pattern[0])
    for i in range(1, ncol):
        mirrored = True
        for l in pattern:
            nm = min(i, ncol - i)
            left = l[i - nm:i]
            right = l[i:i + nm]
            if left != right[::-1]:
                mirrored = False
                break
        if mirrored:
            return i

    # Check horizontal
    nrow = len(pattern)
    for i in range(1, nrow):
        mirrored = True
        nm = min(i, nrow - i)
        top = pattern[i - nm:i]
        bot = pattern[i:i + nm][::-1]
        if any(lt != lb for lt, lb in zip(top, bot)):
            mirrored = False
            continue
        if mirrored:
            return 100 * i

    print("\n".join(pattern))
    raise ValueError("No line of reflection found")


def find_mirrors_smudged(pattern):
    # Check vertical
    ncol = len(pattern[0])
    for i in range(1, ncol):
        nm = min(i, ncol - i)
        ndiff = 0
        for l in pattern:
            left = l[i - nm:i]
            right = l[i:i + nm][::-1]
            for cl, cr in zip(left, right):
                ndiff += (cl != cr)
            if ndiff > 1:
                break
        if ndiff == 1:
            return i

    # Check horizontal
    nrow = len(pattern)
    for i in range(1, nrow):
        nm = min(i, nrow - i)
        top = pattern[i - nm:i]
        bot = pattern[i:i + nm]
        ndiff = 0
        for ct, cb in zip(chain.from_iterable(top), chain.from_iterable(bot[::-1])):
            ndiff += (ct != cb)
            if ndiff > 1:
                break
        if ndiff == 1:
            return 100 * i

    print("\n".join(pattern))
    raise ValueError("No line of reflection found")


def day13_part1(filename):
    with open(filename) as f:
        lines = f.read()
        mirrors = lines.split("\n\n")
        mirrors = list(map(lambda s: s.split("\n"), mirrors))
        mirrors[-1] = mirrors[-1][:-1]  # remove trailing newline

    return sum(find_mirrors(m) for m in mirrors)


def day13_part2(filename):
    with open(filename) as f:
        lines = f.read()
        mirrors = lines.split("\n\n")
        mirrors = list(map(lambda s: s.split("\n"), mirrors))
        mirrors[-1] = mirrors[-1][:-1]  # remove trailing newline
    for m in mirrors:
        rp = find_mirrors_smudged(m)
        print(f"v = {rp}")
    return sum(find_mirrors_smudged(m) for m in mirrors)


if __name__ == "__main__":
    print("Part 1 example", day13_part1("testinput.txt"))
    print("Part 1", day13_part1("input.txt"))
    print("Part 2 example", day13_part2("testinput.txt"))
    print("Part 2", day13_part2("input.txt"))

def single_number(l: list[int]) -> int:
    sorted_l = sorted(l)
    stack = []

    for val in sorted_l:
        if val not in stack:
            stack.append(val)
        elif val in stack:
            stack.pop()

    return stack[0]


def main() -> None:
    print(single_number([1, 0, 1]))


if __name__ == '__main__':
    main()

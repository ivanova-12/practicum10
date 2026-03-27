def specific_numbers(A: int, B: int) -> None:
    """Print all numbers between A and B
    which have all nums from {1, 3, 4, 8, 9}
    """
    all_spec_symbol = [1, 3, 4, 8, 9]
    cnt = 0
    spec_nums = []

    if A < B:
        for num in range(A, B + 1):
            for elem in str(num):
                if int(elem) in all_spec_symbol:
                    cnt += 1
                    all_spec_symbol.remove(int(elem))
                    if cnt == 5:
                        spec_nums.append(num)
                        break
            cnt = 0
            all_spec_symbol = [1, 3, 4, 8, 9]

    elif A == B:
        for elem in str(A):
            if int(elem) in all_spec_symbol:
                cnt += 1
                all_spec_symbol.remove(int(elem))
                if cnt == 5:
                    spec_nums.append(A)
                    break

    else:
        A, B = B, A
        for num in range(A, B + 1):
            for elem in str(num):
                if int(elem) in all_spec_symbol:
                    cnt += 1
                    all_spec_symbol.remove(int(elem))
                    if cnt == 5:
                        spec_nums.append(num)
                        break
            cnt = 0
            all_spec_symbol = [1, 3, 4, 8, 9]

    print(*spec_nums)















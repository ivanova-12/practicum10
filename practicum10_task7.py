def is_prime(num: int) -> bool:
    """Check if number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def common_multiple(A: int, B: int, N: int) -> None:
    """Return common multiple of A and B"""
    list_of_cm = []

    if is_prime(A) and is_prime(B):
        common_mltpl = A * B

        for i in range(1, N*2):
            common_mltpl *= i

            if common_mltpl <= N:
                list_of_cm.append(str(common_mltpl))
                common_mltpl = A * B
            else:
                break

    else:
        if A > B:
            composition = A * B
            surplus = A % B

            while surplus != 0:
                A = B
                B = surplus
                surplus = A % B

            if surplus == 0:
                the_biggest_divisor = B
                common_mltpl = composition // B

                for i in range(1, N*2):
                    common_mltpl *= i

                    if common_mltpl <= N:
                        list_of_cm.append(str(common_mltpl))
                        common_mltpl = composition // B
                    else:
                        break
        if A == B:
            common_mltpl = A

            for i in range(1, N*2):
                common_mltpl *= i

                if common_mltpl <= N:
                    list_of_cm.append(str(common_mltpl))
                    common_mltpl = A
                else:
                    break
        else:
            composition = A * B
            surplus = B % A

            while surplus != 0:
                B = A
                A = surplus
                surplus = B % A

            if surplus == 0:
                the_biggest_divisor = A
                common_mltpl = composition // A

                for i in range(1, N * 2):
                    common_mltpl *= i

                    if common_mltpl <= N:
                        list_of_cm.append(str(common_mltpl))
                        common_mltpl = composition // A
                    else:
                        break

    print(*list_of_cm)
    

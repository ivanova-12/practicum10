def num_of_fibonachi(n: int) -> None:
    """Prints the first n Fibonacci numbers
    Args: number of the last Fibonacci number
    Returns: None
    """
    all_nums = [1,]
    num = 0

    for i in range(n - 1):
        num += all_nums[-1]
        all_nums.append(num)
        num = all_nums[-2]

    print(*all_nums)














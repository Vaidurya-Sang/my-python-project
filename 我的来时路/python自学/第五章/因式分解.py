def factorize(n):
    """
    将正整数n分解为质因数的乘积

    参数:
        n: 待分解的正整数

    返回:
        字典，键为质因数，值为对应质因数的指数
    """
    if not isinstance(n, int) or n <= 0:
            raise ValueError("输入必须是正整数")

    factors = {}

    # 处理2的情况
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n = n // 2

    # 处理奇数的情况
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors[i] = factors.get(i, 0) + 1
            n = n // i
        i += 2

    # 如果剩余的n是一个质数
    if n > 1:
        factors[n] = 1

    return factors


def format_factorization(factors):
    """将质因数字典格式化为易读的字符串形式"""
    if not factors:
        return "1"

    parts = []
    for prime, exp in sorted(factors.items()):
        if exp == 1:
            parts.append(f"{prime}")
        else:
            parts.append(f"{prime}^{exp}")

    return " × ".join(parts)


if __name__ == "__main__":
    try:
        num = int(input("请输入一个正整数: "))
        factors = factorize(num)
        print(f"{num} 的因式分解结果为: {format_factorization(factors)}")
    except ValueError as e:
        print(f"错误: {e}")

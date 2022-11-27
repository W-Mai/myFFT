from typing import List
import math


# f_0 = a_0 * x_0^2 + ...
# f_1 = a_4 * x_0^2 + ...
# f = f_0 + x * f_1


def fft(arr: List[complex], inverse: bool):
    n = len(arr)

    if n == 1:
        return arr

    w = math.cos(2 * math.pi / n) + math.sin(2 * math.pi / n) * (-1j if inverse else 1j)

    res0 = fft(arr[::2], inverse)
    res1 = fft(arr[1::2], inverse)

    res = [0 + 0j] * n
    for i in range(n >> 1):
        res[i] = res0[i] + res1[i] * w ** i
        res[i + (n >> 1)] = res0[i] - res1[i] * w ** i

    return res


if __name__ == '__main__':
    f1 = fft([5, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], False)
    f2 = fft([0, 9, 8, 7, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], False)

    print(f1)
    print(f2)

    f = list(map(lambda x: (x[0] * x[1]), zip(f1, f2)))
    f = list(map(lambda x: round(x.real / 16), fft(f, True)))
    print(f)

    print()

    sum0 = 0
    carry = 0
    p = 1
    for i in f:
        div, mod = divmod(i + carry, 10)
        carry = div
        sum0 += mod * p
        p *= 10

    assert sum0 == 12345 * 67890

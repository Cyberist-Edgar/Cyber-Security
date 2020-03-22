import time
import math


def isPrime(num):
    """直接计算是否是素数"""
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count += 1
            return False
    return True


def isPrime2(num):
    """
    定理1.1.7 和 欧几里得除法
    首先找出 <= sqrt(num) 的所有素数，如果num不能够被其中的任意一个整除，那么便是素数
    """
    prime_list = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if isPrime(i):
            prime_list.append(i)

    for prime in prime_list:
        if num % prime == 0:
            return False
    return True


def prime(num):
    """
    厄拉托塞师筛法
    首先找出 <= sqrt(num) 的所有素数， 然后对从1到num中删除掉素数的倍数
    """
    prime_list = []
    for i in range(2, int(math.sqrt(num)) + 1):
        if isPrime(i):
            prime_list.append(i)
    all_num = [i for i in range(2, num + 1)]
    for prime in prime_list:
        for i in all_num:
            if i % prime == 0 and i / prime > 1:
                all_num.remove(i)
    return all_num


start_time = time.time()
print(isPrime2(1601))
end_time = time.time()


print("Cost:", end_time - start_time)



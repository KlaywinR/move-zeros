from collections import deque


def mover_zeros_fila(nums):
    fila = deque()
    zeros = 0

    for num in nums:
        if num == 0:
            zeros += 1
        else:
            fila.append(num)

    i = 0

    while fila:
        nums[i] = fila.popleft()
        i += 1

    while zeros > 0:
        nums[i] = 0
        i += 1
        zeros -= 1

    return nums


nums = [0, 1, 0, 3, 12]


mover_zeros_fila(nums)

print(nums)
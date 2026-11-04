
from collections import deque
from time import perf_counter
import sys


def mover_zeros_in_place(nums):
    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos] = nums[i]
            pos += 1

    while pos < len(nums):
        nums[pos] = 0
        pos += 1

    return nums


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

def medir(funcao, entrada):
    nums = entrada.copy()  
    inicio = perf_counter()
    funcao(nums)
    tempo = perf_counter() - inicio
    return nums, tempo


def main():

    nums = [0, 1, 0, 3, 12]

    resultado_in_place, tempo_in_place = medir(mover_zeros_in_place, nums)
    resultado_fila, tempo_fila = medir(mover_zeros_fila, nums)

    print("Array original:", nums)
    print("Tamanho do array:", len(nums), "elementos")
    print()

    print("Com a solução usando in-place")
    print("Resultado:", resultado_in_place)
    print(f"Tempo medido: {tempo_in_place:.8f} segundos")
    print("Complexidade de tempo: O(n)")
    print("Complexidade de espaço auxiliar: O(1)")
    print()

    print("Com a solução usando fila")
    print("Resultado:", resultado_fila)
    print(f"Tempo medido: {tempo_fila:.8f} segundos")
    print("Complexidade de tempo: O(n)")
    print("Complexidade de espaço auxiliar: O(n)")


if __name__ == "__main__":
    main()

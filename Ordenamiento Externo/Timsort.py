# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 13:48:14 2023

@author: PC
"""

def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        key_item = arr[i]
        j = i - 1

        while j >= left and arr[j] > key_item:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key_item

def merge(arr, left, mid, right):
    if arr[mid - 1] <= arr[mid]:
        return

    i = left
    j = mid
    temp = []

    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i < mid:
        temp.append(arr[i])
        i += 1

    for i in range(len(temp)):
        arr[left + i] = temp[i]

def timsort(arr):
    min_run = 32
    n = len(arr)

    for i in range(0, n, min_run):
        insertion_sort(arr, i, min((i + min_run - 1), n - 1))

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = min((start + size - 1), (n - 1))
            end = min((start + size * 2 - 1), (n - 1))
            merge(arr, start, midpoint, end)
        size *= 2

# Ejemplo de uso
arr = [64, 34, 25, 12, 22, 11, 90]
timsort(arr)

print("Lista ordenada:")
for element in arr:
    print(element)

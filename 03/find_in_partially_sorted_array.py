#!/usr/bin/env python3


def find(num, matrix):
    if not matrix:
        return False
    row = 0
    column = len(matrix[0]) - 1
    while row < len(matrix) and column >= 0:
        if matrix[row][column] > num:
            column -= 1
        elif matrix[row][column] < num:
            row += 1
        else:
            return True
    return False

#!/usr/bin/python3
"""defines pascal_triangle function"""


def pascal_triangle(n):
    """
        This function creates a pascal triangle of n

        Args:
            n(int): number/height of triangle

        Return: an empty list if n <= 0 or
            a list of lists of integers representing the pascal triangle of n

    """
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])
    if n == 1:
        return triangle
    triangle.append([1, 1])
    if n == 2:
        return triangle
    for i in range(0, n - 2):
        new_list = [1, 1]
        old_list = triangle[-1]
        for j in range(0, len(old_list) - 1):
            new_num = old_list[j] + old_list[j + 1]
            new_list.insert(j+1, new_num)
        triangle.append(new_list)
    return triangle

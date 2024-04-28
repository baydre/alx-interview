#!/usr/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Traverse each layer from outer to inner
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        # Traverse each element in the current layer
        for i in range(first, last):
            # Save top element
            top = matrix[first][i]

            # Move left element to top
            matrix[first][i] = matrix[last - (i - first)][first]

            # Move bottom element to left
            matrix[last - (i - first)][first]\
                = matrix[last][last - (i - first)]

            # Move right element to bottom
            matrix[last][last - (i - first)] = matrix[i][last]

            # Move top element to right
            matrix[i][last] = top

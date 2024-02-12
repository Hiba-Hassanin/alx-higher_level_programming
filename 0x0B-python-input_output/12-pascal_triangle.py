#!/usr/bin/python3


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): The number of rows in the Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        if i > 0:
            prev_row = triangle[i - 1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])  # Middle elements
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle

def print_triangle(triangle):
    """
    Print the triangle.

    Args:
        triangle (list): A list of lists representing Pascal's triangle.

    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

# Test the function
if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)

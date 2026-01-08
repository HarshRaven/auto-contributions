# Python: Generates a spiral pattern of numbers within a square matrix.

def generate_spiral_matrix(n):
    if n <= 0:
        return []

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    num = 1
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1

    while row_start <= row_end and col_start <= col_end:
        # Traverse right
        for col in range(col_start, col_end + 1):
            matrix[row_start][col] = num
            num += 1
        row_start += 1

        # Traverse down
        for row in range(row_start, row_end + 1):
            matrix[row][col_end] = num
            num += 1
        col_end -= 1

        # Traverse left
        if row_start <= row_end:
            for col in range(col_end, col_start - 1, -1):
                matrix[row_end][col] = num
                num += 1
            row_end -= 1

        # Traverse up
        if col_start <= col_end:
            for row in range(row_end, row_start - 1, -1):
                matrix[row][col_start] = num
                num += 1
            col_start += 1
    return matrix

if __name__ == '__main__':
    size = 4
    spiral = generate_spiral_matrix(size)
    for row in spiral:
        print(" ".join(f"{x:2d}" for x in row))

    print("\n")

    size = 5
    spiral = generate_spiral_matrix(size)
    for row in spiral:
        print(" ".join(f"{x:2d}" for x in row))
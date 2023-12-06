def maximalSquare(matrix):
    if not matrix or not matrix[0]:
        return 0

    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side


def take_matrix_input(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = input(f"Enter element at position ({i+1}, {j+1}): ")
            row.append(element)
        matrix.append(row)
    return matrix


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix1 = take_matrix_input(rows, cols)

print(maximalSquare(matrix1))